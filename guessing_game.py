import random
GREEN = "\033[92m"
YELLOW = "\033[93m"
RED = "\033[91m"
CYAN = "\033[96m"
RESET = "\033[0m"

def play_game():
    print(f"{CYAN}🎯 Welcome to the Number Guessing Game!{RESET}")
    print(f"{YELLOW}Choose difficulty: Easy / Medium / Hard{RESET}")
    difficulty = input("Enter difficulty: ").lower()

    if difficulty == "easy":
        max_num = 10
        attempts = 6
        color = GREEN
    elif difficulty == "medium":
        max_num = 50
        attempts = 5
        color = YELLOW
    elif difficulty == "hard":
        max_num = 100
        attempts = 4
        color = RED
    else:
        print(f"{RED}Invalid choice. Defaulting to Easy.{RESET}")
        max_num = 10
        attempts = 6
        color = GREEN

    secret_number = random.randint(1, max_num)
    print(f"\n{color}I'm thinking of a number between 1 and {max_num}. You have {attempts} attempts!{RESET}")

    for i in range(attempts):
        guess = int(input(f"Attempt {i+1}: Your guess? "))
        if guess == secret_number:
            print(f"{GREEN}🎉 Correct! You win!{RESET}")
            break
        elif guess < secret_number:
            print(f"{YELLOW}📉 Too low.{RESET}")
        else:
            print(f"{RED}📈 Too high.{RESET}")
    else:
        print(f"{RED}😢 Out of attempts. The number was {secret_number}.{RESET}")

while True:
    play_game()
    again = input(f"\n{CYAN}Do you want to play again? (yes/no): {RESET}").lower()
    if again != "yes":
        print(f"{CYAN}Thanks for playing! Goodbye! 👋{RESET}")
        break
