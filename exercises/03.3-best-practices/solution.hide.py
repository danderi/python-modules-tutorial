# The solution shows the complete working code structure:

# models.py
from dataclasses import dataclass
from typing import List

@dataclass
class Student:
    id: int
    name: str
    courses: List[str]

    def __post_init__(self):
        if self.courses is None:
            self.courses = []

@dataclass
class Course:
    code: str
    name: str
    students: List[int]

    def __post_init__(self):
        if self.students is None:
            self.students = []

# utils.py
def validate_student_id(student_id: int) -> bool:
    return isinstance(student_id, int) and student_id > 0

def validate_course_code(course_code: str) -> bool:
    return isinstance(course_code, str) and len(course_code) == 5

def format_enrollment(student: Student, course: Course) -> str:
    return f"Student: {student.name} (ID: {student.id}) enrolled in Course: {course.name} (Code: {course.code})"

# students.py
def create_student(student_id: int, name: str) -> Student:
    if validate_student_id(student_id):
        return Student(id=student_id, name=name, courses=[])
    raise ValueError("Invalid student ID")

def enroll_student(student: Student, course: Course) -> str:
    if course.code not in student.courses:
        student.courses.append(course.code)
        course.students.append(student.id)
        return format_enrollment(student, course)
    return "Student already enrolled"

# courses.py
def create_course(code: str, name: str) -> Course:
    if validate_course_code(code):
        return Course(code=code, name=name, students=[])
    raise ValueError("Invalid course code")

def get_course_students(course: Course) -> list:
    return course.students.copy()