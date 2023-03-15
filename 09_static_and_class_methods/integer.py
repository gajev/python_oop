class Integer:
    def __init__(self, value):
        self.value = value

    @classmethod
    def from_float(cls, float_value):
        if not isinstance(float_value, float):
            return "value is not a float"
        return cls(float_value // 1)

    @classmethod
    def from_roman(cls, value):
        roman_dict = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        integer_value = 0

        for i in range(len(value)):
            if i != 0 and roman_dict[value[i]] > roman_dict[value[i - 1]]:
                integer_value += roman_dict[value[i]] - 2 * roman_dict[value[i - 1]]
            else:
                integer_value += roman_dict[value[i]]
        return cls(integer_value)

    @classmethod
    def from_string(cls, value):
        if not isinstance(value, str):
            return "wrong type"
        return cls(int(value))

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string("26"))

