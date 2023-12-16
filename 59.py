class Month:
    def __init__(self, number):
        self.number = number

    def get_month_number(self):
        return self.number

    def get_month_name(self):
        month_names = ["Январь", "Февраль", "Март", "Апрель", "Май", "Июнь", "Июль", "Август", "Сентябрь", "Октябрь", "Ноябрь", "Декабрь"]
        return month_names[self.number - 1]

    def get_last_day(self):
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        return days_in_month[self.number - 1]

    def get_first_day_of_week(self):
        return (self.number + 6) % 7

    def get_last_day_of_week(self):
        return (self.number + self.get_last_day() - 1) % 7

