def view_courses(courses_data: list[dict[str, str]]) -> None:
    """
    Displays a list of available courses with details such as course name, duration, 
    and instructor.

    Args:
        courses_data (list): A list of dictionaries containing course details. 
                              Each dictionary has keys like 'course_name', 'instructor', and 'duration'.
    """
    pass


    if not courses_data:
        print("No courses available at the moment.")
    else:
        print("\nAvailable Courses:")
        for index, course in enumerate(courses_data, start=1):
            print(f"{index}. {course['course_name']} - Instructor: {course['instructor']}, Duration: {course['duration']}, Price: ${course['price']}")