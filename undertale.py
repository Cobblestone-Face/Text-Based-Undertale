"""
undertale

Description:
undertale battle mechanic thing idk
"""
import random
import sys

def generateBattle(opponent, hp, opHp, image):
    print("\n" * 100) # clears the screen
    print(opponent) # shows your opponent's name
    print()
    print("HP:") 
    print("🟨" * opHp) # displays opponent hp in a visually pleasing way
    print()
    print("      " + str(image)) # emoji for opponent
    print("______________")
    print("|            |") # udnetrale
    print("|            |")
    print("|            |")
    print("|     ❤️     |")
    print("|            |")
    print("|            |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("HP: " + str(hp)) # displays user hp
    print()

def options(opponentHealth):
    choice = input("|FIGHT (f)|  |ACT (a)|  |MERCY (m)| ") # options
    if choice == "f": # fight
        attack = random.randint(1,10)
        num = int(input("Pick a number between 1 and 10. "))
        if num > 10:
            num = 10
        if num < 1:
            num = 1
        damage = 10 - abs(attack - int(num))
        print("The number was " + str(attack) + ", you picked " + str(num) + ".")
        input("You did " + str(damage) + " damage. (enter to continue) ")
    
        return damage
    if choice == "a": # act
        print("Temporarily unavailable :(")
        sys.exit()
    if choice == "m": # mercy
        mercy = input("Spare (s) or Flee (f)? ")
        if mercy == "f":
            print("You fled safely")
        if mercy == "s":
            print("you got a strike instead") # bowling joke lmao
        end = "y"
        return end
def opponentAtk(hp, difficulty):
    print()
    print("(This dodge system is temporary until i can think of something better :P)") # because im stupid

    if difficulty == 1:
        comment = "really easy."
    if difficulty == 2:
        comment = "easy."
    if difficulty == 3:
        comment = "average."
    if difficulty == 4:
        comment = "difficult."
    if difficulty == 5:
        comment = "really hard!"

    print("The attack is level " + str(difficulty) + " out of 5. This attack is " + comment)
    dodge = random.randint(1,10) # generates a random number the player needs to guess
    luckIGuess = int(input("Pick a number between 1 and 10. ")) # player guesses the number
    if luckIGuess > 10:
        luckIGuess = 10
    if luckIGuess < 1:
        luckIGuess = 1
    damageTaken = abs(dodge - int(luckIGuess)) + difficulty - 1 # math :(
    print("The number was " + str(dodge) + ", you chose " + str(luckIGuess) + ", and the damage was increased by " + str(difficulty - 1) + " from the difficulty level.")
    input("You took " + str(damageTaken) + " damage. (enter to continue) ")
    return damageTaken # returns how much damage you took to calculate in the main program
    
