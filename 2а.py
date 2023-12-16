class Person:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    def print_info(self):
        print("Имя: {}, Возраст: {}, Пол: {}".format(self.name, self.age, self.gender))

person = Person("Коля", 17, "мужской")
person.print_info()
