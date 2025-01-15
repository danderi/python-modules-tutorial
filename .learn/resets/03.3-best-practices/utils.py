# Shared utilities used across modules
from typing import Optional
from .models import Student, Course

def validate_student_id(student_id: int) -> bool:
    """Check if a student ID is valid"""
    return isinstance(student_id, int) and student_id > 0

def validate_course_code(course_code: str) -> bool:
    """Check if a course code is valid"""
    return isinstance(course_code, str) and len(course_code) == 5

def format_enrollment(student: Student, course: Course) -> str:
    """Format enrollment information"""
    return f"Student: {student.name} (ID: {student.id}) enrolled in Course: {course.name} (Code: {course.code})"
