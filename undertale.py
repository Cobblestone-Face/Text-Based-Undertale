"""
undertale

Description:
undertale battle mechanic thing idk
"""
import random

def generateBattle(opponent, hp, opHp, image):
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print(opponent)
    print()
    print("HP:")
    print("🟨" * opHp)
    print()
    print("      " + str(image))
    print("______________")
    print("|            |")
    print("|            |")
    print("|            |")
    print("|     ❤️     |")
    print("|            |")
    print("|            |")
    print("‾‾‾‾‾‾‾‾‾‾‾‾‾‾")
    print("HP: " + str(hp))
    print()

def options(opponentHealth):
    choice = input("|FIGHT (f)|  |ACT (a)|  |MERCY (m)|")
    if choice == "f":
        attack = random.randint(1,10)
        num = input("Pick a number between 1 and 10. ")
        damage = 10 - abs(attack - int(num))
        print("The number was " + str(attack) + ", you picked " + str(num) + ".")
        input("You did " + str(damage) + " damage. (enter to continue) ")
        return damage
    if choice == "a":
        print("Temporarily unavailable :(")
    if choice == "m":
        mercy = input("Spare (s) or Flee (f)?")
        if mercy == "f":
            print("You fled safely")
        if mercy == "s":
            print("you got a strike instead")
        end = "y"
        return end
def opponentAtk(hp, difficulty):
    print()
    print("(This dodge system is temporary until i can think of something better :P)")
    print("The attack is level " + str(difficulty) + " out of 5.")
    dodge = random.randint(1,10)
    luckIGuess = input("Pick a number between 1 and 10. ")
    damageTaken = abs(dodge - int(luckIGuess)) - difficulty
    print("The number was " + str(dodge) + ", you chose " + str(luckIGuess) + ", and the damage was increased by " + str(difficulty) + " from the difficulty level.")
    input("You took " + str(damageTaken) + " damage. (enter to continue) ")
    return damageTaken
    
