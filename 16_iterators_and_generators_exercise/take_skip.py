class take_skip:
    def __init__(self, step, count):
        self.step = step
        self.count = count
        self.start = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.count == 0:
            raise StopIteration
        self.count -= 1
        self.start += 1
        return self.start * self.step
