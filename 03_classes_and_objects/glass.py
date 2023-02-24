class Glass:
    capacity = 250

    def __init__(self, content=0):
        self.content = content

    def fill(self, ml):
        if ml > self.capacity:
            return f"Cannot add {ml} ml"
        else:
            self.capacity -= ml
            self.content += ml
            return f"Glass filled with {ml} ml"

    def empty(self):
        self.capacity = 250
        self.content = 0
        return "Glass is now empty"

    def info(self):
        return f"{self.capacity} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())


