# Hangman Game.
def start_application():
    # Initialize the game cycle
    cycle = True

    while cycle:
        print("\nWelcome! Today is a day of challenges. Win or Lose!")
        player_name = input("Name: ").capitalize()
        # Check if the player's name is valid
        if player_name.isalpha() and len(player_name) >= 3:
            print(f"Welcome {player_name}, remember you have 6 lives to guess the word. Good Luck!")
            choosing_word(player_name)  # Start the word selection process
            cycle = False
        else:
            print("Only letters. Minimum 3 characters. Thank you!")
            continue

def choosing_word(player_name):
    # List of random words for the game
    random_word_list = ["python", "javascript", "technology", "world", "space"]
    cycle = True
    while cycle:
        try:
            # Prompt the player to choose a word
            choosing_random_word = int(input(f"{player_name}, enter a number from 1-5 (A random word will be chosen): "))
            selecting_random_word = choosing_random_word - 1
        except:
            print("Only numbers. Thank you!")
            continue
        # Validate the chosen number
        if choosing_random_word > 0 and choosing_random_word <= 5:
            for iter in random_word_list:
                random_word = random_word_list[selecting_random_word]
                hidden_word = ["_" for _ in range(len(random_word))]  # Create a hidden version of the word
                validate_hidden_word(player_name, hidden_word, random_word)  # Start validating the hidden word
                cycle = False
                break
        else:
            print("Wrong option.")
            continue

def validate_hidden_word(player_name, hidden_word, random_word):   
    lives = 6  # Set initial lives
    mistakes = []  # List to track mistakes
    correct_guesses = []  # List to track correct guesses
    
    while lives > 0:
        # Display current game status
        print(f"\nLives: {lives}\nHidden Word: {' '.join(hidden_word)}\nMistakes: {', '.join(mistakes)} and number of mistakes {len(mistakes)}")

        letter = str(input("Letter = -1 life | Word = -3 lives: ").lower())
        # Check if the input is a single letter
        if letter.isalpha() and len(letter) == 1:
            pass

        # Check if the input is numeric
        if letter.isnumeric():
            print(f"Only letters. Thank you!\nRemember to use a letter or the full number of characters in the word. {len(hidden_word)}")
            continue

        # Check if the guessed word is incorrect
        if len(letter) > 1 and letter != random_word:
            print(f"{player_name}, incorrect word. You lost '3' lives.")
            lives -= 3
            continue

        # Check if the guessed word is correct
        if letter == random_word:
            print(f"{player_name}, you guessed the complete word. Congratulations!")
            break

        # Check if the letter has not been guessed before
        if letter not in correct_guesses:
            if letter in random_word and len(letter):
                for i, e in enumerate(random_word):
                    if e == letter:
                        hidden_word[i] = letter  # Reveal the letter in the hidden word
                        correct_guesses.append(letter)  # Add to correct guesses
                        print(f"Correct {player_name}")
            else:
                print(f"The letter does not exist. You lost a life!\n")
                mistakes.append(letter)  # Add to mistakes
                lives -= 1
        else:
            print("The letter has already been used. You lost '1' life.")
            lives -= 1
            continue

        # Check if the player has guessed the whole word
        if "_" not in hidden_word:
            print(f"\nHidden Word: {' '.join(hidden_word)}\n'{player_name}' you won. Congratulations!\nThe word was '{''.join(hidden_word).upper()}'")
            break

    else:
        # If the player runs out of lives
        print(f"You lost {player_name}, you have no more lives. The word was: {random_word}")

start_application()  # Start the application
