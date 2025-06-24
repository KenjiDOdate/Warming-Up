#Receive a salary and calculate tax: <2000 exempt, <5000 = 10%, above that 20%.

salary = float(input("Enter your salary: "))

if salary < 2000:
    print("EXEMPT!")
elif 2000 <= salary <= 5000:
    print(f"The income tax of {salary} will be {salary * 0.1}")
else:
    print(f"The income tax of {salary} will be {salary * 0.2}")