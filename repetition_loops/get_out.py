#Create a loop that only ends when the user types "exit".

a = input("say a word : ")

while a != 'exit':
    print("You're in loop. Enter exit to exit.")
    a = input("say a word : ")
    if a == 'exit':
        break

print("Bye!")