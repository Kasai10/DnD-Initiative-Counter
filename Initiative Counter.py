import os
import random
from colorama import init, Fore, Style


# Initialize colorama
init()

def get_characters():
    characters = {}
    while True:
        character = input("Input a Player (n to continue): ")
        if(character == "n"):
            break
        initiative = int(input("Initiative Count: "))
        characters[character] = initiative

    while True:
        monster = input("Input a Monster (n to finish): ")
        if(monster == "n"):
            break
        number_of_monsters = int(input("Number of Monsters of type: "))
        for i in range(number_of_monsters):
            initiative = random.randint(1, 20)
            characters[monster + " " + str(i + 1)] = initiative
    
    sort_initiative(characters)

def sort_initiative(characters):
    sorted_dict_desc = dict(sorted(characters.items(), key=lambda item: item[1], reverse=True))
    display_inititative(sorted_dict_desc)

def display_inititative(characters):
    values = characters.keys()
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    # For Linux, macOS, and other Unix-like systems
    else:
        os.system('clear')
        
    print("Press d to kill a participant!")
    print()
    print("Initiative Order: ")
    
    for key in characters.keys():
        print(Fore.GREEN + key + Style.RESET_ALL)
        characters[key] = "a"

    print(f'\x1b[{len(values)}A', end="", flush=True)

    while True:
        
        i = 0
        # Move the cursor down to the first entry and print the arrow
        for _ in characters.keys():
            i += 1
            color = Fore.GREEN
            if(characters[_] == "a"):
                print(color + "\r" + str(_) + " <----" + Style.RESET_ALL, flush=True, end="")
                user_input = input()
                if(user_input == "d"):
                    color = Fore.RED
                    characters[_] = "d"
                print('\x1b[1A', end='', flush=True)  # Move cursor up
                print('\x1b[2K', end='', flush=True)  # Clear the line
                print(color + "\r" + str(_) + Style.RESET_ALL, flush=True, end="") 
                print('\x1b[1B', end ="", flush=True)
            else:
                print('\x1b[1B', end ="", flush=True)
            
            if(i == len(values)):
                i = 0
                print(f'\x1b[{len(values)}A', end="", flush=True)


get_characters()


