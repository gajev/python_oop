class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, second_person):
        return Person(self.name, second_person.surname)


class Group:
    def __init__(self, name, people):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __add__(self, group_2):
        name = f"{self.name} {group_2.name}"
        people = []
        for current_person in self.people:
            people.append(current_person)
        for current_person in group_2.people:
            people.append(current_person)
        return Group(name, people)

    def __repr__(self):
        return f"Group {self.name} with members {', '.join(x.name + ' ' + x.surname for x in self.people)}"

    def __getitem__(self, index):
        return f"Person {index}: {repr(self.people[index])}"


p0 = Person('Aliko', 'Dangote')
p1 = Person('Bill', 'Gates')
p2 = Person('Warren', 'Buffet')
p3 = Person('Elon', 'Musk')
p4 = p2 + p3

first_group = Group('__VIP__', [p0, p1, p2])
second_group = Group('Special', [p3, p4])
third_group = first_group + second_group

print(len(first_group))
print(second_group)
print(third_group[0])

for person in third_group:
    print(person)

