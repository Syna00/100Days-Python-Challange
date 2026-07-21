import random
word_list = ["jambu", "mangga", "alpukat"]
chosen_word = random.choice(word_list)
print(chosen_word) 

# TODO-1 : Creat a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

guess = input("Guess a letter : ").lower()

# TODO-2 : creat a "display" that puts the guess letter in the right positions and _ in

display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"
print(display)

added = ""
for repeat in display:
    if repeat ==  