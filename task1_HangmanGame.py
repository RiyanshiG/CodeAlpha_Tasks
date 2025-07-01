import random

def choose_word():
    words = ["python", "hangman", "programming", "developer", "challenge"]
    return random.choice(words)

def display(word, guessed_letters):
    return ''.join(letter if letter in guessed_letters else '_' for letter in word)

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6

    print("Welcome to Hangman!")
    while attempts > 0:
        print("\nWord:", display(word, guessed_letters))
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess in word:
            guessed_letters.add(guess)
            if set(word) <= guessed_letters:
                print("Congratulations! You guessed the word:", word)
                break
        else:
            attempts -= 1
            print("Incorrect! You have", attempts, "attempts left.")

    if attempts == 0:
        print("Game over! The word was:", word)

hangman()
