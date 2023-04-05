class Car:
    def __init__(self, make, model, fuel_consumption, fuel_capacity):
        self.make = make
        self.model = model
        self.fuel_consumption = fuel_consumption
        self.fuel_capacity = fuel_capacity
        self.fuel_amount = 0

    @property
    def make(self):
        return self.__make

    @make.setter
    def make(self, new_value):
        if not new_value:
            raise Exception("Make cannot be null or empty!")
        self.__make = new_value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, new_value):
        if not new_value:
            raise Exception("Model cannot be null or empty!")
        self.__model = new_value

    @property
    def fuel_consumption(self):
        return self.__fuel_consumption

    @fuel_consumption.setter
    def fuel_consumption(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel consumption cannot be zero or negative!")
        self.__fuel_consumption = new_value

    @property
    def fuel_capacity(self):
        return self.__fuel_capacity

    @fuel_capacity.setter
    def fuel_capacity(self, new_value):
        if new_value <= 0:
            raise Exception("Fuel capacity cannot be zero or negative!")
        self.__fuel_capacity = new_value

    @property
    def fuel_amount(self):
        return self.__fuel_amount

    @fuel_amount.setter
    def fuel_amount(self, new_value):
        if new_value < 0:
            raise Exception("Fuel amount cannot be negative!")
        self.__fuel_amount = new_value

    def refuel(self, fuel):
        if fuel <= 0:
            raise Exception("Fuel amount cannot be zero or negative!")
        self.__fuel_amount += fuel
        if self.__fuel_amount > self.__fuel_capacity:
            self.__fuel_amount = self.__fuel_capacity

    def drive(self, distance):
        needed = (distance / 100) * self.__fuel_consumption

        if needed > self.__fuel_amount:
            raise Exception("You don't have enough fuel to drive!")

        self.__fuel_amount -= needed

import unittest


class TestCarManager(unittest.TestCase):
    def setUp(self):
        self.car = Car("BMW", "e60", 5.6, 100)

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.car.make, "BMW")
        self.assertEqual(self.car.model, "e60")
        self.assertEqual(self.car.fuel_consumption, 5.6)
        self.assertEqual(self.car.fuel_capacity, 100)
        self.assertEqual(self.car.fuel_amount, 0)

    def test_negative_fuel_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = -2
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_set_fuel(self):
        self.car.fuel_capacity = 10
        self.assertEqual(10, self.car.fuel_capacity)

    def test_empty_model_name(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_set_model(self):
        self.car.model = "Mercedes"
        self.assertEqual("Mercedes", self.car.model)

    def test_empty_make_name(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_set_make(self):
        self.car.make = "benz"
        self.assertEqual("benz", self.car.make)

    def test_negative_fuel_consumption(self):
        with self.assertRaises(Exception) as ex:
            self.car.consumption = -2
        self.assertEqual("Consumption cannot be zero or negative!", str(ex.exception))

    def test_set_consumption(self):
        self.car.fuel_consumption = 10
        self.assertEqual(10, self.car.fuel_consumption)

    def test_refuel(self):
        self.assertEqual(0, self.car.fuel_amount)
        self.car.refuel(10)
        self.assertEqual(10, self.car.fuel_amount)

    def test_refuel_with_negative(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-10)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_drive_without_fuel(self):
        self.assertEqual(0, self.car.fuel_amount)
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive(self):
        self.car.refuel(100)
        self.assertEqual(100, self.car.fuel_amount)
        self.car.drive(10)
        self.assertEqual(99.44, self.car.fuel_amount)

    def test_drive_with_not_enough_fuel(self):
        self.car.refuel(0.1)
        with self.assertRaises(Exception) as ex:
            self.car.drive(10)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))


if __name__ == "__main__":
    unittest.main()

