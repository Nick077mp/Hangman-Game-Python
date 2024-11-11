# Hangman-Game-Python

# Note:
The reason why I decided to program this game was to keep practicing and improve my comprehension of list abilities and programming logic. With this type of game, you will find yourself in a position to figure out plenty of logic issues along the way. You will function with concepts like enumerating and indexing elements, logical positioning, and ordering to build the world and lists, similar to the function 'join'.


# How to Play
Start the Game: Run the Python script.
Enter Your Name: Provide your name when prompted.
Choose a Word: Select a number between 1 and 5 to choose a random word.
Guess Letters:
Guess a letter.
If the letter is in the word, it will be revealed.
If the letter is not in the word, you lose a life.
You can also guess the entire word.
Win or Lose:
If you guess the word before running out of lives, you win.
If you run out of lives, you lose.

# Code Structure
The code is structured into several functions:
start_application(): Initializes the game and handles the main game loop.
choosing_word(): Prompts the player to choose a random word from a list.
validate_hidden_word(): Implements the core game logic, including:
Tracking lives and mistakes.
Processing player input (letters or full word guesses).
Revealing letters in the hidden word.
Determining win or loss conditions.

