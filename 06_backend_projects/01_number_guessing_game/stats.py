import json
import os 


FILE = "game_data/stats.json"

def load_stats():
    
    if not os.path.exists(FILE):
        return {"played":0, "wins":0, "losses":0}
    
    try:
        with open(FILE, "r") as f:
            return json.load(f)
        
    except json.JSONDecodeError:
        return {"played":0, "wins":0, "losses":0}
    
    
def save_stats(stats):
    with open(FILE, "w") as f:
        json.dump(stats, f, indent=4)
    
def show_stats(stats):
    
    print("\n== Player Stats ==")
    print("--------------------")
    
    print(f"Played Game: {stats['played']}")
    print(f"Wins: {stats['wins']}")
    print(f"Losses: {stats['losses']}")
    
    if  stats["played"]> 0:
        rate = (stats["wins"] / stats["played"]) * 100
        print(f"Win Rate: {rate:.2f}%")
    
    