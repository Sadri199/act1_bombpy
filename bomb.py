###################Version: 2.0###################
import random, datetime, time, sys, string

###########################Special Box###########################

randList = [1, 2, 3, 4, 5, 6] ##I'm gonna use this for something, but haven't decided yet.

date1 = datetime.date.today()

datename = date1.strftime("%A")

inventory = []

###########################Special Box###########################

###########################Class Box###########################

class Commands:
    
    def __init__(self):
        self.username = ""
        self.Endings = {}
        self.pickedATM = False
        self.pickedSack = False
        self.pickedJar = False
        self.picked150 = False
        self.jarLiquid = False
        self.quackCounter = 0
    
    def look (self): #Working
        print("You take a minute to understand the entire")
        time.sleep(1)
        print('''You are in a big room! 
In the middle lies a "Mysterious Machine", with red lights and a numeric pad.
In the wall in front of you there is a "Door", connected with cables to the Mysterious Machine.
At your back there is a "Hole" through which you arrived here.
In the wall to your left there is a "Wall Fountain", a "Liquid" flows from the top to the bottom.
In the wall to your right there is an "ATM" that's also a Vending Machine, it looks operational.

In this room there are some other objects, here's what you see:
a "Sack of Silica Gel", an "Empty Glass Jar", "$150".''') #Only a print.
        time.sleep(0.5)
        return
    
    def sleep (self): #Working
        print(f"{self.username} is feeling a bit sleepy, but don't want to sleep yet.\n")
        eepySleepy = input("You want to try to sleep? Yes or No: ").capitalize()
        if eepySleepy == "Yes":
            print("Well, time to sleep i guess?????????\n")
            time.sleep(5)
            print("Zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz.\n\nYou slept a lot, so much that when you woke up the Mysterious Machine is deactivated, the Soor is open and there is nothing left in the room. You got nothing, but hey, at least you survived!\n")
            time.sleep(1)
            self.Endings.update({"Alternative Ending #1":"Ahhh so Eepy Sleepy"})
            sys.exit(f'''\nListen {self.username}, i don't really know what you expected if you typed "Sleep" but yeah, you slept.
Thank you for playing my game!^_^
{self.Endings} Have you heard a Duck?''') #Some endings need flavor text to make players find the rest of the endings.
        else:
            print("OK, returning to main menu.\n")
            
    def grab (self): #Working
        try:
            grabbing = input('''From this room, what item do you want to Grab?
You can go back to main menu by typing "Back".
If you don't know what items are here, please go back and use "Look": 

''').upper() #I prefer an Upper so it doesn't matter how someone types, it gets formatted correctly.
            if grabbing == "BACK":
                print("Going back to main menu.")
                return
            elif grabbing == "MYSTERIOUS MACHINE":
                print("The Machine is bolted to the ground, you can't pick it up!\n")
            elif grabbing == "DOOR":
                print("How are you going to pick a Door?\n")
            elif grabbing == "WALL FOUNTAIN":
                print("No, you cannot pick a fountain, i'm sorry.\n")
            elif grabbing == "ATM":
                if self.pickedATM == False:
                    print("You picked the ATM! You store it in your Backpack.")
                    inventory.append("ATM") 
                    self.pickedATM = True
                    return self.pickedATM
                else: #Give the ability to return it to the ground
                    print("You already have the ATM in your Backpack!!")
            elif grabbing == "LIQUID":
                if self.pickedJar == True:
                    print("You filled the Jar with this Liquid! You store it in your Backpack.")
                    inventory.remove("Empty Glass Jar")
                    inventory.append("Jar with Liquid")
                    self.jarLiquid = True
                    return self.jarLiquid 
                else:
                    print("You tried to grab the liquid, but with your bare hands it's impossible, it falls from your hands whenever you try.\n")
            elif grabbing == "SACK OF SILICA GEL":
                if self.pickedSack == False:
                    print("You picked the Sack of Silica Gel! You store it in your Backpack.")
                    inventory.append("Sack of Silica Gel") 
                    self.pickedSack = True
                    return self.pickedSack
                else:
                    print("You already have the Sack of Silica Gel in your Backpack!!")
            elif grabbing == "EMPTY GLASS JAR":
                if self.pickedJar == False:
                    print("You picked the Empty Glass Jar! You store it in your Backpack.")
                    inventory.append("Empty Glass Jar")
                    self.pickedJar = True
                    return self.pickedJar
                else:
                    print("You already have the Empty Glass Jar in your Backpack!!")
            elif grabbing == "$150":
                if self.picked150 == False:
                    print("You picked the $150! You store it in your Backpack.")
                    inventory.append("$150")
                    self.picked150 = True
                    return self.picked150
                else:
                    print("You already have the $150 in your Backpack!!")
        except Exception:
            print("You can only add stuff to your backpack that you can see. Remember to look!\nGoing back to main menu.\n")
    
    def eat (self): #Working
        if "Sack of Silica Gel" in inventory:
            eating = input("What do you want to eat? \n").upper()
            if eating == "SACK OF SILICA GEL":
                uhhhh = input('Uh, it says "Not Edible", are you still going to eat it? Yes or No: ').capitalize()
                if uhhhh == "Yes":
                    print("\nHere we go!\n...")
                    time.sleep(8)
                    print("All those people telling you this shouldn't be done were wrong, now you can see through the veil of reality, trascend this existence and become a god!\n")
                    self.Endings.update({"Bad Ending #3":"No escape from the Matrix"})
                    time.sleep(1)
                    sys.exit(f'''Just kidding, you died. Sorry.
                    Thank you for playing my game tho!^_^
                    {self.Endings}''')
                else:
                    print("That was close, returning to main menu.\n")
                    return    
            else:
                print("Sorry, that isn't edible.")
                return
        else:
            print("You don't have any object that can be eaten.\n")
            return
                
    def drink (self):
        if "Jar with Liquid" in inventory:
            drinking = input("What do you want to drink? \n").upper()
            if drinking == "JAR WITH LIQUID":
                uhhhh = input('Uh, you really have no idea what this liquid is, are you still going to drink it? Yes or No: ').capitalize()
                if uhhhh == "Yes":
                    print("\nHere we go!\n...")
                    time.sleep(5)
                    print("The liquid was no other than Mug Root Beer™, that's right, i want to thank my sponsor Mug Root Beer™ for helping with all the costs of this game!\n")
                    self.Endings.update({"Mug Ending #1":"I sold my soul for $1"})
                    time.sleep(1)
                    sys.exit(f'''I don't know how it taste, it isn't available in my country. Also they aren't my sponsors, but if they want to give me money they can get in touch.
                    Thank you for playing my game tho!^_^
                    {self.Endings}''')
                else:
                    print("That was close, returning to main menu.\n")
                    return    
            else:
                print("Sorry, that isn't drinkable.")
                return
        else:
            print("You don't have any object that can be drunk.\n")
            return
    
    def use (self):
        if "$150" in inventory:
            byeBucks = input("You can use the money in the ATM. Want to do that? Yes or No: ").capitalize()
            if byeBucks == "Yes":
                inventory.remove("$150")
                print("You put the $150 in the ATM.\nProcessing...\n")
                time.sleep(1)
                inventory.append("Six Sided Dice")
                print('You got a "Six Sided Dice"!\n')
            else:
                print("Returning to main menu\n")    
        elif "ATM" in inventory:
            byeATM = input("The ATM looks breakable, would you like to throw it? Yes or No: ").capitalize()
            if byeATM == "Yes":
                inventory.remove("ATM")
                print('You smashed the ATM into the ground with all your strength!\nBetween all the wreckage you find "Magical Voucher"!')
                inventory.append("Magical Voucher")
            else:
                print("Returning to main menu\n")    
        elif "Six Sided Dice" in inventory:
            byeDice = input("This dice looks weird, would you like to use it? Yes or No: ").capitalize()
            if byeDice == "Yes":
                inventory.remove("Six Sided Dice")
                diceUp = dice() #Some sides end the game, others let you continue with a new item in your Inventory.
                print('Something strange is about to happen!\n')
                time.sleep(2)
                if diceUp == 1: #Floppy with Norton
                    ...
                elif diceUp == 2: #Absolutely nothing, scammed
                    print("You got nothing, congratulations???\n")
                elif diceUp == 3: #Golden ping pong racket??
                    ...
                elif diceUp == 4: #Cube with 70k lines of code, ending
                    print("A magical cube appears out of nowhere, it starts spinning and suddenly numbers appear on your screen?\n")
                    for n in range(70000):
                        print(f"Wow, you got a {n}!")
                elif diceUp == 5: #ATM and $150 returned to Inventory, so you can loop the dice.
                    ...        
                elif diceUp == 6: #Hell, ending
                    print(f"You go to Hell.")
            else:
                print("Returning to main menu\n")                
        elif "Magical Voucher" in inventory:
            byeATM = input('"This voucher lets you exchange a login reward for any other reward"\nYou have no idea what this means, would you like to use it? Yes or No: ').capitalize()
            if byeATM == "Yes":#I need to think how to pull this off.
                inventory.remove("Magical Voucher")
                print('...')
                inventory.append("Magical Voucher")
            else:
                print("Returning to main menu\n")
        else:
            print("None of the items you currently have can be used right now.\n")        
        
    def quack (self): #Working
        print("You quacked really loud!")
        print("...\n")
        time.sleep(1)
        self.quackCounter += 1
        if self.quackCounter == 5:
            time.sleep(2)
            print(f"Out of nowhere, thousands of ducks appear, they quack, they quack a lot.\nThey take you with them to their duck village.\nNow you live with them, i guess?")
            self.Endings.update({"Alternative Ending #2":"Duck tales, oooo ooooo!"})
            sys.exit(f'''\n{self.username}, the bomb is intact, you didn't get the treasure, but hey, the ducks are nice??\nCan you get out of here though?\n
            Thank you for playing my game!^_^
            {self.Endings}''')
        else:
            print("Hmmmmmmmm, nothing seems to happen. Going back to main menu.\n")                            
                      
    def admGive (self): #Admin command to add any object to Inventory, even ones that don´t exist.
        admCheck = input("STOP RIGHT THERE! ACCESS TO THIS PART IS FORBIDDEN (⌐■_■) .\nONLY THOSE WHO HAVE THE SECRET PASSPHRASE MY CONTINUE.\nENTER IT NOW IF YOU KNOW IT: ")
        if  admCheck == "GleebyDeeby":
            admAppend = input("\nAcces code granted, add any item you want to the Inventory: ")
            capiPhrase = formatter(admAppend)
            inventory.append(capiPhrase)
            print("Item succesfully added to Inventory.")
        else:
            print("Go back where you came.\n")    
                
###########################Class Box###########################

###########################Function Box###########################

def formatter (text): #Lazy way to bypass players not using the correct uppercase for Inventory objects.
    capWordFormat = string.capwords(text)
    return capWordFormat

def dice ():
    face = random.choice(randList)
    print(f"The dice landed in {face}.")
    return face

def newUser (): #50/50
    newYou = 0
    if newYou == 0:
        saveUser = input("Hello, it looks like you are a new player. Please enter your name, this will be saved to personalize your experience: ")
        myCommands.username = saveUser
        print (f"\n{myCommands.username}! A pleasure to meet you, enjoy your stay here!\n")
        newYou = 1 #This is to change the initial message, i haven´t decided how to save this information.
        return newYou
    elif newYou == 1:
        print(f"Welcome back {myCommands.username}!\n")
        
def intro ():
    print(f'\nIn your search for treasures you have ended in a room with a numerical keyboard on top of a mysterious machine and a door in front of it.\n')
    time.sleep(0.5)

    print('The machine activates and says:\n"Only a Leap Year will let you go forward, but many tries you have not, type carefully or nothing will remain of you": \n#########################################\n')
    time.sleep(0.5)

def leapList (year): ##The leap year is now its own function.
    if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
        time.sleep(1)
        print (f"\nWow {myCommands.username}, you made it. The bomb has been deactivated, the door in front of you opens and reveals a treasure, one which has been sealed for centuries, lost in time.")
        
        print (f"\n#################################\n\n⸜(⸝⸝⸝´꒳`⸝⸝⸝)⸝ This is your treasure, {myCommands.username}! Enjoy 'https://media1.giphy.com/media/v1.Y2lkPTc5MGI3NjExbWxlbG00ODZvejV4a200bmU5aHdpZXVnYmc2dnBkNm56ajJ1em83YiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/58QYcMsKz9xiSXtF9d/giphy.webp' ⸜(⸝⸝⸝´꒳`⸝⸝⸝)⸝")
        myCommands.Endings.update({"Real Ending #1":"Wow! You defused the bomb. Wow you da best, woooooo, woooooo! Bomb!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"})
        sys.exit(f"\nThank you so much {myCommands.username} for playing my game!\n {myCommands.Endings}")
    else:
        time.sleep(1)
        print ("That's not a Leap Year")
        return

def loginRewards (): #Working
    if datename == "Monday":
        print(f'\033[1;37;40m Today is {datename}! Your reward is a "Bottle of Hornets!"\n༼ つ ◕_◕ ༽つ') #Color White
        inventory.append("Bottle Of Hornets!")
        return
    elif datename == "Tuesday":
        print(f'\033[1;33m Today is {datename}! Your reward is a "Banana Phone!"\n༼ つ ◕_◕ ༽つ') #Color Yellow
        inventory.append("Banana Phone!")
        return
    elif datename == "Wednesday":
        print(f'\033[1;32m Today is {datename}! Your reward is a "Lightbulb with a Flower!"\n༼ つ ◕_◕ ༽つ') #Color Green
        inventory.append("Lightbulb With A Flower!")
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
        print(f'\033[1;35m Today is {datename}! Your reward is a "Armored Core"\n༼ つ ◕_◕ ༽つ') #Color Purple
        inventory.append("Armored Core")
        return

myCommands = Commands() #Instance for the class.

def actions (): #Working
    while True:
        actMenu = input(f"""What will you do, {myCommands.username}\n?
Available actions: Look, Type, Sleep, Grab, Eat, Drink, Use, Inventory, Exit: \n""").capitalize()
        if actMenu == "Look":
            myCommands.look()
            continue
        elif actMenu == "Type":
            mainBomb()
            break
        elif actMenu == "Sleep":
            myCommands.sleep()
            continue
        elif actMenu == "Grab":
            myCommands.grab()
            continue
        elif actMenu == "Eat":
            myCommands.eat()
            continue
        elif actMenu == "Drink":
            myCommands.drink()
            continue    
        elif actMenu == "Quack":
            myCommands.quack()
            continue
        elif actMenu == "Use":
            myCommands.use()
            continue
        elif actMenu == "Give":
            myCommands.admGive()
            continue
        elif actMenu == "Inventory":
            print(f"This is your Inventory: {inventory}\n")
            time.sleep(0.5)
            continue
        elif actMenu == "Exit":
            myCommands.Endings.update({"Bad Ending #2":"You let the bomb alone :("}) 
            sys.exit(f"\nThank you so much {myCommands.username} for playing my game!\n{myCommands.Endings}")
        else:
            print(f"\nSorry, i couldn't understand you {myCommands.username}, please choose one of the available actions.\n")   
            
def mainBomb (): #Working
       for counter in range (5,-1,-1):
        try:    
            if counter == 5:
                print(f"\nYou have {counter} chances!")
                leapList(int(input("""What number will you type? I inquire a year that it is a Leap Year: """)))
                counter -= 1
                print (f"I demand a Leap Year, now you have {counter} chances\n##################################")
            elif counter == 4:
                print(f"You have {counter} more chances!\n")
                leapList(int(input("""What number will you type? I desire a year that it is a Leap Year: """)))
                counter -= 1
                print (f"Now you have {counter} chances\n##################################")
            elif counter == 3:
                print(f"You have {counter} more chances!\n")
                leapList(int(input("""What number will you type? I ask only for a year that it is a Leap Year: """)))
                counter -= 1
                print (f"Bad answer, now you have {counter} chances\n##################################")
            elif counter == 2:
                print(f"Your chances are running lower, you only have {counter} chances left!")
                leapList(int(input("""What number will you type? I demand for a year that it's a Leap Year: """)))
                counter -= 1
                print (f"You are walking in thin ice, now you have only {counter} chance\n##################################")
            elif counter == 1:
                counter -= 1
                print(f"Lady Luck is about to abandon you, you only have {counter} chance left!")
                leapList(int(input("""What number will you type? I ask only for a year that it is a Leap Year: """)))    
                myCommands.Endings.update({"Bad Ending #1":"You are dead, dead, dead."})
                sys.exit(f"""Your destiny has been sealed, you've been left on your own, like a Rainbow in the Dark. Bomb activated. Exploding now. (⊙_⊙;)
                {myCommands.Endings} Leap years appear every 4 years or something, i don't know man.""")                
        except Exception:
            myCommands.Endings.update({"Error Ending #1":"Man, why don't you want to type an Integer?"})
            print (f"I only ask for numbers, nothing more, nothing else.\n")
            if counter == 0:
                print(f"Game is closing, you run out of chances.\n{myCommands.Endings}")         
                   
###########################Function Box###########################

