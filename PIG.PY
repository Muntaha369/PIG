import random
while True:
    try:
     players = int(input("Enter the no. of players: "))
     if 2 <= players <= 4:
        break
     else:
        print("Players should be between 2-4")
    except ValueError:
       print("enter only numbers")    

def roll():
    print(random.randrange(1,12))
roll()
