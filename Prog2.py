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