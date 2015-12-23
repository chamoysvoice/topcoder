class Weekday:
    def __init__(self):
        self.months = [31, 'variable', 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        self.days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

    def getDay(self, month, day, year):
        self.months[1] = 29 if year % 4 == 0 else 28
        _day = day + 365 * (year - 1990 - 1) + ((year - 1988) / 4)
        for b in range(month - 1):
            _day += self.months[b]
        return self.days[_day % 7]


# Test case
w = Weekday()
print w.getDay(1, 1, 1990)
print w.getDay(11, 2, 1993)
