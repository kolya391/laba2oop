class ZateExt(Zate):
    def add_years(self, years):
        new_date = self.date + timedelta(days=years * 365)
        return Zate(new_date.year, new_date.month, new_date.day)

    def subtract_years(self, years):
        new_date = self.date - timedelta(days=years * 365)
        return Zate(new_date.year, new_date.month, new_date.day)

    def add_months(self, months):
        new_date = self.date + timedelta(days=months * 30)
        return Zate(new_date.year, new_date.month, new_date.day)

    def subtract_months(self, months):
        new_date = self.date - timedelta(days=months * 30)
        return Zate(new_date.year, new_date.month, new_date.day)

    def add_days(self, days):
        new_date = self.date + timedelta(days=days)
        return Zate(new_date.year, new_date.month, new_date.day)

    def subtract_days(self, days):
        new_date = self.date - timedelta(days=days)
        return Zate(new_date.year, new_date.month, new_date.day)
