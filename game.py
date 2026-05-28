#Sandra, Angela


import random
import time
score= 0

start_time= time.time()

diff= input("Choose difficulty easy, medium, hard: ")

if diff== "easy":
        rand= random.randint(1,10)
        for i in range(5):

                number= int(input("Guess a number between 1 and 10: "))
                if number== rand:
                    print("Yay")
                    break

                elif number > rand:
                    print("Too high. Try again")


                elif number < rand:
                    print("Too low. Try again")

elif diff== "medium":
        rand= random.randint(1,25)
        for i in range(5):
                number= int(input("Guess a number between 1 and 25: "))
                if number== rand:
                    print("Yay")
                    break

                elif number > rand:
                    print("Too high. Try again")


                elif number < rand:
                    print("Too low. Try again")

elif diff== "hard":
        rand= random.randint(1,50)
        for i in range(10):
                number= int(input("Guess a number between 1 and 50: "))
                if number== rand:
                    print(f"Yay your score is {score} ")
                    break

                elif number > rand:
                    print("Too high. Try again")


                elif number < rand:
                    print("Too low. Try again")


end_time = time.time()
elapsed_time = end_time - start_time
print(f"Elapsed time: {elapsed_time} seconds")
