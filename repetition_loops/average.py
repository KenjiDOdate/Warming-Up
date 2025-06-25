#Ask the user for 5 numbers and calculate the average.
total = 0.0
for i in range(1, 6):
    number = float(input("Enter a Number : "))
    total += number

print(total)