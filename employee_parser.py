from typing import Dict, List
import datetime
from collections import defaultdict
from payment import WeeklyWorkedHours, TimeRange


def parse_from_file(filename: str) -> Dict[str, WeeklyWorkedHours]:
    with open(filename, "r") as f:
        all_employees = f.read().splitlines()

    employees_weekly_work = dict()
    for employee_info in all_employees:
        employee, employee_worked_hours = employee_info.split("=")
        employees_weekly_work[employee] = parse_to_time_ranges(employee_worked_hours)

    return employees_weekly_work


def parse_to_time_ranges(worked_info: str) -> WeeklyWorkedHours:
    worked_hours_per_day: Dict[str, List[TimeRange]] = defaultdict(list)
    per_day = worked_info.split(",")

    for day_info in per_day:
        # The aliases for the days are always length 2
        day_alias, schedule = day_info[:2], day_info[2:]
        worked_hours_per_day[day_alias].append(time_range_string_to_object(schedule))
    return worked_hours_per_day


def time_range_string_to_object(schedule: str) -> TimeRange:
    start, end = [datetime.datetime.strptime(d, "%H:%M").time() for d in schedule.split("-")]
    return TimeRange(start, end)
