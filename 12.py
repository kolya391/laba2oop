class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def get_name(self):
        print(self.name)
    def get_salary(self):
        print(self.salary)
    def increase_salary(self):
        self.salary *= 1.1
employee = Employee("Kolya", 100000)
employee.get_name()
employee.get_salary()
employee.increase_salary()
employee.get_salary()