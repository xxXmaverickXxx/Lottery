#!/bin/python3

import random
from termcolor import cprint
replypos = ["Y" , "y" , "Yes" , "yes", "YES" , "YEs ", "YeS", "yEs", "yES" , "Yeah", "Yah", "Yessir",]
replyneg = ["N" , "n" , "No" , "Nope", "no " , "Nah" , "nah" , "nO" , "NAh"]
Numbers = []
UserList = []
instructions = "We've all claimed to have good luck at some point in our lives, this game puts that claim to the ultimate test. Wanna see if you're truly lucky? Then try this game. Based on the amount of money put in, two random numbes will be generated within a range of numbers. " + "\n" + "Your goal as the player is to guess which two numbers within that range were selected. Good luck, you'll need it. ;) " + "\n" + "\n" + " - Maverick"
packages = [30, 50 , 70 , 80 , 100]
a = 0
print("\n")
print("           **         **      ***********    **          **********   ***********     **             **    **********     ")
print("          **         **      **             **          **           **       **     ****        ** **    **              ")
print("         **         **      **             **          **           **       **     **   **    **  **    **               ")
print("        **    **   **      **********     **          **           **       **     **    **  **   **    **********        ")
print("       **  **  ** **      **             **          **           **       **     **       **    **    **                 ")
print("      ****     ****      **             **          **           **       **     **             **    **                  ")
print("     **         **      ************   **********  ***********  ************    **             **    ************         ")
print("                                                                                                                             ")
print("                                  *************      ************                                                          ")
print("                                       **           **        **                                                          ")
print("                                      **           **        **                                                            ")
print("                                     **           **        **                                ")
print("                                    **           **        **                                 ")
print("                                   **           ************                             ")
print("                                                                                          ")
print("                      ***************    **         **      ***********                                 ")
print("                            **          **         **      **                                 ")
print("                           **          **         **      **                                  ")
print("                          **          *************      ***********                        ")
print("                         **          **         **      **                                    ")
print("                        **          **         **      **                                     ")
print("                       **          **         **      ************                             ")
print("                                                                                     ")
print("                                                                                     ")
print("                                                                                     ")
print("         **             *************     ***************    **************     ***********    ************    **          **       ")
print("        **             **         **           **                 **           **             **        **     **        **         ")
print("       **             **         **           **                 **           **             **        **      **      **           ")
print("      **             **         **           **                 **           ***********    **        **       ********             ")
print("     **             **         **           **                 **           **             ***********           **                 ")
print("    **             **         **           **                 **           **             **        **          **                  ")
print("   ************   *************           **                 **           ***********    **          **        **                    ")
print("                                                                                                                                     ")
print("                                                                                                                                     ")
print("                                                                                                                                     ")
name = input("Your Name Please :   ")
print("Welcome " + name + " ")
print("\n")

for q in range(1):
    instruct = input("For instructions, Type 'Y'. To Skip Instructions Press 'Enter'  :")
    if instruct == "Y":
        print(instructions)
        break
    else:
        break

for x in range(10):
    cprint("Please make sure your money is sufficient for one try, CHANGE NO DEY O!!", attrs=['bold'])
    print("\n")
    print("\n")
    cprint("Seriously tho, Just make sure the amount of money you put in is not an odd number but is an even one", attrs=['bold'])
    print("\n")
    
    cprint(" $2 = 1 try", attrs=['bold'])
    
    cprint("Available Packages are $50, $60, $70, $100", attrs=['bold'])
    print("\n")
    print("\n")
    money = int(input("Insert money to start : $"))
    cut = 60 / 100
    if money in packages:
        print("\n")
        print("You have enough money to play")
        tries = int(money / 2)
        Score = money * 2
        Score2 = money * 2
        showhint = int(cut * tries)
        for i in range(2):
            num = random.randint(1, money)
            Numbers.append(num)
        #print(Numbers)
        for  i in range(tries):
            a += 1
            for j in range(2):
                user = int(input("Pick a number from 1 - " + str(money) + ":   "))
                UserList.append(user)
            
            
            compare1 = any(item in UserList for item in Numbers)
            compare2 = all(item in UserList for item in Numbers) 
            
            if compare1 == True:
                print("\n")
                print("===================")
                print(" A number is there ")
                print("===================")
                print("     Try Again     ")
                print("===================")
                print("\n")
                UserList.pop(0)
                UserList.pop(0)
                Score -= 1
            else:
                Score -= 0.5
                print("\n")
                print("===================")
                print("     Try Again     ")
                print("===================")
                print("\n")
                UserList.pop(0)
                UserList.pop(0)
        
                for l in range(1):
                    if a == showhint: 
                        hint = input("Do you want a hint? It will cost you some points from your score (y/n)  ")
                        if hint in replyneg:
                            print("Okay, Carry on then.")
                            break
                        if hint in replypos:
                            print(random.choice(Numbers))
                            Score -= 6
                            break
                        
            if compare2 == True:
                print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
                print("         Congratulations " + name + "!!!, You Won!!!!!")
                print("/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/")
                break


        print(Numbers , "Your score is " + str(Score) + "/" + str(Score2) )
        Total_Score = Score / Score2
        Prize = int(Total_Score * 10000)
        print("You won $" + str(Prize))
        break
    else:
        print("\n")
        print("========================================")
        print("    You Are Too Broke To Play Bruh")
        print("========================================")
        print("  Come Back When You Have More Money")
        print("========================================")
        print("\n")
        print("\n")
        print("\n")
