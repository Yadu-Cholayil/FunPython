# Game of hangman
# Computer should have a word list
# Computer chooses a random word from wordlist
# Computer shows the words with hiphens in place
# User inputs a charector
# Checks
# Takes if the charector is present, word is modified with letter in place of word
# Idea of limit with lives
# Should print used letters on the page 

import random
from words import words

word = random.choice(words)
print(word)