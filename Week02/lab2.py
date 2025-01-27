# Lab 02 solutions
import random

# Define the weapons array 
weapons = ["Fist", "Knife", "Club", "Gun", "Bomb", "Nuclear bomb"]

try:
    # Roll the dice (1-6) 
    weaponRoll = random.randint(1, 6) - 1  # Subtract 1 to match the 0-based index of the array

    # Add weaponRoll to the hero's combat strength
    hero_combat_strength = 10  # Example base combat strength of the hero
    hero_combat_strength += weaponRoll

    # Use weaponRoll as an index into the weapons array and get the hero's weapon
    if 0 <= weaponRoll < len(weapons):  # Ensure the weaponRoll is within valid range
        chosen_weapon = weapons[weaponRoll]
        print(f"Weapon chosen: {chosen_weapon}")

        # Define the conditions
        if weaponRoll <= 2:
            print("You rolled a weak weapon, friend.")
        elif weaponRoll <= 4:
            print("Your weapon is meh.")
        else:
            print("Nice weapon, friend!")

        if chosen_weapon != "Fist":
            print("Thank goodness you didn't roll the Fist...")

    else:
        # Handle any unexpected cases where weaponRoll is out of range
        print("Error: Invalid weapon index.")

except ValueError:
    # Error handling if input is invalid
    print("Invalid input. Please ensure the inputs are valid integers.")
except Exception as e:
    print(f"An error occurred: {e}")
