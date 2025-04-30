import random
from words import hangman_words  
import string 

def get_valid_word(words):
    word = random.choice(words)
    while '-' in word or ' ' in word:
        word = random.choice(words)
    return word.upper()

def hangman():
    word = get_valid_word(hangman_words)
    word_letters = set(word)  # letters to guess
    alphabet = set(string.ascii_uppercase)
    used_letters = set()      # letters the user has guessed

    while len(word_letters) > 0:
        print("\nYou have used these letters:", ' '.join(sorted(used_letters)))

        # Show current word progress
        word_list = [letter if letter in used_letters else '-' for letter in word]
0        print("Current word:", ' '.join(word_list))

        # Get user input
        user_letter = input("Guess a letter: ").upper()
        
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                print("Correct!")
            else:
                print("Wrong guess.")
        elif user_letter in used_letters:
            print("You have already used that letter. Please try again.")
        else:
            print("Invalid character. Please try again.")

    print(f"\nYou guessed the word: {word} 🎉")

# Start the game
hangman()
