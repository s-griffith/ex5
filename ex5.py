import json
import os
import glob


def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the student's database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    student_names = []
    # Open the file as a JSON file and receive the data in its proper data structure:
    with open(input_json_path) as json_file:
        data = json.load(json_file)
        # Run on all the students in the database, and add their name to a list if they are registered in the course:
        for index in data:
            current_name = [data[index]['student_name'] for elem in data[index]['registered_courses']
                            if course_name == elem]
            if current_name != []:
                student_names.append(current_name[0])
    return student_names


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the student's database json file.
    :param output_file_path: Path of the output text file.
    """
    courses_list = set()
    num_enrolled = {}
    # Open the file as a JSON file and receive the data in its proper data structure:
    with open(input_json_path) as json_file:
        data = json.load(json_file)
        # Go through each student in the database and create a set of courses:
        for index in data:
            courses = data[index]['registered_courses']
            courses_list.update(courses)
    # Use the previous function to get a list of students registered for each course:
    for elem in courses_list:
        students = names_of_registered_students(input_json_path, elem)
        num_enrolled[elem] = len(students)
    # Sort the list in alphabetical order and print it accordingly:
    ordered_list = list(num_enrolled.keys())
    ordered_list.sort()
    with open(output_file_path, 'w') as file:
        for item in ordered_list:
            file.writelines(['"', item, '"', " ", str(num_enrolled[item]), "\n"])
    pass


def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semesters_data files.
    :param output_json_path: Path of the output json file.
    """
    lecturers_dict = {}
    # Go through json files in folder
    for filename in glob.glob(os.path.join(json_directory_path, '*.json')):
        with open(filename) as currentFile:
            data = json.load(currentFile)
            # Go through the courses in each file, and to the relevant lecturers in the dictionary
            for course in data:
                for lecturer in data[course]["lecturers"]:
                    if lecturer not in lecturers_dict:
                        lecturers_dict[lecturer] = [data[course]["course_name"]]
                    elif data[course]["course_name"] not in lecturers_dict[lecturer]:
                        lecturers_dict[lecturer].append(data[course]["course_name"])
    # Write dictionary to output file
    with open(output_json_path, 'w') as outfile:
        json.dump(lecturers_dict, outfile, indent=4)
    pass
