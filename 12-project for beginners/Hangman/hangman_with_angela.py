import random

data = ["mouse", "apple", "rice"]
chosen_word = random.choice(data)
print(chosen_word)


# s2
guess = input("please guess the letters:  ").lower()
display = []
for _ in chosen_word:
    display += "_"
print(display)
# if chosen_word in data:
# if the later the user guessed is one of the letters in the chosen word

for letter in chosen_word:
    if letter == guess:
        print('right')
    else:
        print("wrong")
