import os
import time
import random

# Define the stages of the stickman
stages = [
    """
     ------
     |    |
     |    
     |   
     |    
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   
     |    
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |    |
     |    
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|
     |    
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |    
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / 
     |
    ---
    """,
    """
     ------
     |    |
     |    O
     |   /|\\
     |   / \\
     |
    ---
    """
]

def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')

def display_game(word, guessed_letters, stage_index, final=False):
    clear_screen()
    if not final:
        print(stages[stage_index])
    print("Word: " + ' '.join([letter if letter in guessed_letters else '_' for letter in word]))
    print("Guessed letters: " + ', '.join(guessed_letters))

def hangman(word):
    guessed_letters = set()
    attempts = len(stages) - 1
    
    while attempts >= 0:
        display_game(word, guessed_letters, len(stages) - attempts - 1)
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            time.sleep(1)
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            time.sleep(1)
            continue
        
        guessed_letters.add(guess)
        
        if guess not in word:
            attempts -= 1
        
        if all(letter in guessed_letters for letter in word):
            display_game(word, guessed_letters, len(stages) - attempts - 1, final=True)
            print("Congratulations! You've guessed the word.")
            return
        
    display_game(word, guessed_letters, len(stages) - attempts - 1, final=True)
    print("Game over! The word was: " + word)

def main():
    words = ["hangman", "python", "programming", "challenge"]
    play_again = True
    
    while play_again:
        word = random.choice(words)
        hangman(word)
        
        play_again = input("Do you want to play again? (y/n): ").lower() == 'y'

if __name__ == "__main__":
    main()
