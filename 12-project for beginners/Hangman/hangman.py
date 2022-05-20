import random
import string
from words import words


def get_valis_word(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)

        return word


def hangman():
    word = get_valis_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()  # what the user is guess

    # getting user input

    user_latter = input("guess the letter: ").upper()
    if user_latter in alphabet - used_letters:
        used_latters.add(user_latter)



user_input = input("enter your word")
print(user_input)
