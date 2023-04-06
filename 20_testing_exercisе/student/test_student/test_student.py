import unittest
from project.student import Student


class TestStudent(unittest.TestCase):
    def setUp(self):
        self.student = Student("Angel")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.student.name, "Angel")
        self.assertEqual(self.student.courses, {})

    def test_init_creates_courses(self):
        self.assertEqual(self.student.name, "Angel")
        self.student = Student("Angel", {"Basics": ["notes", "more_notes"]})
        self.assertEqual(self.student.courses, {"Basics": ["notes", "more_notes"]})

    def test_add_notes(self):
        self.student = Student("Angel", {"Basics": ["notes", "more_notes"]})
        result = self.student.enroll("Basics", ["another_notes", "and_another_notes"])
        self.assertEqual("Course already added. Notes have been updated.", result)

    def test_add_course_and_add_course_notes_Y(self):
        self.student = Student("Angel", {"Basics": ["notes", "more_notes"]})
        result = self.student.enroll("Advanced", ["another_notes", "and_another_notes"], "Y")
        self.assertEqual(self.student.courses["Advanced"], ["another_notes", "and_another_notes"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_course_and_add_course_notes_empty_string(self):
        self.student = Student("Angel", {"Basics": ["notes", "more_notes"]})
        result = self.student.enroll("Advanced", ["another_notes", "and_another_notes"], "")
        self.assertEqual(self.student.courses["Advanced"], ["another_notes", "and_another_notes"])
        self.assertEqual("Course and course notes have been added.", result)

    def test_add_course_without_notes(self):
        self.student = Student("Angel", {"Basics": ["notes", "more_notes"]})
        result = self.student.enroll("Advanced", ["another_notes", "and_another_notes"], "N")
        self.assertEqual(self.student.courses["Advanced"], [])
        self.assertEqual("Course has been added.", result)

    def test_add_notes_error_if_course_not_found(self):
        self.student = Student("Angel", {"Basics": ["notes", "more_notes"]})
        with self.assertRaises(Exception) as ex:
            self.student.add_notes("Advanced", ["some_note"])
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_add_notes_method(self):
        self.student = Student("Angel", {"Basics": ["notes", "more_notes"]})
        result = self.student.add_notes("Basics", "some_note")
        self.assertEqual(["notes", "more_notes", "some_note"], self.student.courses["Basics"])
        self.assertEqual("Notes have been updated", result)

    def test_leave_course_error_if_course_not_found(self):
        self.student = Student("Angel", {"Basics": ["notes", "more_notes"]})
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("Advanced")
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))

    def test_leave_course(self):
        self.student = Student("Angel", {"Basics": ["notes", "more_notes"]})
        result = self.student.leave_course("Basics")
        self.assertEqual(self.student.courses, {})
        self.assertEqual(result, "Course has been removed")


if __name__ == "__main__":
    unittest.main()
