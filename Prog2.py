print("-----------------------------------------------------------")
print("Welcome to U Guess the Num \n Come and Play!")
print("-----------------------------------------------------------")
print("Note! Make sure that your answer is a number.")
print("-----------------------------------------------------------")

import random

the_num = random.randint(0,100)

def getPlayerNum():
    your_num = int(input("Enter your guess number from 0-100: "))
    return your_num

your_guess = getPlayerNum()

while your_guess != the_num:
    if your_guess > the_num:
        print("-----------------------------------------------------------")
        print("Try again. Make it Lower!(less than)")
        print("-----------------------------------------------------------")
        your_guess = getPlayerNum()

    else:
        print("-----------------------------------------------------------")
        print ("Try again. Make it Higher!(greater than)")
        print("-----------------------------------------------------------")
        your_guess = getPlayerNum()

print("YOU GOT IT RIGHT!")
print(f"The number is {the_num}")