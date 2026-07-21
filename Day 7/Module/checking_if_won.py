import random
word_list = ["jambu", "mangga", "alpukat"]
chosen_word = random.choice(word_list)
print(chosen_word) 

placeholder = ""
word_lenght = len(chosen_word)
for position in range(word_lenght):
    placeholder += "_"
print(placeholder)

#TODO-1 : Use a while loop to let the user guess again
game_over = False
corret_letter = []

while not game_over:
    guess = input("Guess a letter : ").lower()

    display = ""

# TODO-2 : Change the for loop so that you keep the previous correct letters in display

    for letter in chosen_word:
        if letter == guess:
            display += letter
            corret_letter.append(guess)
        elif letter in corret_letter:
            display += letter
        else:
            display += "_"

    print(display)

    if "_" not in display:
        game_over = True
        print("You Win!")

