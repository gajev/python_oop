from wild_farm.animals.animal import Animal, Mammal


class Mouse(Mammal):
    def make_sound(self):
        return "Squeak"

    def feed(self, food):
        if food.__class__.__name__ not in Animal.dictionary[self.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity


class Dog(Mammal):
    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ not in Animal.dictionary[self.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity


class Cat(Mammal):
    def make_sound(self):
        return "Meow"

    def feed(self, food):
        if food.__class__.__name__ not in Animal.dictionary[self.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity


class Tiger(Mammal):
    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ not in Animal.dictionary[self.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += food.quantity
        self.food_eaten += food.quantity


