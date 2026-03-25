def choose_difficulty():
    print("\nChoose difficulty:")
    print("1 → Easy (10)")
    print("2 → Medium (8)")
    print("3 → Hard (6)")

    while True:
        try:
            choice = int(input("Enter choice: "))
            if choice == 1:
                return 10
            elif choice == 2:
                return 8
            elif choice == 3:
                return 6
            else:
                print("Invalid choice")
        except ValueError:
            print("Enter valid number")


def get_user_guess():
    while True:
        try:
            guess = int(input("Enter guess (1–100): "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Out of range")
        except ValueError:
            print("Invalid input")


def check_guess(secret, guess):
    if guess == secret:
        print("Correct!")
        return True

    elif guess > secret:
        print("Too High")
    else:
        print("Too Low")

    diff = abs(secret - guess)

    if diff <= 5:
        print("Too Close")
    elif diff <= 15:
        print("Close")
    else:
        print("Far")

    return False