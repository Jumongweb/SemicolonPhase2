from decimal import Decimal
from commission_employee import CommissionEmployee


class SalaryEmployee(CommissionEmployee):
    def __init__(self, first_name, last_name, nin, sales, rate, gender, base_pay):
        super().__init__(first_name, last_name, nin, sales, rate, gender)
        self.base_pay = base_pay

    @property
    def base_pay(self):
        return self._base_pay

    @base_pay.setter
    def base_pay(self, pay):
        if pay < Decimal(0.0):
            raise ValueError("Invalid pay")
        self._base_pay = pay

    def earning(self):
        return self.base_pay + super().earning()

    def __repr__(self):
        return f"{super().__repr__()}\n" \
               f"Salary: {self.base_pay}\n" \
               f"Salary Earning: {self.earning()}"

if __name__ == '__main__':
    s1 = SalaryEmployee("Izu", "Miriam", 420, 10000, 15, "male", 500000)
    #ying = SalaryEmployee("Ying", "Yang", 422, 20000, 14, "male", 600000)
    c1 = CommissionEmployee("Ying", "yang",421, 12, 15, "male")
    # print(izu)
    #print(izu.earning())
    # print(issubclass(SalaryEmployee, CommissionEmployee))
    # print(issubclass(CommissionEmployee, object))
    # print(issubclass(SalaryEmployee, object))


    # for employee in [s1, c1, a1]:
    #     print(f"{employee}.")