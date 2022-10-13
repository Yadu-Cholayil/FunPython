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
import time
from words import words
import string

def validWord():
    word = random.choice(words) # Chooses a random word
    # while "-" not in word or " " not in word:
    #     word = random.choice(words)
    #     print(word)
    return word.upper()

def hangman():
    word = validWord()
    wordLetters = set(word) # Store letters in a word as a set - avoids duplicates
    alphabet = set(string.ascii_uppercase)
    # User choosed letters
    usedLetters = set()
    
    lives = 7
    # User input a letter
    while len(wordLetters) > 0 and lives > 0:
        print("\n")
        time.sleep(1)
        print(f"lives: {lives}")
        #show the used letters
        print('You have used the letters: ' + ' '.join(usedLetters))

        #show the Word to User
        wordList = [letter if letter in usedLetters else '-' for letter in word]
        print('Current word: ' + " ".join(wordList))

        userLetter = input("Enter your Guess: ").upper()
        if userLetter in alphabet - usedLetters:
            usedLetters.add(userLetter)
            if userLetter in wordLetters:
                wordLetters.remove(userLetter)
            else:
                lives -= 1
                print("Letter not in the word")
        elif userLetter in usedLetters:
            print("You have already entered that character. Please enter another character")
        else:
            print("Enter a Valid character")
    if lives == 0 :
        print(f'You have died. The word was {word}')
    else:
        print(f"Congradulations!!! The word is {word}!!!!!")


hangman()