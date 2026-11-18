import random
import os

class NumberGuessingGame:
    def __init__(self):
        self.score_file = "high_scores.txt"
        
    def get_difficulty(self):
        """Allows the user to select difficulty and returns max attempts and difficulty name."""
        print("\n=== SELECT DIFFICULTY ===")
        print("1. Easy (10 attempts)")
        print("2. Medium (7 attempts)")
        print("3. Hard (5 attempts)")
        while True:
            choice = input("Enter choice (1-3): ").strip()
            if choice == '1':
                return 10, "Easy"
            elif choice == '2':
                return 7, "Medium"
            elif choice == '3':
                return 5, "Hard"
            print("Invalid choice. Please enter 1, 2, or 3.")

    def give_hint(self, secret_number, wrong_tries):
        """Provides a helpful hint after 3 wrong attempts."""
        if wrong_tries == 3:
            print("\n [HINT]:", end=" ")
            if secret_number % 2 == 0:
                print("The number is even.")
            else:
                print("The number is odd.")
            
            if secret_number > 50:
                print("It is greater than 50.")
            else:
                print("It is 50 or less.")

    def save_score(self, username, difficulty, attempts_left):
        """Saves username, difficulty, and score (attempts remaining) to a .txt file."""
        score = attempts_left + 1
        record = f"{username},{difficulty},{score}\n"
        with open(self.score_file, "a") as f:
            f.write(record)

    def show_leaderboard(self):
        """Reads high scores from the file and displays a sorted leaderboard."""
        if not os.path.exists(self.score_file):
            print("\n No high scores recorded yet!")
            return
        
        print("\n --- LEADERBOARD (TOP 5) ---")
        scores = []
        with open(self.score_file, "r") as f:
            for line in f:
                parts = line.strip().split(",")
                if len(parts) == 3:
                    name, diff, scr = parts[0], parts[1], int(parts[2])
                    scores.append((name, diff, scr))
        
        # Sort by score descending
        scores.sort(key=lambda x: x[2], reverse=True)
        
        print(f"{'Rank':<6} {'Username':<15} {'Difficulty':<12} {'Score':<6}")
        print("-" * 43)
        for i, (name, diff, scr) in enumerate(scores[:5], 1):
            print(f"{i:<6} {name:<15} {diff:<12} {scr:<6}")
        print("-" * 43)

    def play(self):
        """Main game loop."""
        print("========================================")
        print("     Welcome to the Number Guessing Game! ")
        print("========================================")
        username = input("Enter your username: ").strip()
        if not username:
            username = "Player"

        while True:
            secret_number = random.randint(1, 100)  # as per instructions
            max_attempts, diff_name = self.get_difficulty()
            attempts_left = max_attempts
            wrong_tries = 0

            print(f"\nI'm thinking of a number between 1 and 100.")
            print(f"Difficulty: {diff_name} ({max_attempts} attempts). Good luck!\n")

            won = False
            while attempts_left > 0:
                print(f"Attempts remaining: {attempts_left}")
                guess_input = input("Enter your guess: ").strip()

                if not guess_input.isdigit():
                    print(" Please enter a valid integer between 1 and 100.")
                    continue

                guess = int(guess_input)

                if guess == secret_number:
                    print(f"\n Correct! You guessed the number {secret_number} in {max_attempts - attempts_left + 1} tries!")
                    won = True
                    self.save_score(username, diff_name, attempts_left)
                    break
                elif guess < secret_number:
                    print(" Too Low!")
                else:
                    print(" Too High!")

                attempts_left -= 1
                wrong_tries += 1

                # Trigger hint after 3 wrong tries
                if not won and attempts_left > 0:
                    self.give_hint(secret_number, wrong_tries)

            if not won:
                print(f"\n Game Over! You ran out of attempts. The secret number was {secret_number}.")

            self.show_leaderboard()

            play_again = input("\nWould you like to play again? (y/n): ").strip().lower()
            if play_again != 'y':
                print("\nThanks for playing! Goodbye.")
                break

if __name__ == "__main__":         # control how the application starts
    game = NumberGuessingGame()
    game.play()