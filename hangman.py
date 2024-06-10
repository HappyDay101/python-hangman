
import random

words = ['python', 'java', 'kotlin', 'javascript', 'ruby', 'swift', 'r', 'scala', "c#", "c++", 'php', 'vb.net', 'sql', 'go', 'perl']

 ""# Randomly choose a word from the list
chosen_word = random.choice(words)
# Create a list of underscored
word_display = ['_' for _ in chosen_word]
attempts = 8

print("Welcome to Hangman!")

while attempts > 0 and '_' in word_display:
    print("\n" + ' '.join(word_display))
    guess = input("Guess a letter: ").lower()
    if guess in chosen_word:
        for index, letter in enumerate(chosen_word):
            if letter == guess:
                # reveal letter
                word_display[index] = guess
    else:
        print("That letter doesn't appear in the word!")
        attempts -= 1

# Game conclusion
if '_' not in word_display:
    print("You guess the word!")
    print(' '.join(word_display))
    print("You survived!!")
else:
    print("You ran out of attempts. The word was: " + chosen_word)
    print("You lost, Hanged!!")
