def vowel_filter(func):
    def wrapper():
        letters = func()
        return [letter for letter in letters if letter.lower() in "aouie"]

    return wrapper


@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
