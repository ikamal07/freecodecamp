# This is a sample Python script.
import random
num = random.randint(1,10)
for i in range(1,10):
    guess = int(input("Enter your guess :"))
    if guess == num:
        print("you entered correct")
        exit()
    elif guess < num:
        print("too low , guess little higher")
    else:
        print("Too High ,lower your guess")



