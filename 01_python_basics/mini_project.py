#=====================================
#         Number Guessing Game
#=====================================

"""


CLI game where the player guesses a 
random number between 1 and 100.

Features:
- Difficulty levels
- Hint system
- Attempt system
- Input validation
- Player statistics
- Leaderboard (Top 5)
- Replay option

Author: Mohammad Faizan
Date: 09/03/2026
"""

import random
import json
import os 
os.makedirs("data", exist_ok=True)
#-------------------------------------------------------
# LeaderBoard Functions

FILE = "data/leaderboard.json"
def load_leaderboard():
    
    if not os.path.exists(FILE):
        return []
    
    
    try:
        with open(FILE,"r") as f:
            return json.load(f)
        
    except json.JSONDecodeError:
        return []
        
# Save Record 
def save_record(name,attempts):
    board = load_leaderboard()
    
    board.append(
        {
            "name" : name,
            "attempts": attempts
        }
    )
    board = sorted(board, key=lambda x : x["attempts"])[:5]
    
    with open(FILE,"w") as f:
        json.dump(board, f, indent=4)

# show Leaderboard
    
def show_leaderboard():
    board = load_leaderboard()
    
    print("\nLeaderboard")
    print("---------------")
    
    if not board:
        print("no scores yet")
        return 
    
    for i, player in enumerate(board,start=1):
        print(f"{i}. {player['name']} - {player['attempts']} attempts")

#----------------------------------------------------------------
# Difficulty 

def choose_difficulty() -> int:
    """Choose game difficulty and return attempts"""

    print("\nChoose difficulty:")
    print("1 → Easy   (10 attempts)")
    print("2 → Medium (8 attempts)")
    print("3 → Hard   (6 attempts)")

    while True:
        try:
            choice = int(input("Enter the number (1/2/3): "))

            if choice == 1:
                return 10
            elif choice == 2:
                return 8
            elif choice == 3:
                return 6
            else:
                print("Invalid input. Choose 1, 2, or 3.")

        except ValueError:
            print("Please enter a valid number.")


def get_user_guess() -> int:
    """Get valid integer guess from the user"""

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if 1 <= guess <= 100:
                return guess
            else:
                print("Enter a number between 1 and 100")

        except ValueError:
            print("Please enter a valid number.")


def check_guess(secret_number: int, guess: int) -> bool:
    """Compare guess with secret number"""

    if guess == secret_number:
        print("Congratulations!")
        return True

    elif guess > secret_number:
        print("Too High")

    else:
        print("Too Low")
        
    # Hint System
    difference = abs(secret_number-guess)
    
    if difference <= 5:
        print("Too Close")
        
    elif difference <= 15:
        print("Close")
        
    else:
        print("Far")

    return False


def play_game() -> bool:
    """Main game logic"""

    print("\nWelcome to the Number Guessing Game!")
    print("Try to guess the number between 1 and 100.")

    secret_number = random.randint(1, 100)
    attempts = choose_difficulty()
    attempts_used = 0

    while attempts > 0:

        print(f"\nAttempts left: {attempts}")

        guess = get_user_guess()
        attempts_used += 1

        if check_guess(secret_number, guess):
            print("You Win!")
             
            name = input("Enter Your name: ")
            save_record(name, attempts_used)
            
            return True   # win
         
        attempts -= 1

    print("\nGame Over")
    print(f"The secret number was {secret_number}")
    
    return False   # loss

   
    
def show_stats(played_games: int, wins:int, losses:int)->None:
    print("Player Statistics")
    print("======================")
    print("Total Games: ",played_games)
    print("Wins: ",wins)
    print("Losses:",losses )
    
    if played_games > 0:
        rate = (wins / played_games) * 100
        print(f"Win Rate: {rate:.2f}%")
    
    
    

def main() -> None:
    """Main program loop"""
    played_game = 0
    wins = 0
    losses = 0

    while True:
        result = play_game()
        played_game +=1
        if result:
            wins +=1
        else:
            losses +=1
            
        show_stats(played_game,wins,losses)
        show_leaderboard()

        again = input("\nPlay again? (y/n): ").lower()

        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()