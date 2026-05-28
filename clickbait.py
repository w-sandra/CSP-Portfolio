#Sandra
#Clickbait
#Takes in information and creates a clickbait headline

#The biggest food trends of 2020 (you wont believ#9)
def example_headline():
    topic= input("Please enter a topic: ")
    year= input("Please enter a year: ")
    print("The biggest " + topic + " trends of " + year)

#These 4 photos will make you think twice about (blank)
def headline1():
    number= input("Please enter a number: ")
    topic= input("Please enter a topic: ")
    second_topic = input("Please enter another topic: ")
    print("These " + number + " photos will make you think twice about " + topic + " and " + second_topic)

#You need to start doing (example) instead of (example) starting...
def headline2():
    good_habit= input("Please enter a good habit: ")
    bad_habit = input("Please enter a bad habit: ")
    day = input("Please enter a day of the week: ")
    #f String
    print(f"You need to start {good_habit} instead of {bad_habit} starting {day}")

#5 Incredible Roofing Tips You Need to Know
def headline3():
    number= input("Please enter a number: ")
    adjective= input("Please enter a adjective: ")
    skill= input("Please enter a skill: ")
    print("{number} {adjective} {skill} Tips You Need to Know")

#Main
headline1()
headline2()
headline3()
