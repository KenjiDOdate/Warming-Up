#Classify a person by age: child, teenager, adult, elderly.
from datetime import date

#the current year
current_year = date.today().year

#the user insert the age who they born
birth_year = int(input("Please, insert your year of birth:\n"))

#Calculate the age

age = current_year - birth_year

if 0 <= age <= 11:
    print("KID!")
elif 12 <= age <= 17:
    print("TEENAGER!")
elif 18 <= age <= 59:
    print("ADULT!")
else:
    print("ELDERLY!")