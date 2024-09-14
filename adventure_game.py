import time
import random
weapons = random.choice(['axe', 'bow', 'sword', 'dagger'])
enemy = random.choice(['dracula', 'skeletons', 'wicked fairie', 'dragon'])


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def intro():
    print_pause("You find yourself standing in an open field,"
                "filled with grass and yellow wildflowers.")
    print_pause(f"Rumor has it that a {enemy} is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    field()


def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    print_pause("What would you like to do?")
    while True:
        player = input("(Enter 1 or 2)\n")
        if player == '1':
            house()
            break
        elif player == '2':
            cave()
            break
        else:
            print_pause("Invalid input! Please enter 1 or 2.")
            field()
            break


def house():
    print_pause("You are about to knock on the door.")
    print_pause("You walk inside the house.")
    print_pause(f"The house is full of {enemy}")
    print_pause(f"Yikes!, This is the {enemy} house!")
    fight()


def fight():
    print_pause(f"The {enemy} start to attacks you!")
    while True:
        fight = input("Would you like to (1) fight or (2) run away?\n")
        if fight == '1':
            print_pause(f"The {enemy} moves towards you to attack")
            print_pause(f"You grab new {weapons}")
            print_pause(f"The shiny {weapons} of Wudang in your"
                        "hand as you make an attack.")
            print_pause(f"Attack! {enemy}")
            print_pause(f"The {enemy} is now destroyed.")
            print_pause(f"Victory!, You have defeated the {enemy}.")
            play_again()
            break
        elif fight == '2':
            print_pause("You run back to the open field.")
            print_pause("Unfortunately you unable to attack the enemy.")
            print_pause("Luckily, no enemies follow you.")
            print_pause("Game Over!")
            play_again()
            break
        else:
            print_pause("Invalid input! Please enter 1 or 2.\n")


def cave():
    print_pause("This is an empty cave.")
    print_pause("You have been to this place before,"
                "and got the weapons from the wooden crates")
    print_pause(f"You have found magical {weapons} located inside the crate.")
    print_pause("Walk back out to the field.")
    field()


def play_again():
    choice = input("Would you like to play again? (y or n)").lower()
    while True:
        if choice == 'y':
            print_pause("OK, Restarting the game...\n")
            play_game()
            break
        elif choice == 'n':
            print_pause("Thanks for playing the game! Goodbye\n")
            break
        else:
            print_pause("Please enter y or n.\n")
            play_again()
            break


# Starts the game function
def play_game():
    intro()


play_game()
