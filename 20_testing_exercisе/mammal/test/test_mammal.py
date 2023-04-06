import unittest
from project.mammal import Mammal

class TestCarManager(unittest.TestCase):
    def setUp(self):
        self.mammal = Mammal("Tom", "cat", "meow")

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.mammal.name, "Tom")
        self.assertEqual(self.mammal.type, "cat")
        self.assertEqual(self.mammal.sound, "meow")

    def test_make_sound(self):
        result = self.mammal.make_sound()
        self.assertEqual("Tom makes meow", result)

    def test_get_kingdom(self):
        result = self.mammal.get_kingdom()
        self.assertEqual(result, "animals")

    def test_info(self):
        result = self.mammal.info()
        self.assertEqual(result, "Tom is of type cat")


if __name__ == "__main__":
    unittest.main()
