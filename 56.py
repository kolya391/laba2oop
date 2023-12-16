class Period:
    def __init__(self, moment1, moment2):
        self.moment1 = moment1
        self.moment2 = moment2

    def get_seconds(self):
        return abs((self.moment2 - self.moment1).total_seconds())

    def get_minutes(self):
        return abs((self.moment2 - self.moment1).total_seconds() // 60)

    def get_hours(self):
        return abs((self.moment2 - self.moment1).total_seconds() // 3600)

    def get_days(self):
        return abs((self.moment2 - self.moment1).days)
