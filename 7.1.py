class Employee:
  name = None
  salary = None

  def show(self):
    print(self.name)
employee = Employee()
employee.name = 'Kolya'
employee.salary = 100000
employee.show()