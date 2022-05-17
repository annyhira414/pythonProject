import random
import math

lower = int(input("input your lower limit number: "))
upper = int(input("input your upper limit number: "))

# print(f"your number range {lower} to {upper}")
guess = int(input("please guess your number "))

if guess < lower or guess > upper:
    print(f"this is not your range number please enter your number between {lower} to {upper}")
else:
    random_num = random.randint(lower, upper)
    chances = round(math.log(upper - lower + 4, 2))

    while chances > 0:
        chances = chances - 1
        if guess > random_num:
            print("too high")
        elif guess < random_num:
            print("too low")
        else:
            print(f"you win! your guess was right! the number is {random_num}")
            break
        if chances != 0:
            print(f"you have {chances} left chances so try again ")
            guess = int(input("please guess your number "))

        else:
            print("sorry you lost your change ")
