import random
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors"):
         (user_choice == "scissors" and computer_choice == "paper") 
         (user_choice == "paper" and computer_choice == "rock")
         return "user"
    else:
        return "computer"
user_score = 0
computer_score = 0
ties = 0
while True:
    user_choice = input("\nEnter rock, paper, or scissors (or 'quit' to exit): ")
    if user_choice == "quit":
        print("\nGame Over!")
        print(f"Final Scores: You - {user_score}, Computer - {computer_score}, Ties - {ties}")
        break
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        continue
    computer_choice = get_computer_choice()
    print(f"Computer chose: {computer_choice}")
    result = determine_winner(user_choice, computer_choice)   
    if result == "user":
        print("You win this round!")
        user_score += 1
    elif result == "computer":
        print("Computer wins this round!")
        computer_score += 1
    else:
        print("It's a tie!")
        ties += 1
