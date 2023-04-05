class IntegerList:
    def __init__(self, *args):
        self._IntegerList__data = None
        self.__data = []
        for x in args:
            if type(x) == int:
                self.__data.append(x)

    def get_data(self):
        return self.__data

    def add(self, element):
        if not type(element) == int:
            raise ValueError("Element is not Integer")
        self.get_data().append(element)
        return self.get_data()

    def remove_index(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        a = self.get_data()[index]
        del self.get_data()[index]
        return a

    def get(self, index):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        return self.get_data()[index]

    def insert(self, index, el):
        if index >= len(self.get_data()):
            raise IndexError("Index is out of range")
        elif not type(el) == int:
            raise ValueError("Element is not Integer")

        self.get_data().insert(index, el)

    def get_biggest(self):
        a = sorted(self.get_data(), reverse=True)
        return a[0]

    def get_index(self, el):
        return self.get_data().index(el)


import unittest


class TestIntegerList(unittest.TestCase):
    def setUp(self):
        self.list_test = IntegerList(1, 2, 3, 4)

    def test_init_creates_all_attributes(self):
        self.assertEqual([1, 2, 3, 4], self.list_test._IntegerList__data)

    def test_init_takes_not_integers(self):
        self.list_test = IntegerList(1, 2, 3.4, "4")
        self.assertEqual([1, 2], self.list_test._IntegerList__data)

    def test_add_operation_error_in_case_element_not_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.list_test.add("3")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_add_integer_to_the_list(self):
        result = self.list_test.add(5)
        self.assertEqual([1, 2, 3, 4, 5], result)

    def test_error_to_remove_index_if_it_is_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list_test.remove_index(15)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_remove_element(self):
        self.list_test.remove_index(0)
        self.assertEqual([2, 3, 4], self.list_test._IntegerList__data)

    def test_get_method_if_index_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list_test.get(15)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_get_method(self):
        self.list_test.get(1)
        self.assertEqual(2, self.list_test._IntegerList__data[1])

    def test_insert_method_out_of_range(self):
        with self.assertRaises(IndexError) as ex:
            self.list_test.insert(10, 2)
        self.assertEqual("Index is out of range", str(ex.exception))

    def test_insert_method_not_integer(self):
        with self.assertRaises(ValueError) as ex:
            self.list_test.insert(1, "2")
        self.assertEqual("Element is not Integer", str(ex.exception))

    def test_insert_method(self):
        self.list_test.insert(0, 12)
        self.assertEqual([12, 1, 2, 3, 4], self.list_test._IntegerList__data)

    def test_get_biggest(self):
        self.assertEqual(4, self.list_test.get_biggest())

    def test_get_index(self):
        index = self.list_test.get_index(2)
        self.assertEqual(1, index)


if __name__ == "__main__":
    unittest.main()
