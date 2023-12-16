class Employee:
    def show(self, name, salary):
        return name + ' ' + salary
employee = Employee()
print(employee.show("Kolya", "50000"))
