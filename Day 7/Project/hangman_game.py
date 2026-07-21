import random
#TODO-1 : Update the word list to use the 'word_list' from hangman_words.py
from hangman_words import word_list
from hangman_art import logo, stages
lives = 6

#TODO-3 : Import the logo from hangman_art.py and print it at the start of the game 
print(logo)
chosen_word = random.choice(word_list)
print(chosen_word) 

placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

game_over = False
corret_letter = []

while not game_over:

    # TODO-6 : Update the code below to tell the user how many lives they have left.
    print(f"**********{lives}/6 LIVES LEFT**********")
    guess = input("Guess a letter : ").lower()

    #TODO-4 : If user has entered a letter they've already guessed, print the letter and let them know.
    if guess in corret_letter:
        print(f"You've already guessed {guess}")
    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            corret_letter.append(guess)
        elif letter in corret_letter:
            display += letter
        else:
            display += "_"

    print("Word to guess: " + display)

    # TODO-5 : 

    if guess not in chosen_word:
        lives -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life.")

        if lives == 0:
            game_over = True
            # TODO-7 : 
            print(f"**********IT WAS {chosen_word}! YOU LOSE!**********")
    if "_" not in display:
        game_over = True
        print("**********You Win!**********")

    # TODO-2 : Update the code to use the stages from the life hangman_art.py 
    print(stages[lives])