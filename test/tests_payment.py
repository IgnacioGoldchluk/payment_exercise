import unittest
from payment import TimeRange, PayRange
import datetime


class TestTimeRange(unittest.TestCase):
    def test_delta_in_minutes(self):
        first = TimeRange("MO", datetime.time(0, 0), datetime.time(8, 40))
        second = TimeRange("MO", datetime.time(4, 20), datetime.time(10, 0))

        self.assertEqual(first.overlapped_hours(second), 4)

    def test_no_overlapping_returns_zero(self):
        first = TimeRange("MO", datetime.time(5, 0), datetime.time(10, 30))
        second = TimeRange("MO", datetime.time(11, 00), datetime.time(20, 0))

        self.assertEqual(first.overlapped_hours(second), 0)

    def test_timerange_is_conmutative(self):
        first = TimeRange("TH", datetime.time(3, 10), datetime.time(4))
        second = TimeRange("TH", datetime.time(1, 50), datetime.time(8, 10))

        self.assertEqual(first.overlapped_hours(second), second.overlapped_hours(first))


class TestPayment(unittest.TestCase):
    def test_pays_the_expected_hours(self):
        pay_range = PayRange(TimeRange("MO", datetime.time(0, 0), datetime.time(8, 0)), 30.0)
        worked_hours = TimeRange("MO", datetime.time(3, 0), datetime.time(8, 0))

        self.assertEqual(pay_range.payment_from_range(worked_hours), 150)

    def test_payment_rounds_up(self):
        pay_range = PayRange(TimeRange("SA", datetime.time(20, 0), datetime.time(23, 59)), 50.0)
        worked_hours = TimeRange("SA", datetime.time(22, 0), datetime.time(23, 59))

        self.assertEqual(pay_range.payment_from_range(worked_hours), 100)
