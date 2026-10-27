CSC500 Module 7 – Course Information System

Project Overview

This project was developed for the Module 7 Critical Thinking Assignment, Robust Function Development, in CSC500: Principles of Programming at Colorado State University Global.

The Course Information System is a Python program that allows users to enter a course number and retrieve the corresponding room number, instructor, and meeting time.

The program uses three separate dictionaries, a user-defined function, exception handling, and a while loop to process multiple course lookups during one session.

Program Features

Stores course information using three separate Python dictionaries.

Uses course numbers as dictionary keys.

Retrieves room numbers, instructors, and meeting times.

Uses a user-defined function to organize the lookup process.

Uses try and except KeyError to handle invalid course numbers without crashing.

Allows multiple course lookups using a while loop.

Accepts lowercase course numbers and removes extra spaces.

Allows users to enter Q to exit the program.

Course Data

Course Number

Room Number

Instructor

CSC101

3004

Haynes

CSC102

4501

Alvarado

CSC103

6755

Rich

NET110

1244

Burke

COM241

1411

Lee

Meeting Time Note: The assignment provides room numbers and instructors but does not include meeting times. The third dictionary contains the placeholder "Not provided in assignment" for each course rather than using invented meeting times.

Technologies Used

Python 3.14

Visual Studio Code

GitHub

How to Run the Program

Download the Python file from this repository.

Open the file in Visual Studio Code.

Open the integrated terminal.

Navigate to the folder containing the Python file.

Execute the following command:

python CSC500_Module7_Course_Information.py

Enter a course number when prompted.

Continue entering course numbers or type Q to quit.

Example Program Execution

COURSE INFORMATION SYSTEM

Enter a course number (or Q to quit): CSC101
Course Number: CSC101
Room Number: 3004
Instructor: Haynes
Meeting Time: Not provided in assignment

Enter a course number (or Q to quit): CSC102
Course Number: CSC102
Room Number: 4501
Instructor: Alvarado
Meeting Time: Not provided in assignment

Enter a course number (or Q to quit): CSC999
Course CSC999 was not found. Please check the course number.

Enter a course number (or Q to quit): Q
Thank you for using the Course Information System.

Program Testing

The program is designed to support the following tests:

Valid course numbers: CSC101, CSC102, CSC103, NET110, COM241.

Invalid course number: CSC999.

Lowercase input: csc101.

Input with leading and trailing spaces.

Numeric input: 12345.

Blank input.

Program termination using Q.

Expected behavior includes accurate course information, friendly error messages, continued prompting after lookups, and normal program termination.

Project Files

CSC500_Module7_Course_Information.py – Complete Python source code.

README.md – Project description, execution instructions, and testing information.

Academic Information

University: Colorado State University Global
Course: CSC500 – Principles of Programming
Instructor: Dr. Brian Holbert
Assignment: Module 7 Critical Thinking Assignment – Robust Function Development
Date: October 27, 2026

References

Python Software Foundation. (2026). The Python tutorial. https://docs.python.org/3/tutorial/

Python Software Foundation. (2026). Errors and exceptions. https://docs.python.org/3/tutorial/errors.html
