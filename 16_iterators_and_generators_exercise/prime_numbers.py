import math


def get_primes(numbers):
    for number in numbers:
        if number <= 1:
            continue

        for num in range(2, int(math.sqrt(number)) + 1):
            if number % num == 0:
                break
        else:
            yield number
