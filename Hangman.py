import random
import string

def load_words():
    with open("words.txt", "r") as file:
        wordlist = file.readline().strip().split()
    return wordlist

def choose_word(wordlist):
    return random.choice(wordlist)

def is_word_guessed(secret_word, letters_guessed):
    return all(letter in letters_guessed for letter in secret_word)

def get_guessed_word(secret_word, letters_guessed):
    return ''.join(letter if letter in letters_guessed else '-' for letter in secret_word)

def get_available_letters(letters_guessed):
    return ''.join(letter for letter in string.ascii_lowercase if letter not in letters_guessed)

def hangman(secret_word):
    print("Welcome to the game Hangman!")
    print(f"I am thinking of a word that is {len(secret_word)} letters long.")

    warnings = 3
    guesses = 10
    letters_guessed = []

    while guesses > 0 and not is_word_guessed(secret_word, letters_guessed):
        print("-" * 30)
        print(f"You have {guesses} guesses left.")
        print(f"Warnings left: {warnings}")
        print(f"Available letters: {get_available_letters(letters_guessed)}")
        guess = input("Please guess a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:  # Invalid input
            if warnings > 0:
                warnings -= 1
                print("Invalid input. You lose a warning.")
            else:
                guesses -= 1
                print("Invalid input. You lose a guess.")
        elif guess in letters_guessed:  # Already guessed
            if warnings > 0:
                warnings -= 1
                print("You've already guessed that letter. You lose a warning.")
            else:
                guesses -= 1
                print("You've already guessed that letter. You lose a guess.")
        else:  # Valid input
            letters_guessed.append(guess)
            if guess in secret_word:  # Correct guess
                print("Good guess:", get_guessed_word(secret_word, letters_guessed))
            else:  # Incorrect guess
                if guess in 'aeiou':
                    guesses -= 2
                    print("That letter is not in my word. You lose 2 guesses.")
                else:
                    guesses -= 1
                    print("That letter is not in my word. You lose 1 guess.")
                print("Current word:", get_guessed_word(secret_word, letters_guessed))

    print("-" * 30)
    if is_word_guessed(secret_word, letters_guessed):
        unique_letters = len(set(secret_word))
        score = guesses * unique_letters
        print("Congratulations, you won!")
        print(f"Your score is: {score}")
    else:
        print("Sorry, you ran out of guesses. The word was:", secret_word)

if __name__ == "__main__":
    wordlist = load_words()
    secret_word = choose_word(wordlist).lower()
    hangman(secret_word)
