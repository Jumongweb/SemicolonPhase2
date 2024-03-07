import unittest
from logistic_services import calculate_rider_wage


class MyTestCase(unittest.TestCase):
    def test_that_with25Delivery_EmployeeEarns_9000(self):
        self.assertEqual(9000, calculate_rider_wage(25))

    def test_that_with55Deliveries_EmployeeEarns16_000(self):
        self.assertEqual(16000, calculate_rider_wage(55))

    def test_thatWith65Delivery_EmployeeEarns21_250(self):
        self.assertEqual(21250, calculate_rider_wage(65))

    def test_thatWith80Deliveries_EmployeeEarns45_000(self):
        self.assertEqual(45000, calculate_rider_wage(80))

    def test_thatWithZeroDelivery_EmployeeEarnsOnlyBasePay(self):
        self.assertEqual(5000, calculate_rider_wage(0))

    def test_NegativeDelivery_throwsException(self):
        self.assertRaises(ValueError, lambda: calculate_rider_wage(-50))


if __name__ == '__main__':
    unittest.main()
