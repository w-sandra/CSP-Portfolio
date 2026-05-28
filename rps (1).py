#Sandra
#rock paper scissors game

choice= input("Select rock, paper, or scissors: ")

import random
rand=random.randint(1,3)
if rand==1:
    rand="rock"
if rand==2:
    rand="paper"
if rand==3:
    rand="scissors"

x=0
y=0
#Functions
def game():
    rand=random.randint(1,3)
    if rand==1:
        rand="rock"
    if rand==2:
        rand="paper"
    if rand==3:
        rand="scissors"
        global x
        global y
    while True:
        choice= input("Select rock, paper, or scissors: ")
        rand=random.randint(1,3)
        if rand==1:
            rand="rock"
        elif rand==2:
            rand="paper"
        elif rand==3:
            rand="scissors"

            if choice=="rock" and rand=="paper":
                print("you won!")
                x=x+1

            elif choice=="rock" and rand=="scissors":
                print("you won!")
                x= x+1

            elif choice=="paper" and rand=="rock":
                print("you won!")
                x=x+1

            elif choice=="paper" and rand=="scissors":
                print("you lose!")
                y=y+1

            elif choice=="scissors" and rand=="paper":
                print("you won!")
                x=x+1

            elif choice=="scissors" and rand=="rock":
                print("you lose!")
                y=y+1


            else:
                print("Tie")

        print(f"Player: {x} | Computer: {y}")
        play=input("Would you like to play again yes or no? ")
        if play=="yes":
            game()
        if play=="no":
            print("End")
            break




