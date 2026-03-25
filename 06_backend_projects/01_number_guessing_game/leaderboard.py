import json
import os
os.makedirs("game_data", exist_ok=True)

FILE = "game_data/leaderboard.json"
def load_leaderboard():
    if not os.path.exists(FILE):
        return []
    
    try: 
        with open(FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return []
    
def save_record(name, attempts):
    board = load_leaderboard()
    
    board.append(
        {
        "name": name,
        "attempts": attempts
        }
    )
    
    board = sorted(board, key=lambda x: x["attempts"])[:5]
    
    with open(FILE, "w") as f:
        json.dump(board, f, indent=4)
    
def show_leaderboard(): 
    board = load_leaderboard()
    
    print("\n=== Leaderboard ===")
    print("---------------------")
    
    if not board:
        print(" No score yet ")
        return 
    
    for i, player in enumerate(board, 1 ):
        print(f"{i} -> {player['name']} , score: {player['attempts']} attempts")
