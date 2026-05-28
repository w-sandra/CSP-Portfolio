#Sandra
#Madlibs
#Silly story using input

#functions
import random

def madlibs():
    print("If you want to select randomly for any question then respond with random")
    person= input("Please enter a person: ")
    if person=="random":
        people= ["Katie", "Kendrick", "Billy",]

        random.choice(people)
        name= random.choice(people)

    country= input("Please enter a country: ")
    if country=="random":
        place= ["U.S", "Japan", "Brasil",]

        random.choice(place)
        country= random.choice(place)

    adjective= input("Please enter a adjective: ")
    if adjective=="random":
        word= ["blue", "shiny", "strange",]

        random.choice(word)
        adjective= random.choice(word)

    silly= input("Please input a silly word: ")
    if silly=="random":
        funny= ["skibiti", "pumpkin", "labubu",]

        random.choice(funny)
        silly= random.choice(funny)

    number= input("Please enter a number: ")
    food= input("Please enter a food: ")

    #Story
    print(f"""For my birthday I went with \033[1m{name.upper()}\033[0m to \033[1m{country.upper()}\033[0m where we found a \033[1m{adjective.upper()}\033[0m store. We went inside and yelled "\033[1m{silly.upper()}\033[0m" outloud infront of \033[1m{number.upper()}\033[0m people as they ate \033[1m{food.upper()}\033[0m.""")



#Main
madlibs()
