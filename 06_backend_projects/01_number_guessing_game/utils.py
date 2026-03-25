

def choose_difficulty()-> int:
    """ choose game difficulty and return the attempts """
    print("\n== Choose difficulty ==")
    print("1 -> Easy (10 attempts)")
    print("2 -> Medium (8 attempts)")
    print("3 -> Hard (6 attempts)")
    
    while True:
        
        try:
            choice = int(input("Enter the number 1 / 2 / 3: "))
        
            if choice == 1:
                return 10
        
            elif choice == 2:
                return 8
        
            elif choice == 3:
                return 6
        
            else:
                print("Invalid input. Please choose between 1, 2 or 3.")
            
        except ValueError:
            print("Please enter valid input")
            

def get_user_guess():   # userinput
    
    print("\n== Choose number between 1 to 100 ==")
    
    while True:
        try:
            guess = int(input("Guess the number: "))
            if 1 <= guess <=100:
                return guess
            else:
                print("Please choose between 1 to 100")   
                
        except ValueError:
            print("Please enter valid input ")
             

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
    
    print("== Hint ==")
    if difference <= 5:
        print("Too Close")
        
    elif difference <= 15:
        print("Close")
        
    else:
        print("Far")

    return False
    