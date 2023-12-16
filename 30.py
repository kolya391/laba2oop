class User:
    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

class Employee(User):

    def get_salary(self):
        return self.__salary

    def set_salary(self, salary):
        self.__salary = salary

    def get_surname(self):
        return self.__surname

    def set_surname(self, surname):
        self.__surname = surname

emp = Employee()
emp.set_name("Коля")
emp.set_surname("Беляев")
emp.set_salary(350000000)

print(emp.get_name())
print(emp.get_surname())
print(emp.get_salary())
