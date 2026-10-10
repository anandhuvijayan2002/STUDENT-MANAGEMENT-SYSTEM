# Student Management System
this is a simple console-based application developed using Python and SQLite. The system is designed to manage student information in an easy and organized way. It provides separate login options for teachers and students. Teachers can add, view, update, and delete student details and enter marks. Students can view their details and marks.
## Features
-   Teacher and student login options
-   Teacher can Add student records
-   teacher and student login can View student records
-   teacher can Update student details
-   teacher can Delete student records
-   teacher can Enter and update student marks
-   SQLite database for persistent storage
 
  ## Technologies Used

-   **Python 3** --- application logic
-   **SQLite** --- database
-   **Visual Studio Code** --- development environment
## Requirements

-   Python 3 installed
-   Visual Studio Code (recommended)
-   ## Database Tables

### `users`
 |Column| Type |Purpose|
 |------|------|-------|
 |`id`  |INTEGER|Unique user ID|
 | `username`|TEXT|Login username|
 |`password`|   TEXT |     Login password
 |`role`   |    TEXT  |    User role, such as teacher or student

 ### `students`
 |Column| Type |Purpose|
 |------|------|-------|
 |`id`  |INTEGER|Unique student ID|
 |`name`|TEXT   |   Student name|
 |`age` |     INTEGER|   Student age
 |`course`|   TEXT    |  Student course
 |`marks`  |  INTEGER  | Student marks

## Learning Objectives
-   Practice Python functions, loops, conditions, and user input
-   Connect Python to SQLite
-   Perform basic SQL operations (`INSERT`, `SELECT`, `UPDATE`, and
    `DELETE`) IT CAN WORK "CRUD"OPERATION
## Future Improvements

-   Search for a student by ID or name
-   Calculate grades and display results
-   Restrict students to viewing only their own records
-   Hash passwords securely
-   Build a graphical user interface

  
  
