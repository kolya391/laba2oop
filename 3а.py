class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(f"Имя: {self.name}")
        print(f"Возраст: {self.age}")

person1 = Person("Коля", 17)
person1.print_info()
person2 = Person("Даня", 18)
person2.print_info()
