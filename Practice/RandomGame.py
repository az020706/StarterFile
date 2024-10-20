import random
botnumber=random.randrange(1,101)
guess=0
while guess <10:
    guess+=1
    humannumber=int(input("Please enter a number(1 to 100):"))
    print("You've guessed",guess,"times")
    if botnumber < humannumber:
        print("This number has a higher value than the chosen number")
    elif botnumber > humannumber:
        print("This number has a lower value than the chosen number!")
    elif botnumber == humannumber:
        print("You've guessed it! Congrats!")
        win=True
        break
if win==False:
    print("The chosen number is ",botnumber)

