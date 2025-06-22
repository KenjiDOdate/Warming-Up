from datetime import date

#Declare a boolean variable that indicates whether the person is of legal age (age >= 18).

#the current year
current_year = date.today().year

#the user insert the age who they born
birth_year = int(input("Please, insert your year of birth:\n"))

#Calculate the age

age = current_year - birth_year

#Check if the person is >=18 or not

if(age >=18):
    ismajor = True
else:
    ismajor = False

print(f"They're of legal age: {ismajor}.")
