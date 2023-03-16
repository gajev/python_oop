class Category:
    def __init__(self, identity, name):
        self.id = identity
        self.name = name

    def edit(self, new_name):
        self.name = new_name

    def __repr__(self):
        return f"Category {self.id}: {self.name}"
    