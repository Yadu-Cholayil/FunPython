#Guess the number the computer has in mind.
import random

def guess(num,allowedCount):
    randomNum = random.randint(1, num)
    guess = 0
    count = 0
    while guess != randomNum and count != allowedCount:
        guess = int(input("Guess the number: "))
        count += 1
        if guess < randomNum:
            print("Guess again, value is too low")
        elif guess > randomNum:
            print("Guess again, value is too high")
    if guess != randomNum and count == allowedCount:
        print("Better Luck Next Time")
    else:
        print(f'Congratulations!!!, You have guessed {randomNum} correctly in {count} tries!!!')

print("GUESS THE NUMBER")
print('Select a level of difficulty \n \
press 1 for Easy \n \
press 2 for Medium \n \
press 3 for Hard')

level = int(input())
if level == 1:
    print('Easy Difficulty - 1 to 10 \n You have 3 tries')
    guess(10,3)
elif level == 2:
    print('Medium Difficulty - 1 to 40 \n You have 5 tries')
    guess(40,5)
elif level ==3:
    print('Hard Difficulty - 1 to 100 \n You have 10 tries')
    guess(100,10)
else:
    print("Please make a valid selection")

