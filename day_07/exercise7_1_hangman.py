# Exercise 7.1 - Hangman
# from replit import clear
import random
import hangman_words
import hangman_art

print(hangman_art.logo)

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_words.word_list)

# print(f"Pssst, the solution is {chosen_word}.")
lives = 6

display = []
word_length = len(chosen_word)

# Update the display list with underscores to show to the user.
for letter in chosen_word:
    display.append("_")

end = False
while not end:
    # Ask for a letter
    guess = input("Guess a letter: ").lower()
    
    # Clear the code after every iteration. Does not work.
    # clear()
    
    # Check if the letter it was alredy guessed.
    if guess in display:
        print(f"You alredy guessed {guess}.")

    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        
        # Code to test if something goes wrong:
        # print( f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        
        # We add the letter in display in the same position as it is in the word.
        if letter == guess:
            display[position] = letter
    
    # Display if the user lose or win based on the display and lives.
    if "_" not in display:
        if lives != 0:
            end = True
            print("You win.")
        else:
            print("You lose.")

    # Give feedback if the letter is not in the word or if the state of display changes. 
    if guess not in chosen_word:
        print(f"You guessed {guess}, that's not in the word. \nYou lose a life.")
        lives -= 1
        if lives == 0:
            end = True
            print("You lose.")
    print(display)
    print(hangman_art.stages[lives])
