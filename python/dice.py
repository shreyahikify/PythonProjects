import random

print("Dice Rolling Simulator")

while True:
    choice = input("Roll the dice? (y/n): ").lower()

    if choice == "y":
        dice = random.randint(1, 6)
        print("You rolled:", dice)
    elif choice == "n":
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice. Enter y or n.")
