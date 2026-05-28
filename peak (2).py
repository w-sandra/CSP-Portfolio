#Sandra

import random
#Random 12 numbers
dataset=[]


def peak():
    for i in range(12):
        dataset.append(random.randint(0,12))
    print(dataset)
    if dataset[0] > dataset[1]:
            print(f"Peak detected: Value is {dataset[0]} at index 0")

    i=0

    for i in range(1,11):
        if i >= len(dataset):
            i= len(dataset)
        if dataset[i] > dataset[i-1]:
            print(f"Peak detected: Value is {dataset[i]} at index {i}")

            if dataset[i+1] > dataset[i] and dataset[i+1] > dataset[i+3]:
                print(f"Peak detected: Value is {dataset[i+1]} at index {i+1}")
        i= i+1

#Main
peak()

