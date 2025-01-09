def validate_student_id(student_id: int) -> bool:
    """Validate student ID format"""
    return isinstance(student_id, int) and student_id > 0

def validate_course_code(course_code: str) -> bool:
    """Validate course code format"""
    return isinstance(course_code, str) and len(course_code) == 5

def format_enrollment(student_name: str, student_id: int, course_name: str, course_code: str) -> str:
    """Format enrollment message"""
    return f"Student: {student_name} (ID: {student_id}) enrolled in Course: {course_name} (Code: {course_code})"
