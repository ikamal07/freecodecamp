import random


def comp_guess(x):
    min = 1
    max = x
    feedback = ''
    while feedback != 'c':
        guess = random.randint(min, max)
        feedback = input(f"Is {guess} is low/high/correct  :")
        if feedback == 'l':
            print(f"Too Low, Guess Again")

            min = guess + 1
        elif feedback == 'h':
            print("Too High, Guess Again")

            max = guess - 1
        else:
            print(f"You guessed it correctly {guess}")

comp_guess(100)
