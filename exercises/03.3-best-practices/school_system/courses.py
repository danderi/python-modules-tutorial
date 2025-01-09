from typing import List
from .models import Course, Student
from .utils import validate_course_code

def create_course(code: str, name: str) -> Course:
    """Create a new course"""
    if validate_course_code(code):
        return Course(code=code, name=name, students=[])
    raise ValueError("Invalid course code")

def get_course_students(course: Course) -> List[int]:
    """Get list of students enrolled in a course"""
    return course.students.copy()

def has_student(course: Course, student_id: int) -> bool:
    """Check if a student is enrolled in this course"""
    return student_id in course.students
