#Sandra

#prompts users to enter two numbers, an operator, and prints the result of the operation

#Imnit
#Functions
def main ():
    print("Welcome")
    num1= int(input("Pleaser enter first number: "))
    num2= int(input("Please enter second number: "))
    operator= input("Please enter an operator: ")

    if operator == "+":
        print( calc_sum(num1,num2))

    elif operator == "-":
        print( calc_sub(num1,num2))

    elif operator == "*":
        print( calc_mult(num1,num2))

    elif operator =="/":
        print( calc_div(num1,num2))


def calc_sum(x,y):
    return x + y


def calc_sub(x,y):
    return x-y

def calc_mult(x,y):
    return x * y

def calc_div(x,y):
    return x / y

main()
