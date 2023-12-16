class User:
 def __init__(self,name, surname, year):
  super(name, surname)
  self.year = year

 def getYear(self):
  return self.year
class Employee(User):
    def __init__(self, name, surname, age, salary):
        super().__init__(name, surname)
        self.age = age
        self.salary = salary

    def getAge(self):
        return self.age

    def getSalary(self):
        return self.salary
