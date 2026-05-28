#Sandra
#Guest list

guests = ["Alice", "Bob", "Charlie", "David", "Eve",
"Frank", "Grace", "Heidi", "Ivan", "Judy",
"Kevin", "Liam", "Mallory", "Nia", "Oscar",
"Peggy", "Quinn", "Riley", "Sybil", "Trent",
"Uma", "Victor", "Walter", "Xander", "Yara",
"Zane", "Amari", "Blake", "Casey", "Dakota"]


friend= input("Please enter your friends name: ")

guests.append(friend)

vip= input("Name of VIP: ")

guests.insert(0, vip)

newfriend= input("Please enter your new friends name: ")

guests[4]= newfriend

number=len(guests)

#Main

print(guests)

print(number)

