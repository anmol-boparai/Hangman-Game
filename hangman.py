import random
from collections import Counter

def load_words(filename='words.txt'):
    """Load words from a file."""
    try:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
            return [word.strip().lower() for word in words if word.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed."""
    display = []
    for letter in word:
        if letter in guessed_letters:
            display.append(letter)
        else:
            display.append('_')
    return ' '.join(display)

def play_game():
    """Main game loop."""
    words = load_words()
    if not words:
        print("No words available. Exiting.")
        return

    word = random.choice(words)
    guessed_letters = set()
    chances = len(word) + 2
    print("Guess the word! HINT: It's a random word from the dictionary.")
    print(display_word(word, guessed_letters))

    while chances > 0:
        guess = input("\nEnter a letter to guess: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Correct!")
        else:
            print("Wrong!")
            chances -= 1
        
        current_display = display_word(word, guessed_letters)
        print(current_display)
        
        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations, You won!")
            print(f"The word was: {word}")
            return
    
    print("\nYou lost! Try again.")
    print(f"The word was: {word}")

if __name__ == '__main__':
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Bye!")
