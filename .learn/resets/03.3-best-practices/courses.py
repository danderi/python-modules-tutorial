# Course-related operations
from .models import Course
from .utils import validate_course_code

def create_course(code: str, name: str) -> Course:
    """Create a new course"""
    if validate_course_code(code):
        return Course(code=code, name=name, students=[])
    raise ValueError("Invalid course code")

def get_course_students(course: Course) -> list:
    """Get list of student IDs enrolled in a course"""
    return course.students.copy()

# Test the functionality
if __name__ == "__main__":
    course = create_course("PY101", "Python 101")
    print(f"Created course: {course.name} ({course.code})")