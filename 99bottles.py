#Sandra
#generates and prints out the lyrics to the song "99 Bottles of Milk on the Wall."


def song():
    bottles= 100

    for i in range(101):
        if bottles == 1:
            print(f"{bottles} bottle of milk on the wall")
            print(f"{bottles} bottle of milk")
            print("Take it down pass it around")
            bottles= bottles -1

        elif bottles == 0 :
            print("no more bottles of milk on the wall")
            print("Boo Hoo")

        elif bottles <=100:
                print(f"{bottles} bottles of milk on the wall")
                print(f"{bottles} bottles of milk")
                print("Take one down pass it around")
                bottles=bottles -1
                if bottles== 1:
                    print(f"{bottles} bottle of milk on the wall\n")
                elif bottles <=100:
                    print(f"{bottles} bottles of milk on the wall\n")

#Main
song()
