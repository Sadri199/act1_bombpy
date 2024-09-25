from bomb import *

###############Action Box###############

newUser()
loginRewards()
time.sleep(1)

print(f'\nIn your search for treasures you have ended in a room with a numerical keyboard on top of a mysterious machine and a door in front of it.\n')
time.sleep(0.5)

print('The machine activates and says:\n"Only a Leap Year will let you go forward, but many tries you have not, type carefully or nothing will remain of you": \n#########################################\n')
time.sleep(0.5)

actions()
    
###############Action Box###############


###############Bomb Box###############    

time.sleep(1)    
try: ##Everything wrapped in a Try.
    for counter in range (5,-1,-1):
        if counter == 5:
            print(f"\nYou have {counter} chances!")
            esc = leapList(int(input("""What number will you type? I inquire a year that it is a Leap Year: """)))
            if esc == 1: ##This was the only way i figured out to escape the Range.
                break
            else:
                counter -= 1
                print (f"I demand a Leap Year, now you have {counter} chances\n##################################")
        elif counter == 4:
            print(f"You have {counter} more chances!")
            esc = leapList(int(input("""What number will you type? I desire a year that it is a Leap Year: """)))
            if esc == 1:
                break
            else:
                counter -= 1
                print (f"Now you have {counter} chances\n##################################")
        elif counter == 3:
            print(f"You have {counter} more chances!")
            esc = leapList(int(input("""What number will you type? I ask only for a year that it is a Leap Year: """)))
            if esc == 1:
                break
            else:
                counter -= 1
                print (f"Bad answer, now you have {counter} chances\n##################################")
        elif counter == 2:
            print(f"Your chances are running lower, you only have {counter} chances left!")
            esc = leapList(int(input("""What number will you type? I demand for a year that it's a Leap Year: """)))
            if esc == 1:
                break
            else:
                counter -= 1
                print (f"You are walking in thin ice, now you have only {counter} chance\n##################################")
        elif counter == 1:
            print(f"Lady Luck is about to abandon you, you only have {counter} chance left!")
            esc = leapList(int(input("""What number will you type? I ask only for a year that it is a Leap Year: """)))
            if esc == 1:
                break
            else:    
                print("""Your destiny has been sealed, you've been left on your own, like a Rainbow in the Dark. Bomb activated. Exploding now. (⊙_⊙;)""")
                break
except Exception as error:
    print (error)
    print ("I only ask for numbers, nothing more, nothing else.\n")          
    
    
###############Bomb Box###############    
