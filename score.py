#Sandra

count = 0
points= 100
def score():
    global count
    count = count + 100
    print(f"You earned {points} points")


#Main
score()
score()
score()
print(f"Total score: {count}")




