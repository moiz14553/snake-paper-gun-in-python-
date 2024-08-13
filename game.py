#-------GAME-------------------

import random

# Choices: 1 for snake, -1 for water, 0 for gun
choices = {
    "s": 1,  # snake
    "w": -1, # water
    "g": 0   # gun
}

reverse_choices = {
    1: "snake",
    -1: "water",
    0: "gun"
}

# Computer makes a random choice
computer = random.choice([-1, 0, 1])
print(" ------------------------GAME START!:)------------------------")
# User makes a choice
you = input("Enter your choice (s for snake, w for water, g for gun): ").lower()

if you in choices:
    user_choice = choices[you]

    # Display choices
    print(f"Your choice: {reverse_choices[user_choice]}")
    print(f"Computer's choice: {reverse_choices[computer]}")

    # Determine the winner
    if computer == user_choice:
        print("It's a draw!")
    elif (user_choice == 1 and computer == -1) or \
         (user_choice == -1 and computer == 0) or \
         (user_choice == 0 and computer == 1):
        print("You win the game!")
    else:
        print("You lose!")
else:
    print("Invalid choice! Please select 's', 'w', or 'g'.")
