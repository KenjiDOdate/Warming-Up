#Check if a number is divisible by 3.

number = int(input("Choose a number:\n"))

if(number % 3 == 0 ):
    print(f"\nThe number {number} is DIVISIBLE by 3.\n")
else:
    print(f"\nThe number {number} is NOT DIVISIBLE by 3.\n")