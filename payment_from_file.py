from employee_parser import parse_from_file
from acme_payment import ACMEPayment
import sys

if __name__ == "__main__":
    # Just using sys.argv, for more robust argument parsing one can use argparse or click
    filename = sys.argv[1]
    employees_dict = parse_from_file(filename)
    company = ACMEPayment()

    for employee_name, week_work in employees_dict.items():
        print(f"The amount to pay {employee_name} is: {company.calculate_payment(week_work)} USD")
