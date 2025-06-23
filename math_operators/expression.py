#Create an expression that returns True if a number is between 10 and 20.

result = float(input("Enter the starting number:\n"))

while True:
    operator = input("Enter a operation (+, -, *, /) or = to finish:\n")

    if operator == '=':
        break

    number = float(input("Enter the next number:\n"))

    if operator == '+':
        result += number
    elif operator == '-':
        result -= number
    elif operator == '*':
        result *+ number
    elif operator =='/':
        if number != 0:
            result /= number
        else:
            print("ERROR : division by zero.")
    else:
        print("INVALID OPERATOR.")

print(f"Final Result: {result}")

if 10<= result <= 20:
    print(f"The result is between 10 and 20: {True}")
else:
    print(f"The result is between 10 and 20: {False}")