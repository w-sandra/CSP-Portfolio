#Sandra


finish_line=50              #Finish Line
tortoise_pos=0              #Starting Position
hare_pos=0                  #Starting position

is_hare_asleep= False       #Hare Awake

import random

print("------Start------")
while tortoise_pos < finish_line and hare_pos < finish_line:
    tortoise_pos= tortoise_pos + random.randint(1,3)
    is_hare_asleep= int(random.randint(1,3))
    if is_hare_asleep==1:
        is_hare_asleep=True
    else:
        is_hare_asleep=False
    if is_hare_asleep== False:
        hare_pos= hare_pos + random.randint(1,10)
    print(f"Tortoise: {tortoise_pos} | Hare: {hare_pos}")

if tortoise_pos >= finish_line:
    print("🐢 The Tortoise wins!")
else:
    print("🐇 The Hare wins!")

