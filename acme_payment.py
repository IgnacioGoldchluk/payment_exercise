from typing import Dict, Tuple
import datetime
from payment import PayRange, Payment, TimeRange, WeeklyWorkedHours


class ACMEPayment(Payment):
    pay_rate: Dict[str, Tuple[PayRange, ...]] = {
        "MO": (
            PayRange(
                TimeRange(datetime.time(hour=0, minute=0), datetime.time(hour=9, minute=0)),
                usd_per_hour=25.0,
            ),
            PayRange(
                TimeRange(
                    start=datetime.time(hour=9, minute=0), end=datetime.time(hour=18, minute=0)
                ),
                usd_per_hour=15.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=18, minute=0), datetime.time(hour=23, minute=59)),
                usd_per_hour=20.0,
            ),
        ),
        "TU": (
            PayRange(
                TimeRange(datetime.time(hour=0, minute=0), datetime.time(hour=9, minute=0)),
                usd_per_hour=25.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=9, minute=0), datetime.time(hour=18, minute=0)),
                usd_per_hour=15.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=18, minute=0), datetime.time(hour=23, minute=59)),
                usd_per_hour=20.0,
            ),
        ),
        "WE": (
            PayRange(
                TimeRange(datetime.time(hour=0, minute=0), datetime.time(hour=9, minute=0)),
                usd_per_hour=25.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=9, minute=0), datetime.time(hour=18, minute=0)),
                usd_per_hour=15.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=18, minute=0), datetime.time(hour=23, minute=59)),
                usd_per_hour=20.0,
            ),
        ),
        "TH": (
            PayRange(
                TimeRange(datetime.time(hour=0, minute=0), datetime.time(hour=9, minute=0)),
                usd_per_hour=25.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=9, minute=0), datetime.time(hour=18, minute=0)),
                usd_per_hour=15.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=18, minute=0), datetime.time(hour=23, minute=59)),
                usd_per_hour=20.0,
            ),
        ),
        "FR": (
            PayRange(
                TimeRange(datetime.time(hour=0, minute=0), datetime.time(hour=9, minute=0)),
                usd_per_hour=25.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=9, minute=0), datetime.time(hour=18, minute=0)),
                usd_per_hour=15.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=18, minute=0), datetime.time(hour=23, minute=59)),
                usd_per_hour=20.0,
            ),
        ),
        "SA": (
            PayRange(
                TimeRange(datetime.time(hour=0, minute=0), datetime.time(hour=9, minute=0)),
                usd_per_hour=30.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=9, minute=0), datetime.time(hour=18, minute=0)),
                usd_per_hour=20.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=18, minute=0), datetime.time(hour=23, minute=59)),
                usd_per_hour=25.0,
            ),
        ),
        "SU": (
            PayRange(
                TimeRange(datetime.time(hour=0, minute=0), datetime.time(hour=9, minute=0)),
                usd_per_hour=30.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=9, minute=0), datetime.time(hour=18, minute=0)),
                usd_per_hour=20.0,
            ),
            PayRange(
                TimeRange(datetime.time(hour=18, minute=0), datetime.time(hour=23, minute=59)),
                usd_per_hour=25.0,
            ),
        ),
    }

    def calculate_payment(self, employee_worked_hours: WeeklyWorkedHours) -> float:
        total = 0.0
        for abbreviated_day, payment_ranges in self.pay_rate.items():
            for payment_range in payment_ranges:
                for worked_range in employee_worked_hours.get(abbreviated_day, list()):
                    total += payment_range.payment_from_range(worked_range)
        return total
