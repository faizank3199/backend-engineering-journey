import random
from utils import choose_difficulty
from utils import get_user_guess
from utils import check_guess
from leaderboard import save_record


def play_game()-> bool:
    """ main game logic """
    
    print("\n Welcome to  number guessing game! ")
    secret_number = random.randint(1, 100)
    attempts = choose_difficulty()
    attempts_used = 0
    while attempts > 0: 
        
        print("--------------------------")
        print(f"Attempts Left: {attempts}")
        print("--------------------------")
        
        guess  = get_user_guess()
        attempts_used += 1
        
        if check_guess(secret_number, guess):
            print("You Won!")
              
            name = input("Enter your name:  ")
            save_record(name, attempts_used)
        
            return True, attempts_used
        
        attempts -= 1
    
    print("\n== Game Over ==")
    print(f"Secret number was {secret_number}")
    
    return False, attempts_used
        
    

        
        
        
        
        
        
         
    
    