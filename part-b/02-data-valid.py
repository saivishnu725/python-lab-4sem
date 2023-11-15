import re

## patterns
# phone number
phone_pattern = r"^\d{3}-\d{3}-\d{4}$"
# date
date_pattern = r"^\d{4}-\d{2}-\d{2}$"

## validators
# phone number
def validate_phone(number):
    if re.match(phone_pattern, number):
        print(f"{number} is a valid number.")
    else:
        print(f"{number} is not a valid number.")
# date
def validate_date(date):
    if re.match(date_pattern, date):
        print(f"{date} is a valid date.")
    else:
        print(f"{date} is not a valid date.")

## sample inputs
# phone number
validate_phone("123-456-7890")
validate_phone("555-abc-1234")
# date
validate_date("2023-08-29")
validate_date("21-03-15")
validate_date("2023/08/29")
