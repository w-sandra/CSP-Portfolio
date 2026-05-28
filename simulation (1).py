#Sandra
#100 Loops

tortoise_wins = 0
hare_wins = 0


for i in range(100):
    finish_line=50              #Finish Line
    tortoise_pos=0              #Starting Position
    hare_pos=0                  #Starting position

    is_hare_asleep= False       #Hare Awake

    import random

    print("------Start------")
    while tortoise_pos < finish_line and hare_pos < finish_line:
        tortoise_pos= tortoise_pos + random.randint(1,3)
        is_hare_asleep= int(random.randint(1,100))
        if is_hare_asleep<=80:
            is_hare_asleep=True
        else:
            is_hare_asleep=False
        if is_hare_asleep== False:
            hare_pos= hare_pos + random.randint(1,10)
        print(f"Tortoise: {tortoise_pos} | Hare: {hare_pos}")

    if tortoise_pos >= finish_line:
        print("🐢 The Tortoise wins!")
        tortoise_wins =tortoise_wins + 1

    else:
        print("🐇 The Hare wins!")
        hare_wins = hare_wins + 1
print(f"Hare Won: {hare_wins} Tortoise Won: {tortoise_wins}")
