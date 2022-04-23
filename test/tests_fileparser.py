import unittest
from employee_parser import time_range_string_to_object, parse_to_time_ranges
from payment import TimeRange
import datetime


class TestFileParser(unittest.TestCase):
    def test_converts_time_to_object(self):
        range_string = "01:23-09:54"
        expected = TimeRange(datetime.time(1, 23), datetime.time(9, 54))
        self.assertEqual(time_range_string_to_object(range_string), expected)

    def test_days_string_to_obejct(self):
        days_string = "MO04:21-10:11,WE21:12-23:50"
        expected = {
            "MO": [TimeRange(datetime.time(4, 21), datetime.time(10, 11))],
            "WE": [TimeRange(datetime.time(21, 12), datetime.time(23, 50))],
        }
        self.assertEqual(parse_to_time_ranges(days_string), expected)
