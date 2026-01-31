import random

def play_game():
    options = ["rock", "paper", "scissors"]
    user_score = 0
    cpu_score = 0

    print("--- Rock, Paper, Scissors ---")
    
    while True:
        computer_choice = random.choice(options)
        user_choice = input("Enter Rock, Paper, or Scissors (or 'q' to quit): ").lower()

        if user_choice == 'q':
            break
        
        if user_choice not in options:
            print("Invalid choice. Try again.")
            continue

        print(f"Computer chose: {computer_choice}")

        if user_choice == computer_choice:
            print("It's a tie!")
        elif (user_choice == "rock" and computer_choice == "scissors") or \
             (user_choice == "paper" and computer_choice == "rock") or \
             (user_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            user_score += 1
        else:
            print("Computer wins this round!")
            cpu_score += 1
        
        print(f"Score -> You: {user_score} | CPU: {cpu_score}\n")

    print("Final Score:", f"You: {user_score} | CPU: {cpu_score}")
    print("Thanks for playing!")

play_game()