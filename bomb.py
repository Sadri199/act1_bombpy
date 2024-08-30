with open("leap_year.txt", "r") as year:
    correct = year.read()
    leapList = correct.replace("("," ").replace(")"," ").split(", ")
    leapList = list(map(int, leapList))

# print (type(leapList[0]))
# print (leapList[0])##Had to double check if i had the variable saved.##

def my_bomb ():
    counter = 5
    if counter == 5:
        print(f"You have {counter} more chances!")
        action = int(input("""What action will you type? I inquire a year between 1700 and 2200: """))
        if action in leapList:
            print (f"You made it, the bomb has been deactivated, the door opens and reveals a treasure, one which has been sealed for centuries, lost in time.\n#################################\nThis is your treasure, enjoy 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWxlbG00ODZvejV4a200bmU5aHdpZXVnYmc2dnBkNm56ajJ1em83YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/58QYcMsKz9xiSXtF9d/giphy.webp' ")
        else:
            print ("That's not a Leap Year")
            counter -= 1
            print (f"I demand a Leap Year, now you have {counter} chances\n##################################")
    if counter == 4:
        print(f"You have {counter} more chances!")
        action = int(input("""What action will you type? I inquire a year between 1700 and 2200: """))
        if action in leapList:
            print ("You made it, the bomb has been deactivated, the door opens and reveals a treasure, one which has been sealed for centuries, lost in time.\n#################################\nThis is your treasure, enjoy 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWxlbG00ODZvejV4a200bmU5aHdpZXVnYmc2dnBkNm56ajJ1em83YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/58QYcMsKz9xiSXtF9d/giphy.webp' ")
        else:
            print ("That's not a Leap Year")
            counter -= 1
            print (f"Now you have {counter} chances\n##################################")
    if counter == 3:
        print(f"You have {counter} more chances!")
        action = int(input("""What action will you type? I inquire a year between 1700 and 2200: """))
        if action in leapList:
            print ("You made it, the bomb has been deactivated, the door opens and reveals a treasure, one which has been sealed for centuries, lost in time.\n#################################\nThis is your treasure, enjoy 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWxlbG00ODZvejV4a200bmU5aHdpZXVnYmc2dnBkNm56ajJ1em83YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/58QYcMsKz9xiSXtF9d/giphy.webp' ")
        else:
            print ("That's not a Leap Year")
            counter -= 1
            print (f"Bad answer, now you have {counter} chances\n##################################")
    if counter == 2:
        print(f"Your chances are running lower, you only have {counter} chances left!")
        action = int(input("""What action will you type? I inquire a year between 1700 and 2200: """))
        if action in leapList:
            print ("You made it, the bomb has been deactivated, the door opens and reveals a treasure, one which has been sealed for centuries, lost in time.\n#################################\nThis is your treasure, enjoy 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWxlbG00ODZvejV4a200bmU5aHdpZXVnYmc2dnBkNm56ajJ1em83YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/58QYcMsKz9xiSXtF9d/giphy.webp' ")
        else:
            print ("That's not a Leap Year")
            counter -= 1
            print (f"Walking in thin ice, now you have only {counter} chance\n##################################")
    if counter == 1:
        print(f"Lady Luck is about to abandon you, you only have {counter} chance left!")
        action = int(input("""What action will you type? I inquire a year between 1700 and 2200: """))
        if action in leapList:
            print ("You made it, the bomb has been deactivated, the door opens and reveals a treasure, one which has been sealed for centuries, lost in time.\n#################################\nThis is your treasure, enjoy 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWxlbG00ODZvejV4a200bmU5aHdpZXVnYmc2dnBkNm56ajJ1em83YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/58QYcMsKz9xiSXtF9d/giphy.webp' ")
        else:
            print ("That's not a Leap Year")
            counter = 0
            print(f"Your destiny has been sealed, Bomb activated. Exploding now.")
            return  
     
print(f'In your search for treasures you have end up in a room with a numerical keyboard on top of a mysterious machine and a door in front of it.\nThe machine activates and says:\n"Only a Leap Year will let you go forward, but many tries you have not, type carefully or nothing will remain of you": \n#########################################')
my_bomb ()
