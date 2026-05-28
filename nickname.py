#Sandra
#Fairy nicknames

#Functions

def nickname():

    start= input("Which would you prefer to visit a garden or a library: ")
    #Garden
    if start== "garden" :
        choice= input("Do you like to observe or hear: ")

        if choice== "hear":
            choice= input("Do you prefer to hear birds singing or a waterfall: ")
            if choice== "birds singing":
                 print("Your nickname is bloomer")
            elif choice== "waterfall":
                print("Your nickname is riverflow")



        elif choice== "observe":
            second= input("What colors do you like? (glittery or solid): ")
            if second== "glittery":
                print("Your nickname is goldy")
            elif second== "solid":
                print("Your nickname is Tulip")


    #Library
    if start== "library":
            choice= input("Are you an extrovert or introvert: ")

            if choice== "extrovert":
                second=input("Do you prefer to stand out or stay reserved: ")
                if second== "stand out":
                    print("Shining star")
                elif second== "stay reserved":
                    print("Midnight sparkle")

            elif choice== "introvert":
                second= input("Do you enjoy being with famiy or friends: ")
                if second== "family":
                        print("Dawn")
                elif second== "friends":
                        print("whisper")


#Main
nickname()



