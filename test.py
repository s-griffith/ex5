from ex5 import names_of_registered_students, enrollment_numbers, courses_for_lecturers
import json
import unittest

input_json_path = "students_database.json"
database_directory_path = "semesters_databases"

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Test(unittest.TestCase):


    def test1(self):
        """
        this test for the first function - names_of_registered_students.

        """

        correct_answer = ["Mohamed Gramne", "Mhameed", "Efrat Levkovizh", "Yazeed Falah"]

        result = names_of_registered_students(input_json_path,"Introduction to Systems Programming")

        correct_answer.sort()
        result.sort()

        self.assertListEqual(correct_answer, result, "Error: the output of the function   \
                                                  names_of_registered_students        \
                                                  doesn't match the expected one.")
        print(bcolors.OKGREEN + "Test 1 Passed" + bcolors.ENDC)
    
    def test1a(self):
        """
        this test for the first function - names_of_registered_students.

        """

        correct_answer = ["Mohamed Gramne", "Mhameed", "Yazeed Falah"]

        result = names_of_registered_students(input_json_path,"Data Structures 1")

        correct_answer.sort()
        result.sort()

        self.assertListEqual(correct_answer, result, "Error: the output of the function   \
                                                  names_of_registered_students        \
                                                  doesn't match the expected one.")
        print(bcolors.OKGREEN + "Test 1a Passed" + bcolors.ENDC)

    def test1b(self):
        """
        this test for the first function - names_of_registered_students.

        """

        correct_answer = ["Mohamed Gramne", "Zoabi", "Yazeed Falah"]

        result = names_of_registered_students(input_json_path,"Introduction to Algorithms")

        correct_answer.sort()
        result.sort()

        self.assertListEqual(correct_answer, result, "Error: the output of the function   \
                                                  names_of_registered_students        \
                                                  doesn't match the expected one.")
        print(bcolors.OKGREEN + "Test 1b Passed" + bcolors.ENDC)

    def test1c(self):
        """
        this test for the first function - names_of_registered_students.

        """

        correct_answer = []

        result = names_of_registered_students(input_json_path,"Introduction to Computer Science")

        correct_answer.sort()
        result.sort()

        self.assertListEqual(correct_answer, result, "Error: the output of the function   \
                                                  names_of_registered_students        \
                                                  doesn't match the expected one.")
        print(bcolors.OKGREEN + "Test 1c Passed" + bcolors.ENDC)

    def test2(self):
        """
        this test for the second function - enrollment_number.
        """

        expected_output_file = "expected_output_test2_enrollment_numbers.txt"
        enrollment_numbers(input_json_path,"test2.out")
        with open("test2.out") as file_to_test:
            data_to_test = list(file_to_test)

        with open(expected_output_file) as expected_file:
            expected_data = list(expected_file)

        self.assertListEqual(data_to_test,expected_data, "Error: the content of the file created by   \
                                              the fucntion - enrollment_number     \
                                              doesn't match the expected one.")
        print(bcolors.OKGREEN + "Test 2 Passed" + bcolors.ENDC)

		
    def test3(self):
        
        """
        this test for the third function - courses_for_lecturers.
        """
        expected_output_file = "expected_output_test3_courses_for_lecturers.json"
        courses_for_lecturers(database_directory_path,"test3_output.json")

        with open("test3_output.json") as file_to_test:
            data_to_test = json.load(file_to_test)

        with open(expected_output_file) as expected_file:
            expected_data = json.load(expected_file)

        for h in data_to_test:
            data_to_test[h].sort()

        for h in expected_data:
            expected_data[h].sort()

        self.assertDictEqual(data_to_test ,expected_data, "Error: the content of the file created by   \
                                                           the fucntion - courses_for_lecturers        \
                                                           doesn't match the expected one.")
        print(bcolors.OKGREEN + "Test 3 Passed" + bcolors.ENDC)

if __name__ == '__main__':
    unittest.main()












