import random

HANGMAN_ART = [
    """
    +---+
        |
        |
        |
       ===
    """,
    """
    +---+
    O   |
        |
        |
       ===
    """,
    """
    +---+
    O   |
    |   |
        |
       ===
    """,
    """
    +---+
    O   |
   /|   |
        |
       ===
    """,
    """
    +---+
    O   |
   /|\  |
        |
       ===
    """,
    """
    +---+
    O   |
   /|\  |
   /    |
       ===
    """,
    """
    +---+
    O   |
   /|\  |
   / \  |
       ===
    """
]

def load_words(filename='words.txt'):
    """Load words from a file."""
    try:
        with open(filename, 'r') as file:
            words = file.read().splitlines()
            return [word.strip().lower() for word in words if word.strip()]
    except FileNotFoundError:
        print(f"Error: {filename} not found.")
        return []

def get_hint(word):
    """Generate a random hint."""
    hints = [
        f"The word has {len(word)} letters.",
        f"It starts with '{word[0]}'.",
        f"It ends with '{word[-1]}'.",
        f"It has {sum(1 for char in word if char in 'aeiou')} vowels."
    ]
    return random.choice(hints)

def display_word(word, guessed_letters):
    """Display the word with guessed letters revealed."""
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    """Main game loop."""
    words = load_words()
    if not words:
        print("No words available. Exiting.")
        return

    word = random.choice(words)
    guessed_letters = set()
    wrong_guesses = 0
    max_wrong_guesses = len(HANGMAN_ART) - 1
    used_hints = 0
    max_hints = 2

    print("\n=== Welcome to Hangman! ===")
    print("Guess the word! Type 'hint' for a clue.")
    print(HANGMAN_ART[wrong_guesses])
    print("\nWord:", display_word(word, guessed_letters))

    while wrong_guesses < max_wrong_guesses:
        guess = input("\nEnter a letter (or 'hint'): ").lower().strip()

        if guess == 'hint':
            if used_hints < max_hints:
                print("\nHint:", get_hint(word))
                used_hints += 1
            else:
                print("No more hints left!")
            continue

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
            wrong_guesses += 1

        print(HANGMAN_ART[wrong_guesses])
        print("\nWord:", display_word(word, guessed_letters))
        print(f"Wrong guesses left: {max_wrong_guesses - wrong_guesses}")

        if all(letter in guessed_letters for letter in word):
            print("\nCongratulations, You won!")
            print(f"The word was: {word}")
            return

    print("\nGame Over! You lost.")
    print(f"The word was: {word}")

if __name__ == '__main__':
    try:
        play_game()
    except KeyboardInterrupt:
        print("\nGame interrupted. Bye!")
