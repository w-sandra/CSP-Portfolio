#Sandra

#Functions
#Convert takes in a message and returns the message with :) and :( converted to 🙂 and 🙁
def convert (msg):
    message= msg.replace(":)","🙂").replace(":(", "🙁")

    return message


def main():
    msg= input("Enter Text: ")
    print( convert(msg) )

#Main
main()
