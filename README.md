
# CSC500 Module 7 – Course Information System

## Project Overview

This project was developed for the Module 7 Critical Thinking Assignment, Robust Function Development, in CSC500: Principles of Programming at Colorado State University Global.

The Course Information System is a Python program that allows users to enter a course number and retrieve the corresponding room number, instructor, and meeting time.

The program uses three separate dictionaries, a user-defined function, exception handling, and a while loop to process multiple course lookups during one session.

## Program Features

- Stores course information using three separate Python dictionaries.
- Uses course numbers as dictionary keys.
- Retrieves room numbers, instructors, and meeting times.
- Uses a user-defined function to organize the lookup process.
- Uses 'try' and 'except KeyError' to handle invalid course numbers without crashing.
- Allows multiple course lookups using a 'while' loop.
- Accepts lowercase course numbers and removes extra spaces.
- Allows users to enter 'Q' to exit the program.

## Course Data

| Course Number | Room Number | Instructor | Meeting Time |
|---     |---   |---       |---                 |
| CSC101 | 3004 | Haynes   | Monday 9:00 AM     |
| CSC102 | 4501 | Alvarado | Tuesday 10:00 AM   |
| CSC103 | 6755 | Rich     | Wednesday 11:00 AM |
| NET110 | 1244 | Burke    | Thursday 1:00 PM   |
| COM241 | 1411 | Lee      | Friday 2:00 PM     |

### Meeting Time Clarification

The assignment provides room numbers and instructors but does not include meeting times.

On October 29, 2026, Dr. Brian Holbert confirmed by email that students could either allow users to enter meeting times or create fictional meeting times for the assignment.

Based on this clarification, the third dictionary contains five fictional meeting times.

These meeting times are used for demonstration purposes only and do not represent official course schedules.

## Technologies Used

- Python 3.14
- Visual Studio Code
- GitHub

## How to Run the Program

1. Download `CSC500_Module7_Course_Information.py` from this repository.
2. Open the file in Visual Studio Code.
3. Open the integrated terminal.
4. Navigate to the folder containing the Python file.
5. Execute the following command:

```bash
python CSC500_Module7_Course_Information.py
```

6. Enter a course number when prompted.
7. Continue entering course numbers or type 'Q' to quit.

## Example Program Execution

The following example illustrates the expected program output:

```text
COURSE INFORMATION SYSTEM

Enter a course number (or Q to quit): CSC101
Course Number: CSC101
Room Number: 3004
Instructor: Haynes
Meeting Time: Monday 9:00 AM

Enter a course number (or Q to quit): CSC102
Course Number: CSC102
Room Number: 4501
Instructor: Alvarado
Meeting Time: Tuesday 10:00 AM

Enter a course number (or Q to quit): CSC999
Course CSC999 was not found. Please check the course number.

Enter a course number (or Q to quit): Q
Thank you for using the Course Information System.
```

## Program Testing

The program is designed to support the following test cases:

| Test Input | Expected Result |
|---|---|
| CSC101 | Room 3004, Haynes, Monday 9:00 AM |
| CSC102 | Room 4501, Alvarado, Tuesday 10:00 AM |
| CSC103 | Room 6755, Rich, Wednesday 11:00 AM |
| NET110 | Room 1244, Burke, Thursday 1:00 PM |
| COM241 | Room 1411, Lee, Friday 2:00 PM |
| CSC999 | Friendly not-found message |
| csc101 | Accepted as CSC101 |
| Input with spaces | Spaces removed; valid course retrieved |
| 12345 | Friendly not-found message |
| Blank input | Friendly not-found message |
| Q | Program exits normally |

### Expected Program Behavior

- Correct course information is displayed for valid course numbers.
- Invalid course numbers produce a friendly error message without crashing the program.
- Lowercase course numbers are converted to uppercase.
- Leading and trailing spaces are removed.
- The program continues prompting after each lookup.
- Entering 'Q' terminates the program normally.

## Project Files

- `CSC500_Module7_Course_Information.py` – Complete Python source code.
- `README.md` – Project description, execution instructions, and testing information.

## Academic Information

**University:** Colorado State University Global

**Course:** CSC500 – Principles of Programming

**Instructor:** Dr. Brian Holbert

**Assignment:** Module 7 Critical Thinking Assignment – Robust Function Development

**Date:** October 30, 2026

## References

Python Software Foundation. (2026). *The Python tutorial*. https://docs.python.org/3/tutorial/

Python Software Foundation. (2026). *Errors and exceptions*. https://docs.python.org/3/tutorial/errors.html
