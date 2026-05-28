#Sandra
#To-Do List to keep track of items

#Movies
todo= []

done=[]

def todo_list():
    while True:
        movie=input("What do you want to do with the list? a)see b)add c)remove, d)mark a movie complete or e)Exist program: ")
        if movie=="a":
            print(todo)

        elif movie=="b":
            print(todo)
            adds= input("What movie do you want to add?: ")
            todo.append(adds)
            print(todo)

        elif movie=="c":
            print(todo)
            removes= input("Remove one movie or all movies?: ")
            if removes=="one":
                removes=input("What movie do you want to remove?: ")
                try:
                    todo.remove(removes)
                    print(todo)
                except:
                    print("item not in list")
            elif removes=="all":
                todo.clear()
                print(todo)
            else:
                print("Wrong input.Try again")
        elif movie=="d":
            print(todo)
            swap= input("What movie did you watch?: ")
            try:
                todo.remove(swap)
                done.append(swap)
                print("Done List: ")
                print(done)
            except:
                print("Item not in list")
        elif movie=="e":
            break


#Main
todo_list()

