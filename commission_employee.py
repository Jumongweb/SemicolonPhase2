from decimal import Decimal
class CommissionEmployee:
    def __init__(self, first_name, last_name, nin, sales, rate, gender):
        self._firstname = first_name
        self._last_name = last_name
        self._nin = nin
        self._sales = sales
        self._rate = rate
        self._gender = gender

    @property
    def first_name(self):
        return self._firstname

    @property
    def last_name(self):
        return self._sales

    @property
    def nin(self):
        return self._nin

    @property
    def sales(self):
        return self._sales

    @property
    def gender(self):
        return self._gender

    @sales.setter
    def sales(self, value):
        if value < Decimal(0.0):
            raise ValueError(f"Invalid amount {value}")
        self._sales = value

    @property
    def rate(self):
        return self._rate

    @rate.setter
    def rate(self, rate):
        #if Decimal(0.0) < rate < Decimal(1.0):
        if rate < Decimal(0.0):
            raise ValueError("Invalid rate amount")
        self.rate = rate

    def earning(self):
        return self.sales * (self.rate / 100)


    def __repr__(self):
        return f"First Name: {self._firstname}\nLast Name: {self._last_name}\n" \
                f"Nin: {self._nin}\nEarning: {self.earning()}"


bioke = CommissionEmployee("Abbey", "Hannah", 419, 50000, 5.0, "male")
#print(bioke)