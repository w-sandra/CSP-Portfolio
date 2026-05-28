# prompts the user for input and then outputs that same input, replacing each space with ...

#Function
def statement():
    statement= input("Please enter a statment: ")

    statement= statement.replace(" ","...")
    print(statement)

#Main
statement()
