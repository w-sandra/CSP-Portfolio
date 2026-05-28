
#Create Task
#Recommends Roller Coasters Based On Users Input

import random
import pandas as pd

data= pd.read_csv('Rollercoasters.csv')

name= data["Rollercoaster Name"].tolist()
park= data["Amusement Park"].tolist()
country= data["Country"].tolist()
height= data["Height"].tolist()
speed=data["Speed"].tolist()
filter=[]


#Functions

def location(place):                                                     #Limits Roller Coasters based on country
    x="not found"                                                        #Throughout the code x will serve as an indicator whether users input is valid
    for i in range(len(name)):


            if place in country[i]:
                filter.append(park[i])
                x="found"
    if x=="found":
        print(f"Here are some Rollercoaster Parks in {place}:")
        print(filter)
        recommend=random.choice(filter)
        print(f"\033[4m I recommend {recommend}\033[0m")
        filter.clear()
    if x=="not found":
        print("Country not found. Please check your spelling")


def park_rides(park_name):                                                         #Limits Roller Coasters to a specific Amusement Park
    x="not found"
    for i in range(len(name)):
        if park_name in park[i]:
            filter.append(name[i])
            x="found"

    if x=="found":
        print(f"Here are some Rollercoasters at {park_name}")
        print(filter)
        recommend=random.choice(filter)
        print(f"\033[4m I recommend {recommend}\033[0m")
        filter.clear()
    if x=="not found":
        print("Park not found. Please check your spelling")

def height_limit(limit):                  #Limits Rollercoasters based on height
    while True:


        if limit=="tiny":
            for i in range(len(name)):
                if height[i] < 15:
                    filter.append(name[i])


        elif limit=="small":
            for i in range(len(name)):
                if height[i] >= 15 and height[i] < 25:
                    filter.append(name[i])



        elif limit=="medium":
            for i in range(len(name)):
                if height[i] >= 25 and height[i] <= 50:
                    filter.append(name[i])
                    continue

        elif limit=="tall":
            for i in range(len(name)):
                if height[i] > 50:
                    filter.append(name[i])
                    continue
        else:
            print("Please type either tiny, small, medium or tall")
            break
        try:
            print(f"Here are some {limit} Rollercoasters")
            print(filter)
            recommend=random.choice(filter)
            print(f"\033[4m I recommend {recommend}\033[0m")
            filter.clear()
            break
        except:
            break


def info(ride):                            #Gives information on a specfic Roller Coaster
    x="not found"
    global filter
    for i in range(len(name)):
        if ride in name[i]:
            filter.append(park[i],)
            filter.append(country[i])
            filter.append(height[i])
            filter.append(speed[i])

            x="found"

    if x=="found":
        print(f"Here is some information on {ride} in order of Park, Country, Speed and Height")
        filter= [filter[i:i + 4] for i in range(0, len(filter), 4)]                  #This algorithm for spliting the list into equal parts is taken from https://stackoverflow.com/questions/12328108/how-can-i-split-a-string-in-python
        print(filter)
        filter.clear()

    if x=="not found":
        print("Ride not found. Please check your spelling")



#Main

def menu():                                                                          #Main Function that user navigates through by entering input
    print("~~~ Welcome! Here to Help you Find your Desired Roller Coaster! ~~~")

    while True:
        print("____________________________________________________________________________________________________________________________________")
        print("What do you want to find?")
        print("a) Find Parks in a Country")
        print("b) Find Rides in an Amusement Park")
        print("c) Find a Ride with your Desired Height")
        print("d) Check information on a ride ")
        print("e) Exit\n ")
        request= input("Enter here: ")

        if request== "a":
            place= input("What country?: ")
            location(place)
            continue

        elif request=="b":
            park_name=input("What park are you searching for: ")
            park_name=park_name.title()
            park_rides(park_name)
            continue

        elif request== "c":
            limit= input("What is the height of your desired Roller Coaster? (tiny, small, medium, or tall) : ")
            height_limit(limit)

        elif request=="d":
            ride= input("What ride do you want to know more about?: ")
            ride=ride.capitalize()
            info(ride)
        elif request=="e":
            print("Hope this helped!")
            break

        else:
            print("_________________________________")
            print("Please type either a, b, c, or d")


#Main
menu()

#Source
#Rollercoaster Dataset
#Website: https://tuvalabs.com/
#URL: https://tuvalabs.com/datasets/?type=datasets&order_by=-pub_date&show=all
