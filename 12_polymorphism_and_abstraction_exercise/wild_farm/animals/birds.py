from wild_farm.animals.animal import Animal, Bird


class Owl(Bird):
    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ not in Animal.dictionary[self.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        if food.__class__.__name__ not in Animal.dictionary[self.__class__.__name__]:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity


