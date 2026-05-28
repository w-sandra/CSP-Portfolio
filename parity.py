#Sandra
#Parity
#This prompts the user for a number and prints wheter that number is even or odd

#Init
#Functions


def main():

    num= int( input("Please enter a number: "))
    if is_even(num):
        print("EVEN")

    else:
        print("ODD")

def is_even(x):
    if x % 2 ==0 :
        return True
    else:
        return False



main()
