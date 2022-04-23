from typing import Dict
import datetime
from payment import WeeklyWorkedHours, TimeRange


def parse_from_file(filename: str) -> Dict[str, WeeklyWorkedHours]:
    with open(filename, "r") as f:
        all_employees = f.read().splitlines()

    employees_weekly_work = dict()
    for employee_info in all_employees:
        employee, employee_worked_hours = employee_info.split("=")
        employees_weekly_work[employee] = parse_to_time_ranges(employee_worked_hours)

    return employees_weekly_work


def parse_to_time_ranges(employee_worked_hours: str) -> WeeklyWorkedHours:
    return [time_range_string_to_object(period) for period in employee_worked_hours.split(",")]


def time_range_string_to_object(period: str) -> TimeRange:
    day_alias, schedule = period[:2], period[2:]
    start, end = [datetime.datetime.strptime(d, "%H:%M").time() for d in schedule.split("-")]
    return TimeRange(day_alias, start, end)
