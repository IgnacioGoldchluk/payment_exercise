from __future__ import annotations
from typing import Dict, List, Tuple, Protocol
import datetime
from dataclasses import dataclass
from abc import abstractmethod


@dataclass(frozen=True)
class TimeRange:
    start: datetime.time
    end: datetime.time

    def overlapped_hours(self, other_timerange: TimeRange) -> float:
        max_start = max(self.start, other_timerange.start)
        min_end = min(self.end, other_timerange.end)

        if max_start >= min_end:
            return 0.0

        return round((self._time_to_minutes(min_end) - self._time_to_minutes(max_start)) / 60.0)

    def _time_to_minutes(self, time_struct: datetime.time) -> int:
        return time_struct.hour * 60 + time_struct.minute


@dataclass(frozen=True)
class PayRange:
    """
    Class to represent a payment for a range of hours.
    """

    time_range: TimeRange
    usd_per_hour: float

    def payment_from_range(self, worked_range: TimeRange) -> float:
        return self.usd_per_hour * self.time_range.overlapped_hours(worked_range)


WeeklyWorkedHours = Dict[str, List[TimeRange]]


class Payment(Protocol):
    pay_rate: Dict[str, Tuple[PayRange, ...]]

    @abstractmethod
    def calculate_payment(self, employee_worked_hours: WeeklyWorkedHours) -> float:
        """Returns the total payment given the weekly hours worked by an employee"""
        raise NotImplementedError()
