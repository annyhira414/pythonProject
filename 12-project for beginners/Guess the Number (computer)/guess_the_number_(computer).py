import random

# print(random.randint(1 , 6))
# normal way, but now we are using a function
user = input("what is your name ? : ")


def guess(x):
    my_random_number = random.randint(1, x)
    # when I stop - my guess number equal the random number . then we iterate over something
    guess_num = 0
    while guess_num != my_random_number:
        guess_num = int(input(f"{user} guess the number between 1 to {x} : "))  # using f string
        # print(guess_num) just show my guess number , don't need
        if guess_num < my_random_number:
            print(f"sorry {user} guess again its too low ")
        elif guess_num > my_random_number:
            print(f"sorry {user} guess again too high ")
    print(f"wow you are guess the number {my_random_number} correctly")


guess(30)
'''
2nd steps - ones is done then the computer has a random number , we need to guess the random number .
we need to use input and the computer will tell us whether its too high or too low ,
or if i guess the number then computer say the number is correctly. 
so I need to keep looping until I get the right answer
'''
'''
date - 5/14/22 time 1.50 pm .
date - 5/15/22 time 7.40 am
'''
