#Sandra
#Hogwarts
#asks for input and assigns house


#Init
import time
import random


#this function checks a name and returns a house from harry potter
def house(name):
    if name== "harry" or name== "ron" or name== "hermione" :
        return "Gryffindor"
    if name== "Newt" or name== "Nymphadora" or name== "Pomona" :
        return "Hufflepuff"
    if name== "Luna" or name== "Cho" or name== "Filius":
        return "Ravenclaw"
    if name== "Voldemort" or name== "Draco" or name== "Serverus":
        return "Slytherin"

    else:
        num= int(random.randint(1, 4))
        if num== 1:
            return "Gryffindor"
        if num== 2:
            return "Hufflepuff"
        if num==3 :
            return "Ravenclaw"
        if num== 4:
            return "Slytherin"




#Functions
def main():
    print("Welcome to Hogwarts")
    name= input("Please enter your name: ")
    time.sleep(1)
    print("..")
    time.sleep(1)
    print("...")
    time.sleep(1)
    print("....")
    print(house(name))


#Main
main()
