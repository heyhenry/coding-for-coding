import random

# battle logic of rock, paper, scissors
def rps_battle(ai_choice, player_choice):
    # 1 = player wins, 2 = ai wins, 3 = draw
    
    if player_choice == 'rock' and ai_choice == 'paper':
        return print("AI Wins")
    elif player_choice == 'paper' and ai_choice == 'scissors':
        return print("AI Wins")
    elif player_choice == 'scissors' and ai_choice == 'rock':
        return print("AI Wins")
    elif player_choice == ai_choice:
        return print("Draw")
    return print("Player Wins")

running = True

ai_choices = ['rock', 'paper', 'scissors']

# loop and input validation
while running:
    print("=== Menu ===")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Exit")
    choice = int(input("Select a number: "))
    print("=== ==== ===")

    if choice == 1:
        rps_battle(random.choice(ai_choices), 'rock')
    elif choice == 2:
        rps_battle(random.choice(ai_choices), 'paper')
    elif choice == 3:
        rps_battle(random.choice(ai_choices), 'scissors')
    elif choice == 4:
        print("Exiting the program...")
        exit(0)
    else:
        raise ValueError("Must be a number listed on the menu.")



