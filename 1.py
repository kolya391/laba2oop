class Car:
    def __init__(self):
        self.color = None
        self.fuel = 0
        self.brand = None
        self.year = 0

    def go(self):
        print("Машина поехала.")

    def turn(self):
        print("Машина повернула.")

    def stop(self):
        print("Машина остановилась.")

    def info(self):
        print("Информация об машине:")
        print(f"Марка: {self.brand}")
        print(f"Год выпуска: {self.year}")
        print(f"Цвет: {self.color}")
        print(f"Уровень топлива: {self.fuel}")

myCar = Car()

myCar.color = 'Черный'
myCar.fuel = 60
myCar.brand = 'Мерседес'
myCar.year = 2023

myCar.info()