import random
stages = ['''
 +---+
 |   |
 O   |
/|\  |
/ \  |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|\  |
/    |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|\  |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
/|   |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
 |   |
     |
     |
=========
''', '''
 +---+
 |   |
 O   |
     |
     |
     |
=========
''', '''
 +---+
 |   |
     |
     |
     |
     |
=========
''']
#TODO-1 : Creat a variable called 'lives' to keep track of the number of lives left. Set lives to equal 6.
lives = 6

word_list = ["jambu", "mangga", "alpukat"]
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
    guess = input("Guess a letter : ").lower()

    display = ""


    for letter in chosen_word:
        if letter == guess:
            display += letter
            corret_letter.append(guess)
        elif letter in corret_letter:
            display += letter
        else:
            display += "_"

    print(display)

    #TODO-2 : If guess is not a letter in the chosen_word, Then reduce lives by 1. 
    # if lives goes down to 0 then the game should end, and it should print "you lose"
    if guess not in chosen_word:
        lives -= 1
        if lives == 0:
            game_over = True
            print("You Lose!")
    if "_" not in display:
        game_over = True
        print("You Win!")

#TODO-3 : Print the ASCII art from the list stages that corresponds to the current number of lives the useer has remaining.

    print(stages[lives])