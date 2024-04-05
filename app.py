from dotenv import load_dotenv
load_dotenv() ## load all the environemnt variables

import streamlit as st
import os
import sqlite3
import pandas as pd
import google.generativeai as genai
import re
## Configure Genai Key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function To Load Google Gemini Model and provide queries as response

def get_gemini_response(question,prompt):
    model=genai.GenerativeModel('gemini-pro')
    response=model.generate_content([prompt[0],question])
    return response.text

## Fucntion To retrieve data from the database

def read_sql_query(sql,db):
    conn=sqlite3.connect(db)
    cur=conn.cursor()
    df=pd.DataFrame()
    if "select" in sql.lower():
        cur.execute(sql)
        rows=cur.fetchall()
        column_headers = [description[0] for description in cur.description]
        df = pd.DataFrame(rows, columns=column_headers)
        df.columns = [col.replace('_', ' ').title() for col in df.columns]
        df.index = range(1, len(df) + 1)
        print("hello")
    else:
        cur.execute(sql)
        df.add("Changes effected")
    conn.commit()
    conn.close()
    return df

## Fucntion To retrieve database info and results custom prompt
def getdatabaseinfo():
    dbtableinfo=""
    tablecolumninfo=""
    connection=sqlite3.connect("University.db")
    cursor=connection.cursor()
    # Step 1: Get a list of all tables in the database
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()  # Each item in 'tables' is a tuple where the first item is the table name

    # Step 2: For each table, retrieve column details
    tables_columns = {}  # Dictionary to store table names as keys and column names as values
    for table in tables:
        table_name = table[0]
        cursor.execute(f"PRAGMA table_info({table_name});")
        columns = cursor.fetchall()
        # Extract column names from the PRAGMA output (column name is in position 1 of the tuple)
        column_names = [column[1] for column in columns]
        tables_columns[table_name] = column_names
    # Print the result
    for table, columns in tables_columns.items():
        dbtableinfo += f"'{table}',"
        tablecolumninfo    += f"For '{table}' has columns: {columns}"
    connection.commit()
    connection.close()
    prompt=[
    f"""
    You are an expert in converting English questions to SQL query!
    The SQL database has the name University and has the following precise information from a database. 
    The database you are working with contains several tables related to a college's academic 
    records: {dbtableinfo}.
    where {tablecolumninfo}
    """
    ]
    return prompt

if 'conversation' not in st.session_state:
    st.session_state.conversation = []

st.header("Custom Database LLM Text to SQL")

def handle_enter():
    question = st.session_state.question  # Access the user input from the session state
    if question:  # Check if the input is not empty
        try:
            st.session_state.conversation.append(f"You: {question}")
            response=get_gemini_response(question,getdatabaseinfo())
           
            pattern = r"(SELECT\s.+?;|UPDATE\s.+?;|DELETE\s.+?;|CREATE\s.+?;|INSERT\s+INTO\s.+?;)"
            getqueries = re.findall(pattern, response, re.DOTALL)
            formatqueries = [getqueries.replace("\n", " ") for getqueries in getqueries]
            if len(formatqueries) == 2 and formatqueries[0].startswith("SELECT"):
                formatqueries[0], formatqueries[1] = formatqueries[1], formatqueries[0]
            # print(response)
            for fq in formatqueries:
                print(fq)
                df1=read_sql_query(fq,"University.db")
                st.session_state.conversation.append(f"SQLGpt:")
                st.session_state.conversation.append(df1)

           
        except Exception as e:
            if str(e)=="You can only execute one statement at a time":
                st.session_state.conversation.append(f"SQLGpt: Current you can just get information from the table")
            else:
                 st.session_state.conversation.append(f"SQLGpt: Error - {e}")
        finally:
             st.session_state.question = ""
conversation_container = st.container()
question=st.text_input("Ask a question about University Information:", key='question', on_change=handle_enter)

with conversation_container:
   for item in st.session_state.conversation:
    if isinstance(item, pd.DataFrame):
        # If the item is a DataFrame, display it as a table
        st.table(item)
    else:
        # Otherwise, display the item as text
        st.write(item)




