class reverse_iter:
    def __init__(self, iterable_object):
        self.iterable_object = iterable_object
        self.start = len(self.iterable_object) - 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < 0:
            raise StopIteration
        index = self.start
        self.start -= 1
        return self.iterable_object[index]


reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)