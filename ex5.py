import json
import os



def names_of_registered_students(input_json_path, course_name):
    """
    This function returns a list of the names of the students who registered for
    the course with the name "course_name".

    :param input_json_path: Path of the students database json file.
    :param course_name: The name of the course.
    :return: List of the names of the students.
    """
    student_names = []
    try:
        with open(input_json_path) as json_file:
            data = json.load(json_file)
            for index in data.keys():
                current_name = [data[index]['student_name'] for elem in data[index]['registered_courses'] if course_name == elem]
                if  current_name != []:
                    student_names.append(current_name[0])
    except IOError:
        print("Could not open file.\n") #temporary until figure out what needs to happen
        raise
    except FileNotFoundError:
        print("File not found.\n")
        raise
    return student_names


def enrollment_numbers(input_json_path, output_file_path):
    """
    This function writes all the course names and the number of enrolled
    student in ascending order to the output file in the given path.

    :param input_json_path: Path of the students database json file.
    :param output_file_path: Path of the output text file.
    """
    pass



def courses_for_lecturers(json_directory_path, output_json_path):
    """
    This function writes the courses given by each lecturer in json format.

    :param json_directory_path: Path of the semsters_data files.
    :param output_json_path: Path of the output json file.
    """
    pass



