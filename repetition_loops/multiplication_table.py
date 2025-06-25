#Receive a number and show its multiplication table.

a = float(input("enter a number: "))
print('\n')
for i in range(1 , 11):
    print(f"{a} * {i} = {a*i}")