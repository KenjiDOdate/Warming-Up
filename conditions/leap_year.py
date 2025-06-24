#Identify if a year is a leap year.
from datetime import date
import calendar

current_year = date.today().year


if calendar.isleap(current_year):
    print(f"{current_year} IS a leap year.")
else:
    print(f"{current_year} IS NOT a leap year.")