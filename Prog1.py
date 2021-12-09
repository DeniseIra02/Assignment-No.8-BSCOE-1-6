print("-----------------------------------------------------------")
print("Welcome to 3numLOTTERY! \n Come Play and Win!")
print("-----------------------------------------------------------")
print("Note! Make sure that your input digit are from 0-9 only.")
print("-----------------------------------------------------------")

import random

def getPlayerNum():
    num_one = int(input("Enter your first number: \n>"))
    num_two = int(input("Enter your second number: \n>"))
    num_three = int(input("Enter your third number: \n>"))
    yourNum_list = [num_one, num_two, num_three]
    return yourNum_list

def getLotNum():
    lotN1, lotN2, lotN3 = random.sample(range (0,9),3)
    lotNum_list = [lotN1, lotN2, lotN3]
    return lotNum_list

player_num = getPlayerNum()
lottery_num = getLotNum()