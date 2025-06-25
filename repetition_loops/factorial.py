#Receive a number and calculate the factorial.

number = int(input("Enter a number: "))

for i in range(1, number):
    number *= i

print(f"Factorial Result: {number}")