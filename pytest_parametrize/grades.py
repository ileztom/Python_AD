import csv
import pytest

def read_grades_from_csv(file_path):
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.reader(file)
        next(reader)
        grades = []
        for row in reader:
            grades.append({
                'Last name': row[0].strip(),
                'First name': row[1].strip(),
                'SSN': row[2].strip(),
                'Test1': float(row[3].strip()),
                'Test2': float(row[4].strip()),
                'Test3': float(row[5].strip()),
                'Test4': float(row[6].strip()),
                'Final': float(row[7].strip()),
                'Grade': row[8].strip()
            })
    return grades

def calculate_average(student):
    tests = [student['Test1'], student['Test2'], student['Test3'], student['Test4']]
    average = sum(tests) / len(tests)
    return round(average, 1)

@pytest.fixture(scope="module")
def grades_data():
    return read_grades_from_csv('grades.csv')


@pytest.mark.parametrize("student", read_grades_from_csv('grades.csv'))
def test_student_grade(student):
    average_tests = calculate_average(student)
    final_grade = student['Final']

    assert average_tests == final_grade, f"Error in grading for {student['First name']} {student['Last name']} (SSN: {student['SSN']}) tests: {final_grade}, Actual average: {average_tests}"
