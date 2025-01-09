# Student-related operations
from .models import Student, Course
from .utils import validate_student_id, format_enrollment

def create_student(student_id: int, name: str) -> Student:
    """Create a new student"""
    if validate_student_id(student_id):
        return Student(id=student_id, name=name, courses=[])
    raise ValueError("Invalid student ID")

def enroll_student(student: Student, course: Course) -> str:
    """Enroll a student in a course"""
    if course.code not in student.courses:
        student.courses.append(course.code)
        course.students.append(student.id)
        return format_enrollment(student, course)
    return "Student already enrolled"

# Test the functionality
if __name__ == "__main__":
    from .courses import create_course

    student = create_student(1, "Alice")
    course = create_course("PY101", "Python 101")
    print(enroll_student(student, course))