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
    used_latter = set()  # what the user is guess


user_input = input("enter your word")
print(user_input)
