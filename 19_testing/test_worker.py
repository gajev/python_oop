class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception("Not enough energy.")

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f"{self.name} has saved {self.money} money."


import unittest


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.worker = Worker("Angel", 5000, 10)

    def test_worker_is_initialized_correctly(self):
        self.assertEqual(self.worker.name, "Angel")
        self.assertEqual(self.worker.salary, 5000)
        self.assertEqual(self.worker.energy, 10)
        self.assertEqual(self.worker.money, 0)

    def test_energy_is_increased_after_rest(self):
        self.worker.rest()
        self.assertEqual(self.worker.energy, 11)

    def test_if_error_message_is_raised_with_negative_energy(self):
        worker = Worker("Angel", 5000, 0)
        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual("Not enough energy.", str(ex.exception))

    def test_salary_is_increased_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.money, 5000)

    def test_energy_is_decreased_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.energy, 9)

    def test_if_get_info_returns_proper_string(self):
        self.worker.work()
        result = self.worker.get_info()
        self.assertEqual(result, "Angel has saved 5000 money.")


if __name__ == "__main__":
    unittest.main()




