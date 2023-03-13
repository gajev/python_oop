class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        if self.__animal_capacity == len(self.animals):
            return "Not enough space for animal"
        if self.__budget < price:
            return "Not enough budget"

        self.animals.append(animal)
        self.__budget -= price

        return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

    def hire_worker(self, worker):
        if self.__workers_capacity == len(self.workers):
            return "Not enough space for worker"
        self.workers.append(worker)
        return f"{worker.name} the {worker.__class__.__name__} hired successfully"

    def fire_worker(self, worker_name):
        for current_worker in self.workers:
            if current_worker.name == worker_name:
                self.workers.remove(current_worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salaries = 0
        for current_worker in self.workers:
            salaries += current_worker.salary
        if salaries > self.__budget:
            return "You have no budget to pay your workers. They are unhappy"
        self.__budget -= salaries
        return f"You payed your workers. They are happy. Budget left: {self.__budget}"

    def tend_animals(self):
        tend_money = 0
        for current_animal in self.animals:
            tend_money += current_animal.money_for_care
        if tend_money > self.__budget:
            return "You have no budget to tend the animals. They are unhappy."
        self.__budget -= tend_money
        return f"You tended all the animals. They are happy. Budget left: {self.__budget}"

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        result = f"You have {len(self.animals)} animals\n"
        animals_dict = {"Lion": [], "Tiger": [], "Cheetah": []}
        for current_animal in self.animals:
            animals_dict[current_animal.__class__.__name__].append(current_animal)
        result += f"----- {len(animals_dict['Lion'])} Lions:\n"
        result += '\n'.join(str(x) for x in animals_dict["Lion"])
        result += f"\n----- {len(animals_dict['Tiger'])} Tigers:\n"
        result += '\n'.join(str(x) for x in animals_dict["Tiger"])
        result += f"\n----- {len(animals_dict['Cheetah'])} Cheetahs:\n"
        result += '\n'.join(str(x) for x in animals_dict["Cheetah"])
        return result

    def workers_status(self):
        result = f"You have {len(self.workers)} workers\n"
        workers_dict = {"Keeper": [], "Caretaker": [], "Vet": []}
        for current_worker in self.workers:
            workers_dict[current_worker.__class__.__name__].append(current_worker)
        result += f"----- {len(workers_dict['Keeper'])} Keepers:\n"
        result += '\n'.join(str(x) for x in workers_dict["Keeper"])
        result += f"\n----- {len(workers_dict['Caretaker'])} Caretakers:\n"
        result += '\n'.join(str(x) for x in workers_dict["Caretaker"])
        result += f"\n----- {len(workers_dict['Vet'])} Vets:\n"
        result += '\n'.join(str(x) for x in workers_dict["Vet"])
        return result











