# Number Guessing Game: Complete Project Guide

A command-line **Number Guessing Game** built in Python featuring selectable difficulty levels, an automatic hint system, persistent local leaderboard tracking, and clean object-oriented design.

---

## Table of Contents
1. [Project Overview & Features](#project-overview--features)
2. [Project Structure](#project-structure)
3. [Prerequisites](#prerequisites)
4. [Repository Source Code (`number_guessing_game.py`)](#complete-source-code-number_guessing_gamepy)
5. [How to Run & Play](#how-to-run--play)

---

## Project Overview & Features

* Object-Oriented Design:** Built using a clean Python class (`NumberGuessingGame`).
* Difficulty Levels:**
  * Easy:** 10 attempts
  * Medium:** 7 attempts
  * Hard:** 5 attempts
* Real-Time Feedback:** Guides the player with `"Too High"` or `"Too Low"` prompts.
* Smart Hint System:** Automatically triggers after **3 consecutive wrong guesses**, giving the player parity (even/odd) and range (greater/less than 50) clues.
* Persistent Leaderboard:** Saves winning scores (`username`, `difficulty`, and score based on remaining attempts) to a local `high_scores.txt` file and displays the Top 5 players.
* Input Validation:** Safely catches non-numeric inputs without crashing.

---

## Project Structure

``` text
number_guessing_game/
├── number_guessing_game.py   # Main game script
├── high_scores.txt           # Auto-generated file storing player high scores
└── README.md                 # Complete project documentation
```
--- 

## Prerequisites
 ### Requirements
 1. Python 3.x installed on your machine.

 2. No external packages required (pip install is unnecessary since it only uses Python's built-in random and os modules).

---

## Installation 
  Download or clone this repository to your local machine.

  Repository link;

```
https://github.com/Derroww/number_guessing_game.git

```

---

## How to Run

1. Save the script.
2. Open a terminal in the folder containing the file.
3. Run:

   ```
   bash

   python number_guessing_game.py

   ```

---

## How to Play

1. Enter your username.
2. Choose a difficulty: 1. `Easy`, 2. `Medium`, or 3. `Hard` (Enter choice(1-3)).
3. The game picks a random number between 1 and 100.
4. Enter your guesses. After each one, the game tells you if it was too low or too high and how many guesses remain.
5. After your 3rd incorrect guess, you get a hint about whether the number is odd or even.
6. Win by guessing the number within your allowed attempts. If you run out, the game reveals the correct number.
7. If correct displays a message and the tries and shows leaderboard. Then displays if you would like to play again.

---

## Example Session

```
========================================
     Welcome to the Number Guessing Game! 
========================================
Enter your username: Derrick

=== SELECT DIFFICULTY ===
1. Easy (10 attempts)
2. Medium (7 attempts)
3. Hard (5 attempts)
Enter choice (1-3): 1

I'm thinking of a number between 1 and 100.
Difficulty: Easy (10 attempts). Good luck!

Attempts remaining: 10
Enter your guess: 20
 Too Low!
Attempts remaining: 9
Enter your guess: 60
 Too High!
Attempts remaining: 8
Enter your guess: 50
 Too High!

 [HINT]: The number is odd.
It is 50 or less.
Attempts remaining: 7
Enter your guess: 40
 Too High!
Attempts remaining: 6
Enter your guess: 30
 Too Low!
Attempts remaining: 5
Enter your guess: 35
 Too High!
Attempts remaining: 4
Enter your guess: 32
 Too Low!
Attempts remaining: 3
Enter your guess: 33

 Correct! You guessed the number 33 in 8 tries!

 --- LEADERBOARD (TOP 5) ---
Rank   Username        Difficulty   Score 
-------------------------------------------
1      Derrick         Easy         4     
-------------------------------------------

Would you like to play again? (y/n): n

Thanks for playing! Goodbye.

```
---
## Scoring system

The game's scoring philosophy rewards **efficiency and precision**: the fewer attempts you use to find the secret number, the higher your score.

When a player successfully guesses the number, their score is computed as:

$$\text{Score} = \text{Remaining Attempts} + 1$$

### Example Breakdowns:

* **Easy Mode (10 total attempts):**
  * You guess correctly on your **3rd try**.
  * Remaining attempts = $10 - 3 = 7$.
  * **Final Score:** $7 + 1 = \mathbf{8 \text{ points}}$

* **Hard Mode (5 total attempts):**
  * You guess correctly on your **1st try** (a lucky first guess!).
  * Remaining attempts = $5 - 1 = 4$.
  * **Final Score:** $4 + 1 = \mathbf{5 \text{ points}}$

---

## Data Persistence (`high_scores.txt`)

Every time a game is won, the program appends a new record to the local `high_scores.txt` file. The data is saved in a simple comma-separated value format:

```text
username,difficulty,score
Derrick,Easy,4

```

---

## Leaderboard Ranking Rules

When the leaderboard is requested or displayed at the end of a round:

Parsing: The script reads high_scores.txt line by line and extracts the player's username, difficulty, and numeric score.

Sorting: The list of scores is sorted in descending order based on the score value (Score descending).

Filtering: The game slices the sorted list to display only the Top 5 highest-scoring players.

---

## Author

Derrick Sum

## License 

This project is licensed by MIT. 

---
