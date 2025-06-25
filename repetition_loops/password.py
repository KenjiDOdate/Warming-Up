#Simulate a password: the user has 3 attempts.

for i in range(1, 5+1):
    password = input("Enter tjhe password : ")
    if password == "password" or password == "1234" or password == "123456789" or password == "0000" or password == "123":
        print("Password acepted!")
        break
    else:
        print("wrong password. Please try again.")
    print("All your attempts are over.")