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

def win_loseChecker(a_list, b_list):
    if sorted(a_list) == sorted(b_list):
        print("Winner!")
    else:
        print("You Lose!")

def anotherGame():
    player_num = getPlayerNum()
    lottery_num = getLotNum()

    print(f"Your number: {player_num} \n Lottery Number: {lottery_num}")
    
    win_loseChecker(player_num, lottery_num)

anotherGame()
while True:
    print("Thank for playing! \nPlease type 'y' if you want to play again and type 'n' if not.")
    yes_no = input("Want to play again?: ")
    if yes_no == 'y':
        print("-----------------------------------------------------------")
        print("Note! Make sure that your input digit are from 0-9 only.")
        print("-----------------------------------------------------------")
        anotherGame()
    else:
        print("Game Over. Bye!")
        break