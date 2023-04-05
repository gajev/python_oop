class Cat:
    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')
        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')
        self.sleepy = False


import unittest


class CatTest(unittest.TestCase):
    def setUp(self):
        self.cat = Cat("Angel")

    def test_cat_is_initialized_correctly(self):
        self.assertEqual(self.cat.name, "Angel")

    def test_cat_cannot_eat_if_fed(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual("Already fed.", str(ex.exception))

    def test_cat_is_fed_after_eating(self):
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)
        self.assertEqual(self.cat.size, 1)

    def test_cat_cannot_fall_asleep_if_not_fed(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual("Cannot sleep while hungry", str(ex.exception))

    def test_cat_is_not_sleepy_after_sleeping(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(self.cat.sleepy, False)


if __name__ == "__main__":
    unittest.main()




