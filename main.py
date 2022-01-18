#Step 1
from hangman_art import logo, stages
from word_list import word_list
from replit import clear
import random

chosen_word = random.choice(word_list)
# print(f"{chosen_word}")
print(logo)
lives = 6
word_end = True
display = []
input_data = []
for _ in range(len(chosen_word)):
    display += "-"
print(display)

while word_end:
    guess = input("Guess a letter :").lower()
    clear()
    if guess in display:
        print(f"you've already guessed {guess}")
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
    if guess not in chosen_word:
        for i in guess:
          if guess not in input_data:
            input_data.append(guess)
        print(input_data)
        # print(f"you guess {guess}")
        lives -= 1
        if lives == 0:
          word_end = False
          print("You Loser")
        # else:
        #   print("wrong")
    print(display)
    if "-" not in display:
        word_end = False
        print("You Understand??")
    print(stages[lives])
