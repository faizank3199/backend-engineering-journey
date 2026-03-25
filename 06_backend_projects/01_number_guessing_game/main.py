from game import play_game
from stats import load_stats, save_stats, show_stats
from leaderboard import show_leaderboard

def main()-> None:
    """ main program loop"""
    stats = load_stats()
    
    while True:
            result, attempts_used = play_game()
            stats["played"] += 1
            
            if result:
                    stats["wins"] +=1
            else:
                    stats["losses"] +=1
                    
            save_stats(stats)
            
            show_stats(stats)
            show_leaderboard()
            
            play_again = input("You want to play again (y/n): ").lower()
        
            if play_again != "y":
                print("Thanks for play game.")
                break
                
if __name__ == "__main__":
    main()