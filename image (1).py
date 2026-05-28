#Images
#Tutorial on how to open images using python

#Initialize

import webbrowser

#Functions
url = ["https://tinyurl.com/53976ae3" , #Muffin
       "https://tinyurl.com/284k3urt", #Ramen
       "https://tinyurl.com/msjmx63a", #chips
       "https://tinyurl.com/yt7kd4x3"  #Chocolate
        ]

descriptions=["A Triple Chocolate Muffin is moist and fluffy.I recommend it since its perfect to enjoy with milk",
               "Spicy Ramen garnished with hearty toppings like soy-marinated eggs, pork belly, pickled bamboo shoots and fish cakesas. I recommend since its a perfect meal when craving something spicy",
                 "Spicy Runner Chips. Recommend as a tiny snack", "Yummy lindor chocolate. Reccommend as a tiny sweet treat."]


def select():
    print("I heard your craving a snack")
    choice= input("Do you want a spicy or sweet treet: ")

    if choice=="spicy":
        pick= input("Something big or small: ")
        if pick=="big":
            webbrowser.open(url[1])
            print(descriptions[1])
        if pick=="small":
            webbrowser.open(url[2])
            print(descriptions[2])

    if choice=="sweet":
        pick=input("Something like bread or candy: ")
        if pick=="bread":
            webbrowser.open(url[0])
            print(descriptions[0])
        if pick=="candy":
            webbrowser.open(url[3])
            print(descriptions[3])

#Main
select()


#Sources of Information
    #Picture of Chocolate Muffin
#Website Name: sweets by elise
#Author Name: Elise
#URL:https://sweetsbyelise.com/triple-chocolate-muffins/
#Arcticle Title: Triple Chocolate Muffins
#Date:

    #Picture of Ramen
#Cooking
#Naz Deravian
#URL: https://cooking.nytimes.com/recipes/1024748-shoyu-ramen
#Shoyu Ramen
#Jan. 10, 2024

    #Picture of Chips
#Lat'n Sweets
#URL:https://tinyurl.com/k7khbck4
#Runners Chips 3 Pack

    #Chocolate candy
#Walmart
#URL:https://tinyurl.com/yt7kd4x3
#Lindt Lindor Milk Chocolate Truffle Candy Bar, 3.5 oz.


