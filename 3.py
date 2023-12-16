class Employee:
    def __init__(self):
        self.name = None
        self.age = None
        self.salary = None

employee = Employee()

employee.name = 'Kolya'
employee.age = 16
employee.salary = 100000

print(f"Имя: {employee.name}")
print(f"Возраст: {employee.age}")
print(f"Зарплата: {employee.salary}")

