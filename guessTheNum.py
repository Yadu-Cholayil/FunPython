#Guess the number the computer has in mind.
import random

def guess(num):
    randomNum = random.randint(1, num)
    guess = 0
    while guess != randomNum:
        guess = int(input("Guess the number: "))
        if guess < randomNum:
            print("Guess again, value is too low")
        elif guess > randomNum:
            print("Guess again, value is too high")
    print(f'Congratulations!!!, You have guessed {randomNum} correctly!!!')

print('Select a level of difficulty \n \
press 1 for Easy \n \
press 2 for Medium \n \
press 3 for Hard')

level = int(input())
if level == 1:
    print('Easy Difficulty - 1 to 10')
    guess(10)
elif level == 2:
    print('Medium Difficulty - 1 to 40')
    guess(40)
elif level ==3:
    print('Hard Difficulty - 1 to 100')
    guess(100)
else:
    print("Please make a valid selection")

