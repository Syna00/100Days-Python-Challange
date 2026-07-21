import random
word_list = ["jambu", "mangga", "alpukat"]
# TODO-1 : randomly choose a word from the word_list and assign it to variable called chosen_word. Then print it
chosen_word = random.choice(word_list)
print(chosen_word) 


# TODO-2 : Ask the user guess a letter and asign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter : ").lower()
print(guess)


# TODO-3 : Check if the letter the user guessed (guess) is one of the letter in the choosen_word. Print "Right" if it is, "Wrong" if it's not
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

