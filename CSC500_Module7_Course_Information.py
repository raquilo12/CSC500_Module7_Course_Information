
# ------------------------------------------------------------
# Student: Richard Aquilo Jr.
# University: Colorado State University Global
# Course: CSC500 - Principles of Programming
# Instructor: Dr. Brian Holbert
# Assignment: Module 7 Critical Thinking Assignment
# Assignment Title: Robust Function Development
# Program: Course Information System
# Date: October 27, 2026 version 3
# ------------------------------------------------------------
# Purpose:
# This program allows a user to enter course numbers and see
# the corresponding room numbers, instructors, and meeting times.
#
# Three separate dictionaries store the course information.
# A user-defined function retrieves and displays the results.
#
# Exception handling prevents the program from crashing if
# the user enters a course number that is not in the data.
#
# A while loop allows the user to look up multiple courses
# without restarting the program.
#
# The user can enter Q at any time to exit the program.
#
# IMPORTANT:
# The assignment's data table does not supply meeting times.
# The third dictionary uses clearly identified placeholders
# until the instructor confirms the official meeting times.
# ------------------------------------------------------------


# STEP 1: CREATE THREE SEPARATE DICTIONARIES.
# Each dictionary uses the course number as its key.

# The first dictionary maps each course to its room number.
# Room numbers are stored as strings because they are
# displayed rather than used in mathematical calculations.

course_rooms = {
    "CSC101": "3004",   # CSC101 meets in room 3004.
    "CSC102": "4501",   # CSC102 meets in room 4501.
    "CSC103": "6755",   # CSC103 meets in room 6755.
    "NET110": "1244",   # NET110 meets in room 1244.
    "COM241": "1411",   # COM241 meets in room 1411.
}


# The second dictionary uses the same course-number keys.
# Its values contain the instructors' last names.

course_instructors = {
    "CSC101": "Haynes",     # Instructor for CSC101.
    "CSC102": "Alvarado",   # Instructor for CSC102.
    "CSC103": "Rich",       # Instructor for CSC103.
    "NET110": "Burke",      # Instructor for NET110.
    "COM241": "Lee",        # Instructor for COM241.
}


# The third dictionary stores the meeting times.
# The assignment requires three dictionaries but does not
# provide actual meeting times in its data table.
#
# The placeholders avoid presenting invented times as facts.

course_times = {
    "CSC101": "Not provided in assignment",
    "CSC102": "Not provided in assignment",
    "CSC103": "Not provided in assignment",
    "NET110": "Not provided in assignment",
    "COM241": "Not provided in assignment",
}


# STEP 2: DEFINE A FUNCTION TO LOOK UP COURSE INFORMATION.
#
# This user-defined function receives a course number from
# the main() function.
#
# It retrieves the corresponding information from all
# three dictionaries.
#
# A try/except block handles invalid course numbers.

def display_course_information(course_number):
    """
    Retrieve and display course information.

    If the course number does not exist, display a friendly
    error message instead of allowing the program to crash.
    """

    # The try block attempts to retrieve information.
    # Square brackets access dictionary values by key.
    #
    # If the key is missing, Python raises a KeyError.

    try:
        room = course_rooms[course_number]
        instructor = course_instructors[course_number]
        meeting_time = course_times[course_number]

    # Handle a missing course number.
    # The program displays an error without a traceback.

    except KeyError:
        print(
            f"Course {course_number} was not found. "
            "Please check the course number."
        )

    # The else block executes only when all three
    # dictionary lookups are successful.

    else:
        print(f"Course Number: {course_number}")
        print(f"Room Number: {room}")
        print(f"Instructor: {instructor}")
        print(f"Meeting Time: {meeting_time}")


# STEP 3: DEFINE THE MAIN FUNCTION.
#
# This function displays the program heading and prompts
# the user to enter a course number.
#
# A while loop allows multiple course lookups.
#
# The loop continues until the user enters Q to quit.

def main():
    """
    Allow repeated course lookups until the user enters Q.
    """

    # Display the heading once when the program starts.

    print("COURSE INFORMATION SYSTEM")

    # Continue asking for course numbers until the
    # user chooses to exit.

    while True:

        # Ask the user to enter a course number.
        #
        # strip() removes leading and trailing spaces.
        # upper() converts lowercase letters to uppercase.
        #
        # For example, csc101 becomes CSC101.

        course_number = input(
            "\nEnter a course number (or Q to quit): "
        ).strip().upper()

        # Check whether the user wants to quit.
        #
        # The break statement exits the while loop.

        if course_number == "Q":
            print(
                "Thank you for using the "
                "Course Information System."
            )
            break

        # Call the user-defined function.
        #
        # The function retrieves and displays the
        # information for the entered course.
        #
        # If the course is invalid, the error message
        # appears and the loop continues.

        display_course_information(course_number)


# STEP 4: START THE PROGRAM.
#
# This condition runs main() when the Python file is
# executed directly.
#
# It prevents main() from running automatically if
# another Python program imports this file.

if __name__ == "__main__":
    main()