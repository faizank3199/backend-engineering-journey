from game import play_game
from leaderboard import show_leaderboard
from stats import load_stats, save_stats, show_stats


def main():
    stats = load_stats()

    while True:
        result, attempts_used = play_game()

        stats["played"] += 1

        if result:
            stats["wins"] += 1
        else:
            stats["losses"] += 1

        save_stats(stats)

        show_stats(stats)
        show_leaderboard()

        again = input("\nPlay again? (y/n): ").lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()