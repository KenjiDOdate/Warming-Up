#Check if a number is positive, negative or zero.

number = float(input("Enter a number: "))

if number > 0:
    print(f"The number {number} is positive")
elif number == 0:
    print(f"The number {number} is zero")
else:
    print(f"The number {number} is negative")