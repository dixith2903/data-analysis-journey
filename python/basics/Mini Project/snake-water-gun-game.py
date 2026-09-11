import random

def game_win(user, comp):
    if user == comp:
        return "None"  # It's a draw
    # Snake vs Water
    if user == "s" and comp == "w":
        return True
    if user == "w" and comp == "s":
        return False
    # Water vs Gun
    if user == "w" and comp == "g":
        return True
    if user == "g" and comp == "w":
        return False
    # Gun vs Snake
    if user == "g" and comp == "s":
        return True
    if user == "s" and comp == "g":
        return False

random_number = random.randint(1, 3)

print("computer turn: snake(1) water(2) gun(3)")

if random_number == 1:
    comp_turn = "snake"
elif random_number == 2:
    comp_turn = "water"
else:
    comp_turn = "gun"

user_input = input("your turn: snake(1) water(2) gun(3)").lower()

# Convert user input to match format
if user_input == "1" or user_input == "snake" or user_input == "s":
    user = "s"
elif user_input == "2" or user_input == "water" or user_input == "w":
    user = "w"
elif user_input == "3" or user_input == "gun" or user_input == "g":
    user = "g"
else:
    user = user_input

# Convert computer choice to character format for comparison
comp_char = comp_turn[0]  # Get first letter: "snake" -> "s", "water" -> "w", "gun" -> "g"

result = game_win(user, comp_char) # Return True if user wins, False if computer wins, Draw if tie

print(f"\nYou chose {user}")
print(f"Computer chose {comp_turn}")

if result == "None":
    print("It's a draw!")
elif result:
    print("Congratulations! You win!")
else:
    print("Computer wins! Better luck next time.")