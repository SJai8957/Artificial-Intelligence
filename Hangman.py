#WAP to implement Hangman Game using Python

import random

def hangman():
    # List of words to choose from
    words = ["python", "programming", "artificial", "intelligence", "machine", "learning", "developer", "hangman"]
    
    # Randomly choose a word
    word = random.choice(words)
    guessed_word = ["_"] * len(word)  # Hidden word representation
    guessed_letters = []  # Keep track of guessed letters
    attempts = 6  # Total attempts allowed
    
    print("Welcome to Hangman Game!")
    print("Guess the word:")
    print(" ".join(guessed_word))
    
    while attempts > 0 and "_" in guessed_word:
        guess = input("\nEnter a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Please enter a single valid letter.")
            continue
        
        if guess in guessed_letters:
            print("⚠️ You already guessed that letter. Try another.")
            continue
        
        guessed_letters.append(guess)
        
        if guess in word:
            print(f"✅ Good guess! '{guess}' is in the word.")
            for i in range(len(word)):
                if word[i] == guess:
                    guessed_word[i] = guess
        else:
            attempts -= 1
            print(f"❌ Wrong guess! '{guess}' is not in the word. Attempts left: {attempts}")
        
        print(" ".join(guessed_word))
    
    if "_" not in guessed_word:
        print("\n🎉 Congratulations! You guessed the word:", word)
    else:
        print("\n💀 Game Over! The word was:", word)


# Run the game
if __name__ == "__main__":
    hangman()
