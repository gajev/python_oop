import unittest
from project.vehicle import Vehicle


class TestVehicle(unittest.TestCase):
    def setUp(self):
        self.vehicle = Vehicle(50, 200)

    def test_init_creates_all_attributes(self):
        self.assertEqual(self.vehicle.fuel, 50)
        self.assertEqual(self.vehicle.horse_power, 200)
        self.assertEqual(self.vehicle.capacity, 50)
        self.assertEqual(self.vehicle.fuel_consumption, 1.25)

    def test_change_consumption(self):
        self.vehicle.fuel_consumption = 3
        self.assertEqual(3, self.vehicle.fuel_consumption)

    def test_drive_if_fuel_is_not_enough(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive(self):
        self.vehicle.drive(10)
        self.assertEqual(37.5, self.vehicle.fuel)

    def test_refuel_if_capacity_is_exceeded(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel(self):
        self.vehicle.fuel = 20
        self.vehicle.refuel(10)
        self.assertEqual(30, self.vehicle.fuel)

    def test_repr(self):
        result = self.vehicle.__str__()
        self.assertEqual(result, "The vehicle has 200 horse power with 50 fuel left and 1.25 fuel consumption")


if __name__ == "__main__":
    unittest.main()