import unittest
from models import Student, Course
from utils import validate_student_id, validate_course_code, format_enrollment
from students import create_student, enroll_student
from courses import create_course, get_course_students

class TestBestPractices(unittest.TestCase):
    def test_validate_student_id(self):
        self.assertTrue(validate_student_id(1))
        self.assertFalse(validate_student_id(-1))
        self.assertFalse(validate_student_id("1"))

    def test_validate_course_code(self):
        self.assertTrue(validate_course_code("PY101"))
        self.assertFalse(validate_course_code("PY10"))
        self.assertFalse(validate_course_code(101))

    def test_create_student(self):
        student = create_student(1, "Alice")
        self.assertEqual(student.id, 1)
        self.assertEqual(student.name, "Alice")
        self.assertEqual(student.courses, [])

        with self.assertRaises(ValueError):
            create_student(-1, "Bob")

    def test_create_course(self):
        course = create_course("PY101", "Python 101")
        self.assertEqual(course.code, "PY101")
        self.assertEqual(course.name, "Python 101")
        self.assertEqual(course.students, [])

        with self.assertRaises(ValueError):
            create_course("PY10", "Python 101")

    def test_enroll_student(self):
        student = create_student(1, "Alice")
        course = create_course("PY101", "Python 101")
        enrollment_message = enroll_student(student, course)
        self.assertEqual(enrollment_message, "Student: Alice (ID: 1) enrolled in Course: Python 101 (Code: PY101)")
        self.assertIn("PY101", student.courses)
        self.assertIn(1, course.students)

        # Test enrolling the same student again
        enrollment_message = enroll_student(student, course)
        self.assertEqual(enrollment_message, "Student already enrolled")

    def test_get_course_students(self):
        course = create_course("PY101", "Python 101")
        student1 = create_student(1, "Alice")
        student2 = create_student(2, "Bob")
        enroll_student(student1, course)
        enroll_student(student2, course)
        self.assertEqual(get_course_students(course), [1, 2])

if __name__ == '__main__':
    unittest.main()