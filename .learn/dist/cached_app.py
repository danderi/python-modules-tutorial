# Main entry point for the school system
from school_system.models import Student, Course
from school_system.students import create_student, enroll_student
from school_system.courses import create_course

def main():
    # Create a student and a course
    student = create_student(1, "Alice")
    course = create_course("PY101", "Python 101")
    
    # Enroll the student in the course
    result = enroll_student(student, course)
    print(result)

if __name__ == "__main__":
    main()
