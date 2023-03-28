class vowels:
    def __init__(self, some_string):
        self.some_string = some_string
        self.index = 0
        self.all_vowels = ["a", "e", "i" , "u", "y", "o", "A", "E", "I", "U", "Y", "O"]
        self.vowels_list = [x for x in self.some_string if x in self.all_vowels]

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == len(self.vowels_list):
            raise StopIteration
        vowel = self.vowels_list[self.index]
        self.index += 1
        return vowel


my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)