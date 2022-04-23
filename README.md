# Programming Challenge

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