class Employee:
    def __init__(self, name, salary, age):
        self.__name = name
        self.__salary = salary
        self.__age = age
    def get_name(self):
        return self.__name
    def get_salary(self):
        return self.__salary
    def get_age(self):
        return self.__age
employee = Employee("Kolya", 100000, 16)
print(employee.get_name())
print(employee.get_salary())
print(employee.get_age())
