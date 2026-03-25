# 🎯 Number Guessing Game (CLI)

A simple and interactive **Command Line Number Guessing Game** built using Python.

-------------------------------

## 🚀 Features

* 🎮 Difficulty Levels (Easy, Medium, Hard)
* 💡 Hint System (Too Close / Close / Far)
* 🔢 Attempt Tracking
* 📊 Player Statistics (Wins, Losses, Win Rate)
* 🏆 Leaderboard (Top 5 Players)
* 🔁 Replay Option
* 🧱 Modular Code Structure

---------------------------------

## 📁 Project Structure

```
01_number_guessing_game/
│
├── main.py          # Entry point
├── game.py          # Game logic
├── utils.py         # Input & helper functions
├── leaderboard.py   # Leaderboard logic
├── stats.py         # Player stats
│
└── game_data/
    ├── leaderboard.json
    └── stats.json
```

----------------------------------

## ▶️ How to Run

```bash
python main.py
```

-------------------------------------------

## 🧠 How It Works

* A random number is generated between **1 and 100**
* Player selects difficulty (attempt limit)
* Player guesses the number
* System gives hints based on closeness

### 📊 Tracks

* Attempts
* Wins / Losses
* Leaderboard

--------------------------------------------

## 🛠️ Tech Used

* Python
* JSON (for data storage)
* CLI (Command Line Interface)

---

## 📌 Future Improvements

* Add GUI (Tkinter / Web)
* Add multiplayer mode
* Store data in database (SQLite)
* Add user authentication

-------------------------------------------------

## 👨‍💻 Author

**Mohammad Faizan**

---

## ⭐ Support

If you like this project, give it a ⭐ on GitHub!
