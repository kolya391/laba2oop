class Position:
    def __init__(self, title):
        self.title = title

class Department:
    def __init__(self, name):
        self.name = name

class User:
    def __init__(self, name, position, department):
        self.name = name
        self.position = position
        self.department = department

position = Position("Адвокат")
department = Department("Экономический")

user = User("Данил Петров", position, department)

print(user.name)
print(user.position.title)
print(user.department.name)
