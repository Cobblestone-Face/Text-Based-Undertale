"""
Unit 2
discountUndertale
Discount Undertale.
"""
import random
import undertale
random_number = 0
health = 10
floweyOneHp = 10
torielHp = 50
genocide = 0
pacifist = 0

print("Welcome to discount Undertale!")
random_number = random.randint(1, 4)

print()
print("You fell from a cliff and ")

if random_number == 4:
    print("died.")
else:
    print("landed safely on a flower bed. Suddenly, a flower with a face approaches you and asks to teach you how everything works.")
    print("--You hear a theme song play in the background.--")
    input("Howdy! I'm Flowey! Flowey the flower! (enter to continue) ")
    
    print()
    undertale.generateBattle("FLOWEY", health, floweyOneHp, "🌻")
    print()
    print("\"Down here, we share our love through..")
    print("friendliness pellets!\"")
    print("\"Try to get as many as you can!\"")
    pellets = input("Collect the pellets? (y/n) ")
    if pellets == "y":
        healthLoss = random.randint(2, 8)
        health = health - healthLoss
        print("-" + str(healthLoss) + " HP")
        print("\"You IDIOT.\"")
        print("\"Down here, it's kill or be killed.\"")
    
    if pellets == "n":
        print("\"You know what you're doing, don't you?\"")
    print("A creature comes by and kicks Flowey offscreen.")
    print("-- BATTLE OVER. --")
    print("(You already know all the stuff that happens so I'll just skip to the cool part)")
    leave = input("(Toriel) \"Are you really sure you want to leave?\" (y/n) ")
    if leave == "n":
        print("ok.")
    if leave == "y":
        print("\"Then show me you are prepared for the underground.\"")
        print("--You hear a theme song play in the background.--")
        while torielHp >= 1:
            undertale.generateBattle("TORIEL", health, torielHp, "🐐")
            damage = undertale.options(torielHp)
            torielHp = torielHp - damage
            damageTaken = undertale.opponentAtk(health, 1)
            health -= damageTaken
            if health <= 0:
                print()
                print("GAME OVER")
                print("This error exists to end the code, idk how else to do it")
                print()
                print(0 / 0) ## This creates an error to end the game. ##
        if torielHp <= 0:
            genocide += 1
        else:
                pacifist += 1
        if damage == "y":
            print()
        print("-- BATTLE OVER. --")
        print("You exited the ruins.")
        
## SANS UNDERTALE OMGOMGOMGOMGOMGOMGOMGOMGOngoango;gsergeurguergl ## 

        print("A strange figure walks slowly behind you.")
        print("\"D o n ' t  y o u  k n o w  h o w  t o  g r e e t  a  n e w  p a l ?\"")
        print("\"T u r n  a r o u n d  a n d  s h a k e  m y  h a n d .\"")
        print()
        print()
        print()
        print()
        print("ppppppfffffpbpbpbhbhhhhbhhhttttt")
        print("ITS SANS OMGMOMGOMGOMGOMOGMOGMigosnperogneugperubguerbguerbgpiergber sans undertale greigberiobgijeorabreigberpgpuierguerh")
