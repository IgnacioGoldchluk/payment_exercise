# Programming Challenge

## Exercise
The company offers their employees the flexibility to work the hours they want. They will pay for the hours worked based on the day of the week and time of day, according to the following table:

| Hour | Day | Amount |
| -----|-----|---------- |
| 00:01 - 09:00 | Monday-Friday | 25 USD|
| 09:01 - 18:00 | Monday-Friday | 15 USD|
| 18:01 - 00:00 | Monday-Friday | 20 USD|
| 00:01 - 09:00 | Saturday-Sunday| 30 USD|
| 09:01 - 18:00 | Saturday-Sunday| 20 USD|
| 18:01 - 00:00 | Saturday-Sunday| 25 USD|

The goal is to calculate the total that the company has to pay an employee based on the hours they worked and the times during which they worked. The following abbreviations will be used for entering data:

|Abbreviation | Day|
|-----|----|
|MO | Monday|
|TU | Tuesday|
|WE | Wednesday|
|TH | Thursday|
|FR | Friday|
|SA | Saturday|
|SU | Sunday|

Input: the name of an employee and the schedule they worked, indicating the time and hours. This should be a .txt file with at least five sets of data. You can include the data from our two examples below.

Output: indicate how much the employee has to be paid

## Usage
- Tested on Python3.10.1.
- Run tests: `python -m unittest`.
- Execute example txt file: `python payment_from_file.py example.txt`

## Conventions and standards
- Code auto formatedd with black (`--line-length=120`)
- Type annotations verified with **mypy**
- Tested using **unittest** framework from the standard libary.

## Description
- *payment.py*: Main business logic file. Contains the core classes and definitions to be used for any payment.
- *acme_payment.py*: Concrete implementation of ACME payment logic.
- *employee_parser.py*: Parses data and converts it into the appropiate format for the core logic.
- *payment_from_file*: Concrete implementation of payment from file + ACME.

### Notes
- Supports employee working multiple times in the same day.
- `datetime.time` objects might be tedious to instance and work with, `TimeRange` class could be modified to work with basic `(hour, time)` tuple or namedtuple.