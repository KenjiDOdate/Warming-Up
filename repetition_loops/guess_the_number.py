#Create a random number guessing game (hint: random).

import random

random_number = random.randint(-100, 100)


while True:
    user_number = int(input("Guess the number : "))
    if user_number == random_number:
        print("Congrats!! You're right!!")
    
    print("try again.")

