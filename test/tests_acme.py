import unittest
import datetime
from acme_payment import ACMEPayment
from payment import TimeRange


class TestAcmePayment(unittest.TestCase):
    def test_acme_pays_expected(self):
        worked = {"MO": [TimeRange(datetime.time(0, 0), datetime.time(12, 0))]}
        company = ACMEPayment()

        self.assertEqual(company.calculate_payment(worked), 25.0 * 9 + 15.0 * 3)

    def test_no_work_pays_zero(self):
        worked = dict()
        company = ACMEPayment()

        self.assertEqual(company.calculate_payment(worked), 0)
