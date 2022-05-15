import random


def computer_guess(x):
    low = 1
    high = x
    feedback = " "
    while feedback != 'c':
        random_number = int(random.randint(low, high))
