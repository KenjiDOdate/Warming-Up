#Get grade1 and grade2 and calculate the average. Display if the student passed (>= 6).

grade1 = float(input("Enter the first grade: "))
grade2 = float(input("Enter the first grade: "))

average_grade = (grade1 + grade2)/2

print(f"Final Result: {average_grade}")

if average_grade >=6:
    print("Approved")
else:
    print("failed")