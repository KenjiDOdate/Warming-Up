#Grading system: if average ≥ 7, passed; between 5 and 7, recovery; < 5, failed.

grades = 0.0
divider = 1
print(f"initial values : grades {grades}, divider {divider}")
while True:
    input_number = input("Enter a grade. If it's over, please, just press : ")

    if input_number == "":
        break
    try:
        grade = float(input_number)
        grades += grade
        divider += 1    

    except ValueError:
        print("Invalid input, please, enter only numbers.")
result = grades / divider

print(f"\n\n The average grade : {result}\n\n")

if result >= 7:
    print("APROVED!")
elif 5<=result <= 7:
    print("RECORVERY!")
else:
    print("FAILED!")


        