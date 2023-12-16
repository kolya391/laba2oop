class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

person = Person("Коля", 17, "мужской")
print(person.name)
print(person.age)
print(person.gender)
