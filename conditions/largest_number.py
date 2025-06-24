#Receive three numbers and display the largest one.

largest_number = 0.0
for i in range (0,3):
    number = float(input("enter a number : "))
    if number >= largest_number:
        largest_number = number

print(f"The largest number is {largest_number}")