

weight = float(input("Enter yout weight in kg : "))
height = float(input("Enter yout weight in m : "))

bmi = weight/height

print(f"BMI: {bmi}.")

if bmi < 18.5:
    print("Underweight")
elif 18.5 <= bmi <=24.9:
    print("Normal weight")
elif 25.0 <= bmi <= 29.9:
    print("Overweight")
elif 30.0 <= bmi <= 34.9:
    print("Obesity class 1")
elif 35.0 <= bmi <= 39.9:
    print("Obesity class 2")
else:
    print("Obesity class 3")