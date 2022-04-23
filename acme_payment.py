from datetime import time
import itertools
from payment import PayRange, Payment, TimeRange, WeeklyWorkedHours


class ACMEPayment(Payment):
    pay_rate = (
        PayRange(TimeRange("MO", time(hour=0, minute=0), time(hour=9, minute=0)), 25.0),
        PayRange(TimeRange("MO", time(hour=9, minute=0), time(hour=18, minute=0)), 15.0),
        PayRange(TimeRange("MO", time(hour=18, minute=0), time(hour=23, minute=59)), 20.0),
        PayRange(TimeRange("TU", time(hour=0, minute=0), time(hour=9, minute=0)), 25.0),
        PayRange(TimeRange("TU", time(hour=9, minute=0), time(hour=18, minute=0)), 15.0),
        PayRange(TimeRange("TU", time(hour=18, minute=0), time(hour=23, minute=59)), 20.0),
        PayRange(TimeRange("WE", time(hour=0, minute=0), time(hour=9, minute=0)), 25.0),
        PayRange(TimeRange("WE", time(hour=9, minute=0), time(hour=18, minute=0)), 15.0),
        PayRange(TimeRange("WE", time(hour=18, minute=0), time(hour=23, minute=59)), 20.0),
        PayRange(TimeRange("TH", time(hour=0, minute=0), time(hour=9, minute=0)), 25.0),
        PayRange(TimeRange("TH", time(hour=9, minute=0), time(hour=18, minute=0)), 15.0),
        PayRange(TimeRange("TH", time(hour=18, minute=0), time(hour=23, minute=59)), 20.0),
        PayRange(TimeRange("FR", time(hour=0, minute=0), time(hour=9, minute=0)), 25.0),
        PayRange(TimeRange("FR", time(hour=9, minute=0), time(hour=18, minute=0)), 15.0),
        PayRange(TimeRange("FR", time(hour=18, minute=0), time(hour=23, minute=59)), 20.0),
        PayRange(TimeRange("SA", time(hour=0, minute=0), time(hour=9, minute=0)), 30.0),
        PayRange(TimeRange("SA", time(hour=9, minute=0), time(hour=18, minute=0)), 20.0),
        PayRange(TimeRange("SA", time(hour=18, minute=0), time(hour=23, minute=59)), 25.0),
        PayRange(TimeRange("SU", time(hour=0, minute=0), time(hour=9, minute=0)), 30.0),
        PayRange(TimeRange("SU", time(hour=9, minute=0), time(hour=18, minute=0)), 20.0),
        PayRange(TimeRange("SU", time(hour=18, minute=0), time(hour=23, minute=59)), 25.0),
    )

    def calculate_payment(self, employee_worked_hours: WeeklyWorkedHours) -> float:
        return sum(
            pay_range.payment_from_range(worked_range)
            for pay_range, worked_range in itertools.product(self.pay_rate, employee_worked_hours)
        )
