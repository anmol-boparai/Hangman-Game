# 🎮 Hangman Game in Python

A classic Hangman game implemented in Python with ASCII art visualization and smart hints system. Perfect for learning Python or just having fun!

## Features ✨

- 🖼️ Interactive ASCII art hangman that progresses with wrong guesses
- 💡 Smart hint system (word length, starting/ending letters, vowel count)
- 📖 Loads words from external file (`words.txt`) - fully customizable
- ✅ Input validation and error handling
- 📊 Tracks remaining guesses
- 🏆 Win/loss conditions with revealed word
- ⌨️ Keyboard interrupt handling

## Customization ⚙️
To add your own words:
 - Edit words.txt - add one word per line
 - Save the file
 - Run the game again

To adjust difficulty:
 - Modify max_wrong_guesses in the code
 - Change max_hints value for more/less help
   
## Installation 

Requires Python 3 and terminal.

```bash
python3 hangman.py
