import random
choices = ["rock", "paper", "scissors"]
rounds_played = 0
user_score = 0
computer_score = 0
ties = 0
total_rounds = int(input("Enter number of rounds to play: "))
while rounds_played < total_rounds:
    print("\nRound", rounds_played + 1)
    user = input("Enter rock, paper, or scissors: ").lower()
    if user not in choices:
        print("Invalid choice! Try again.")
        continue
    computer = random.choice(choices)
    print("You chose:", user)
    print("Computer chose:", computer)
    rounds_played += 1
    if user == computer:
        print("Result: It's a tie!")
        ties += 1
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        print("Result: You win this round!")
        user_score += 1
    else:
        print("Result: Computer wins this round!")
        computer_score += 1
print("\n===== GAME OVER =====")
print("Total rounds played:", rounds_played)
print("Your score:", user_score)
print("Computer score:", computer_score)
print("Ties:", ties)
total_score = user_score + computer_score
with open("game_results.txt", "w") as file:
    file.write("Rock Paper Scissors Game Results\n")
    file.write(f"Total rounds played: {rounds_played}\n")
    file.write(f"User score: {user_score}\n")
    file.write(f"Computer score: {computer_score}\n")
    file.write(f"Ties: {ties}\n")
    file.write(f"Total score (User + Computer): {total_score}\n")
print("\nResults saved successfully in 'game_results.txt'")
