"""Name: Dustin Barnes
Course: 2420-001
Project 3 Linked Lists
File: main.py

All of the following code was written by me.

The main module opens data from a text file, puts it into a linked list,
then displays the course and gpa information for that list."""

from course import Course
from courselist import CourseList

def main():
    """Main function. Opens text file, processes the data and inputs the data
    into a linked list using the course and coureslist modules. It then
    outputs the course information and cumulative gpa."""
    raw_file = open("data.txt", "r")
    raw_file_data = raw_file.read()
    raw_file_data_list = raw_file_data.split('\n')
    course_list = CourseList()
    for course in raw_file_data_list:
        temp_list = course.split(',')
        course = Course(int(temp_list[0]), temp_list[1], float(temp_list[2]), float(temp_list[3]))
        course_list.insert(course)
    print("Current List: (" + str(course_list.size()) + ")\n" + str(course_list) + "\n\n\nCumulative GPA: " + str(f'{course_list.calculate_gpa():.3f}')) #pylint: disable= C0301

if __name__ == "__main__":
    main()
