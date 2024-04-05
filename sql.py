import sqlite3

## Connectt to SQlite
connection=sqlite3.connect("University.db")

# Create a cursor object to insert record,create table

cursor=connection.cursor()

## create the table
student_info="""
CREATE TABLE students (
  student_id INT PRIMARY KEY,
  student_name VARCHAR(255),
  dob DATE,
  major_id INT,
  enrollment_status VARCHAR(20)
);
"""
courses_info="""
CREATE TABLE courses (
  course_code VARCHAR(10) PRIMARY KEY,
  course_name VARCHAR(255),
  room_number VARCHAR(20),
  semester VARCHAR(20),
  credits INT
);"""
enrollments_info="""

CREATE TABLE enrollments (
  enrollment_id INT PRIMARY KEY,
  student_id INT,
  course_code VARCHAR(10),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_code) REFERENCES courses(course_code)
);"""
grades_info="""
CREATE TABLE grades (
  grade_id INT PRIMARY KEY,
  student_id INT,
  course_code VARCHAR(10),
  grade VARCHAR(2),
  FOREIGN KEY (student_id) REFERENCES students(student_id),
  FOREIGN KEY (course_code) REFERENCES courses(course_code)
);"""
prereq_info="""
CREATE TABLE prerequisites (
  prerequisite_id INT PRIMARY KEY,
  course_code VARCHAR(10),
  prerequisite_course VARCHAR(10),
  FOREIGN KEY (course_code) REFERENCES courses(course_code),
  FOREIGN KEY (prerequisite_course) REFERENCES courses(course_code)
);"""
major_info="""
CREATE TABLE majors (
  major_id INT PRIMARY KEY,
  major_name VARCHAR(50)
);
"""
cursor.execute(student_info)
cursor.execute(courses_info)
cursor.execute(enrollments_info)
cursor.execute(grades_info)
cursor.execute(prereq_info)
cursor.execute(major_info)


## Insert Some more records

# cursor.execute('''Insert Into STUDENT values('Krish','Data Science','A',90)''')
# cursor.execute('''Insert Into STUDENT values('Sudhanshu','Data Science','B',100)''')
# cursor.execute('''Insert Into STUDENT values('Darius','Data Science','A',86)''')
# cursor.execute('''Insert Into STUDENT values('Vikash','DEVOPS','A',50)''')
# cursor.execute('''Insert Into STUDENT values('Dipesh','DEVOPS','A',35)''')
cursor.execute('''INSERT INTO students (student_id, student_name, dob, major_id, enrollment_status) VALUES
(1, 'John Doe', '2001-04-12', 1, 'Enrolled'),
(2, 'Jane Smith', '2000-05-19', 2, 'Enrolled'),
(3, 'Alice Johnson', '2002-06-22', 3, 'Enrolled'),
(4, 'Mike Brown', '1999-07-30', 4, 'Enrolled'),
(5, 'Emma Wilson', '2001-09-14', 5, 'Enrolled'),
(6, 'Liam Miller', '2003-08-05', 1, 'Enrolled'),
(7, 'Sophia Davis', '2000-12-17', 2, 'Enrolled'),
(8, 'Lucas Garcia', '2002-11-23', 3, 'Enrolled'),
(9, 'Mia Rodriguez', '2001-01-10', 4, 'Enrolled'),
(10, 'David Martinez', '2003-03-15', 5, 'Enrolled');''')

cursor.execute('''INSERT INTO courses (course_code, course_name, room_number, semester, credits) VALUES
('CS101', 'Introduction to Computer Science', '101', 'Fall 2024', 4),
('MATH201', 'Advanced Calculus', '202', 'Spring 2024', 3),
('PHY301', 'Quantum Physics', '303', 'Fall 2024', 4),
('ENG401', 'Mechanical Engineering Basics', '404', 'Spring 2024', 3),
('BIO501', 'Molecular Biology', '505', 'Fall 2024', 4),
('CHEM601', 'Organic Chemistry', '606', 'Spring 2024', 3),
('LIT701', 'Shakespearean Literature', '707', 'Fall 2024', 4),
('HIST801', 'World History', '808', 'Spring 2024', 3),
('ART901', 'Modern Art and Society', '909', 'Fall 2024', 4),
('POL1001', 'Introduction to Political Science', '100', 'Spring 2024', 3);''')

cursor.execute('''INSERT INTO enrollments (enrollment_id, student_id, course_code) VALUES
(1, 1, 'CS101'),
(2, 2, 'MATH201'),
(3, 3, 'PHY301'),
(4, 4, 'ENG401'),
(5, 5, 'BIO501'),
(6, 6, 'CHEM601'),
(7, 7, 'LIT701'),
(8, 8, 'HIST801'),
(9, 9, 'ART901'),
(10, 10, 'POL1001');''')

cursor.execute('''INSERT INTO grades (grade_id, student_id, course_code, grade) VALUES
(1, 1, 'CS101', 'A'),
(2, 2, 'MATH201', 'B'),
(3, 3, 'PHY301', 'C'),
(4, 4, 'ENG401', 'A'),
(5, 5, 'BIO501', 'B'),
(6, 6, 'CHEM601', 'C'),
(7, 7, 'LIT701', 'A'),
(8, 8, 'HIST801', 'B'),
(9, 9, 'ART901', 'C'),
(10, 10, 'POL1001', 'A');''')

cursor.execute('''INSERT INTO prerequisites (prerequisite_id, course_code, prerequisite_course) VALUES
(1, 'CS101', 'MATH201'),
(2, 'PHY301', 'MATH201'),
(3, 'ENG401', 'PHY301'),
(4, 'BIO501', 'CHEM601'),
(5, 'POL1001', 'HIST801');''')

cursor.execute('''INSERT INTO majors (major_id, major_name) VALUES
(1, 'Computer Science'),
(2, 'Mathematics'),
(3, 'Physics'),
(4, 'Engineering'),
(5, 'Biology');''')

## Disspaly ALl the records

print("The isnerted records are")
data=cursor.execute('''Select * from students''')
for row in data:
    print(row)

## Commit your changes int he databse
connection.commit()
connection.close()