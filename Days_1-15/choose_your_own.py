# Game set up and first choice
print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `"".o|o_.--"    ;o;____/______/______/__
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/___
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/
*******************************************************************************
''')

print("Welcome to Treasure Island.\nYour mission is to find the treasure.\n\n")

print("You're at a crossroad.")
crossroad = input("Where do you want to go?\n Type 'left' or 'right'.\n").lower()

if crossroad == "left":
    print("\nYou head down a dusty path toward a shimmering lake...")
    print("You've come to a lake.")
    lake = input("There is an island in the middle. \n\nType 'wait' to wait for a boat. Type 'swim' to swim across.\n").lower()
    
    if lake == "wait":
        print("\nYou take a well-earned break.")
        print("A small boat ferries you safely to the island.")
        
        door = input("You arrive at the island unharmed. \n\nThere is a house with 3 doors: one red, one yellow, one blue. \n\nWhich color do you choose?\n").lower()
        if door == "red":
            print("\nYou enter the room and there is a massive brainsucker dragon.\n\nIt sucks your brains out.\n\nYou are dead.\n\nGame Over!")
        elif door == "yellow":
            print("\nYou enter the room and see the treasure!\n\nWell done - you win!")
        else:
            print(r"""
                             ____________
                                 (`-..________....---''  ____..._.-`
                                  \\`._______.._,.---'''     ,'
                                  ; )`.      __..-'`-.      /
                                 / /     _.-' _,.;;._ `-._,'
                                / /   ,-' _.-'  //   ``--._``._
                              ,','_.-' ,-' _.- (( =-    -. `-._`-._____
                            ,;.''__..-'   _..--.\\.--'````--.._``-.`-._`.
             _          |\,' .-''        ```-'`---'`-...__,._  ``-.`-.`-.`.
  _     _.-,'(__)\__)\-'' `     ___  .          `     \      `--._
,',)---' /|)          `     `      ``-.   `     /     /     `     `-.
\_____--.  '`  `               __..-.  \     . (   < _...-----..._   `.
 \_,--..__. \\ .-`.\----'';``,..-.__ \  \      ,`_. `.,-'`--'`---''`.  )
           `.\`.\  `_.-..' ,'   _,-..'  /..,-''(, ,' ; ( _______`___..'__
                   ((,(,__(    ((,(,__,'  ``'-- `'`.(\  `.,..______   
                                                      ``--------..._``--.__

""")                                                      
            print("\nYou enter the room and are immediately crushed by a sea dragon.\n\nBad luck.\n\nGame over!")
    else:
        print("\nYou are attacked by a giant sharkworm. \n\nGame over!")

else:
    print("\nYou fell into a hole. Game Over.")
