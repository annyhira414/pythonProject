import random

'''
computer guess my number .
'''


def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != 'c':
        guess_number = int(random.randint(low, high))
        feedback = input(f"its {guess_number} number is too high(H) , too low (l) or correct (c) : ").lower()
        if feedback == 'h':
            high = guess_number - 1
        elif feedback == 'l':
            low = guess_number - 1

    print(f"good job computer {guess_number} it is my number ")


computer_guess(10)
