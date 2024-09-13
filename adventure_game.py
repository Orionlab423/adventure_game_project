import time
import random
weapons = random.choice(['axe', 'bow', 'sword', 'dagger'])
enemy = random.choice(['dracula', 'skeletons', 'wicked fairie', 'dragon'])

def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)

def intro():
    print_pause("You find yourself standing in an open field, filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here," 
                "and has been terrifying the nearby village.")
    field()

def field():
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    player_entry = input("Enter 1 to knock on the door of the house.\n"
                         "Enter 2 to peer into the cave.\n"
                         "What would you like to do?\n"
                         "Enter 1 or 2\n")
    if player_entry == '1':
        house()
    elif player_entry == '2':
        cave()
    else:
        print_pause("Please enter 1 or 2\n")

def house():
    print_pause("You are about to knock on the door.")
    print_pause("You walk inside the house.")
    print_pause(f"The house is full of {enemy}")
    print_pause(f"Yikes!, This is the {enemy} house!")
    fight()

def fight():
    print_pause(f"The {enemy} start to attacks you!")
    fight = input("Would you like to (1) fight or (2) run away?\n")
    if fight == '1':
        print_pause(f"The {enemy} moves towards you to attack")
        print_pause(f"You grab new {weapons}")
        print_pause(f"The shiny {weapons} of Wudang in your hand as you make an attack.")
        print_pause(f"Attack! {enemy}")
        print_pause(f"The {enemy} is now destroyed.")
        print_pause(f"Victory!, You have defeated the {enemy}.")
        play_again()

    elif fight == '2':
        print_pause("You run back to the open field.")
        print_pause("Luckily, no enemies follow you.")
        play_again()
    else:
        print_pause("Unfortunately you unable to attack the enemy.")
        print_pause("You did your best.")
        print_pause("You have been defeated!")
        print_pause("Game Over!")
        play_again()

def cave():
    print_pause("This is an empty cave.")
    print_pause("You have been to this place before,"
                "and got the weapons from the wooden crates")
    print_pause(f"You have found magical {weapons} located inside the crate.")
    print_pause("Walk back out to the field.")
    field()

def play_again():
    choice = input("Would you like to play again? (y or n)").lower()
    if choice == 'y':
        print_pause("OK, Restarting the game...\n")
        play_game()
    elif choice == 'n':
        print_pause("Thanks for playing the game! Goodbye\n")
    else:
        print_pause("Please enter y or n.")

# Starts the game function
def play_game():
    intro()

play_game()