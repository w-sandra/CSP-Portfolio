#Sandra

import random
symbols= ["☁ ","☂", "❄", "☃","☁ ","☂","☁ ","☂","☃","☁ ","☂","☃","☁ ","☂"]
credits=500
casino=500
record= 10,000



while True:
    choice=input("Do you want to spin, deposit, or cash out: ")

    if choice== "deposit":
        amount=int(input("Would you like to deposit 20, 50, or 100: "))
        credits= credits + amount
        print("succes")

    if choice=="spin" and credits >= 10:
        for i in range(1000):
            credits= credits-10
            casino= casino+10
            first= random.choices(symbols)
            second=random.choices(symbols)
            third=random.choices(symbols)
            spin= first, second, third
            if spin==(['❄'], ['❄'], ['❄']):
                print(spin)
                print("Congrates you got the jackpot")
                credits= credits + 500
                casino= casino- 500
                break

            if spin== (['☂'],['☂'],['☂']):
                credits= credits-10
                casino= casino+10
                print(spin)
                print("no gains")


            else:
                credits= credits-10
                casino= casino+10
                print(spin)
                print("no gains")

        if credits == record:
            print(f"You set a new record of {credits} credits")

    if choice=="spin" and credits <= 10:
        print("Not enough credits")

    if choice=="cash out":
        print(f"You earned {credits} credits")
        break

    print(f"You made {credits} credits, casino made {casino} credits")


