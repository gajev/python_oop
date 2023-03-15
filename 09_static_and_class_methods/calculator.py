from functools import reduce

class Calculator:

    @staticmethod
    def add(*numbers):
        return sum(numbers)

    def multiply(*numbers):
        return reduce(lambda a, b: a * b, numbers)

    def divide(*numbers):
        return reduce(lambda a, b: a / b, numbers)

    def subtract(*numbers):
        return reduce(lambda a, b: a - b, numbers)


print(Calculator.add(5, 10, 4))
print(Calculator.multiply(1, 2, 3, 5))
print(Calculator.divide(100, 2))
print(Calculator.subtract(90, 20, -50, 43, 7))
