import re
import sqlite3
# input_string = """
# -- Update the student_name column in the students table
# UPDATE students
# SET student_name = 'JonnyDep'
# WHERE student_name = 'John Doe';

# -- Check if the update was successful
# SELECT student_name
# FROM students
# WHERE student_name = 'JonnyDep';
# """

input_string="""
```sql
SELECT
  *
FROM Students;
```
```sql
DELETE FROM Students
WHERE student_name = 'John Dor';
```"""
# Define a pattern to match the SQL statements
# pattern = r"(UPDATE\s+.+?; |DELETE\s+.+?;|SELECT\s+.+?;)"
# pattern = r"(SELECT\s.+?(?=SELECT|UPDATE|DELETE|INSERT|$)|UPDATE\s.+?(?=SELECT|UPDATE|DELETE|INSERT|$)|DELETE\s.+?(?=SELECT|UPDATE|DELETE|INSERT|$);|INSERT\s+INTO\s.+?(?=SELECT|UPDATE|DELETE|INSERT|$))"
# pattern = r"(SELECT\s.+?;|UPDATE\s.+?;|DELETE\s.+?;|INSERT\s+INTO\s.+?;)"

# # Use re.findall to extract all occurrences that match the pattern
# getqueries = re.findall(pattern, input_string, re.DOTALL)
# formatqueries = [statement.replace("\n", " ") for statement in getqueries]
# if len(formatqueries) == 2 and formatqueries[0].startswith("SELECT"):
#     formatqueries[0], formatqueries[1] = formatqueries[1], formatqueries[0]

