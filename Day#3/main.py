print("""                                                                 #####
                                                                #######
                   #                                            ##O#O##
  ######          ###                                           #VVVVV#
    ##             #                                          ##  VVV  ##
    ##         ###    ### ####   ###    ###  ##### #####     #          ##
    ##        #  ##    ###    ##  ##     ##    ##   ##      #            ##
    ##       #   ##    ##     ##  ##     ##      ###        #            ###
    ##          ###    ##     ##  ##     ##      ###       QQ#           ##Q
    ##       # ###     ##     ##  ##     ##     ## ##    QQQQQQ#       #QQQQQQ
    ##      ## ### #   ##     ##  ###   ###    ##   ##   QQQQQQQ#     #QQQQQQQ
  ############  ###   ####   ####   #### ### ##### #####   QQQQQ#######QQQQQ\n""")

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.\n")

direction = input("left or right?")

if direction != 'left':
    print("Fall into a hole.");
    print("Game Over.")
    exit()

action = input("swim or wait?")

if action != "wait":
    print("Attacked by trout.")
    print("Game Over.")
    exit()

door = input("Which door? Choose one: red, blue, yellow")

if door == "red":
    print("Burned by fire")
    print("Game Over.")
elif door == "blue":
    print("Eaten by beasts.")
    print("Game Over.")
elif door == "yellow":
    print("You Win!")
else:
    print("Game Over.")