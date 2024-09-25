###################Version: 1.1###################
import random , datetime, time, sys

###########################Special Box###########################

# randList = [0, 1, 2, 3 ,4 ,5 ,6, 7, 8, 9] ##I'm gonna use this for something, but haven't decided yet.
# print(random.choice(randList))

date1 = datetime.date.today()

datename = date1.strftime("%A")

###########################Backpack Box###########################

inventory = []

###########################Backpack Box###########################

###########################Special Box###########################

###########################Class Box###########################

class Commands:
    
    def __init__(self):
        self.username = ""
        self.altEndings = {}
        self.pickedATM = False
    
    def look (self):
        print("You take a minute to understand the entire")
        time.sleep(1)
        print('''You are in a big room! 
              In the middle lies a "Mysterious Machine", with red lights and a numeric pad.
              In the wall in front of you there is a "Door", connected with cables to the Mysterious Machine.
              At your back there is a "Hole" through which you arrived here.
              In the wall to your left there is a "Wall Fountain", a "Liquid" flows from the top to the bottom.
              In the wall to your right there is an "ATM", it looks operational.
              
              In this room there are some other objects, here's what you see:
              a "Sack of Silica Gel", an "Empty Glass Jar", "$150".''')
        time.sleep(0.5)
        return
    
    def sleep (self):
        print(f"{myCommands.username} is feeling a bit sleepy, but don't want to sleep yet.\n")
        eepySleepy = input("You want to try to sleep? Yes or No: ").capitalize()
        if eepySleepy == "Yes":
            print("Well, time to sleep i guess?????????\n")
            time.sleep(5)
            print("Zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.\n\nYou slept a lot, so much that when you woke up the Mysterious Machine is deactivated, the Soor is open and there is nothing left in the room. You got nothing, but hey, at least you survived!\n")
            myCommands.altEndings.update({"Alternative Ending #1":"Ahhh so Eepy Sleepy"})
            sys.exit(f'''\nListen {myCommands.username}, i don't really know what you expected if you typed "Sleep" but yeah, you slept and you got Alternative ending "Ahhh so Eepy Sleepy"!\n
            Thank you for playing my game!^_^''')
        else:
            print("OK, returning to main menu.\n")
            
    def grab (self):
        grabbing = input('''From this room, what item do you want to Grab?
                You can go back to main menu by typing "Back".
                If you don't know what items are here, please go back and use "Look": 
                ''').capitalize()
        if grabbing == "Back":
            print("Going back to main menu.")
            return
        elif grabbing == "Mysterious Machine":
            print("The Machine is bolted to the ground, you can't pick it up!\n")
        elif grabbing == "Door":
            print("How are you going to pick a Door?\n")
        elif grabbing == "Wall Fountain":
            print("No, you cannot pick a fountain, i'm sorry.\n")
        elif grabbing == "Atm":
            if myCommands.pickedATM == False:
                print("You picked the ATM! You store it in your Backpack.")
                inventory.append("ATM") 
                myCommands.pickedATM = True
                return myCommands.pickedATM
            else:
                print("You already have the ATM in your Backpack!!")
        elif grabbing == "Liquid":
            print("You tried to grab the liquid, but with your bare hands it's impossible, it falls from your hands whenever you try.\n") #Add an IF to check if you have Jar, copy from ATM.
        elif grabbing == "Sack of Silica Gel":
            print("You picked the Sack of Silica Gel! You store it in your Backpack.")
            inventory.append("Sack of Silica Gel") #Add an IF to check if you have in inventory, copy from ATM
        elif grabbing == "Empty Glass Jar":
            print("You picked the Empty Glass Jar! You store it in your Backpack.")
            inventory.append("Empty Glass Jar") #Add an IF to check if you have in inventory, copy from ATM
        elif grabbing == "$150":
            print("You picked $150! You store it in your Backpack.")
            inventory.append("$150") #Add an IF to check if you have in inventory, copy from ATM
                    
            

###########################Class Box###########################

###########################Function Box###########################

def newUser ():
    newYou = 0
    if newYou == 0:
        saveUser = input("Hello, it looks like you are a new player. Please enter your name, this will be saved to personalize your experience: ")
        myCommands.username = saveUser
        print (f"\n{myCommands.username}! A pleasure to meet you, enjoy your stay here!\n")
        newYou = 1 #This is to change the initial message.
        return newYou
    elif newYou == 1:
        print(f"Welcome back {myCommands.username}!\n")

def leapList (year): ##The leap year is now it's own function.
    token = 0
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        time.sleep(1)
        print (f"\nWow {myCommands.username}, you made it. The bomb has been deactivated, the door in front of you opens and reveals a treasure, one which has been sealed for centuries, lost in time.")
        
        print (f"\n#################################\n\n⸜(⸝⸝⸝´꒳`⸝⸝⸝)⸝ This is your treasure, {myCommands.username}! Enjoy 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWxlbG00ODZvejV4a200bmU5aHdpZXVnYmc2dnBkNm56ajJ1em83YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/58QYcMsKz9xiSXtF9d/giphy.webp' ⸜(⸝⸝⸝´꒳`⸝⸝⸝)⸝")
        
        sys.exit(f"\nThank you so much {myCommands.username} for playing my game!")
    else:
        time.sleep(1)
        print ("That's not a Leap Year")
        return token



def loginRewards ():
    if datename == "Monday":
        print(f'\033[1;37;40m Today is {datename}! Your reward is a "Bottle of Hornets!"\n༼ つ ◕_◕ ༽つ') #Color White
        inventory.append("Bottle of Hornets!")
        return
    elif datename == "Tuesday":
        print(f'\033[1;33m Today is {datename}! Your reward is a "Banana Phone!"\n༼ つ ◕_◕ ༽つ') #Color Yellow
        inventory.append("Banana Phone!")
        return
    elif datename == "Wednesday":
        print(f'\033[1;32m Today is {datename}! Your reward is a "Lightbulb with a Flower!"\n༼ つ ◕_◕ ༽つ') #Color Green
        inventory.append("Lightbulb with a Flower!")
        return
    elif datename == "Thursday":
        print(f'\033[1;31m Today is {datename}! Your reward is a "Claymore!"\n༼ つ ◕_◕ ༽つ') #Color Red
        inventory.append("Claymore!")
        return
    elif datename == "Friday":
        print(f'\033[1;36m Today is {datename}! Your reward is a "Fax Machine!"\n༼ つ ◕_◕ ༽つ') #Color Cyan
        inventory.append("Fax Machine!")
        return
    elif datename == "Saturday":
        print(f'\033[1;34m Today is {datename}! Your reward is a "Blue Sea Dragon!"\n༼ つ ◕_◕ ༽つ') #Color Blue
        inventory.append("Blue Sea Dragon!")
        return
    elif datename == "Sunday":
        print(f'\033[1;35m Today is {datename}! Your reward is a "SU-47"\n༼ つ ◕_◕ ༽つ') #Color Purple
        inventory.append("SU-47")
        return

myCommands = Commands()

def actions ():
    while True:
        actMenu = input(f"""What will you do, {myCommands.username}?
                        
    Available actions: Look, Type, Sleep, Grab, Eat, Drink, Inventory, Exit: \n""").capitalize()
        if actMenu == "Look":
            myCommands.look()
            continue
        elif actMenu == "Type":
            break
        elif actMenu == "Sleep":
            myCommands.sleep()
            continue
        elif actMenu == "Grab":
            myCommands.grab()
            continue
        elif actMenu == "Eat":
            ...
        elif actMenu == "Drink":
            ...    
        elif actMenu == "Quack":
            ...
        elif actMenu == "Inventory":
            print(f"This is your Inventory: {inventory}\n")
            time.sleep(0.5)
            continue
        elif actMenu == "Exit": 
            sys.exit(f"\nThank you so much {myCommands.username} for playing my game!")
        else:
            print(f"\nSorry, i couldn't understand you {myCommands.username}, please choose one of the available actions.\n")   
###########################Function Box###########################

