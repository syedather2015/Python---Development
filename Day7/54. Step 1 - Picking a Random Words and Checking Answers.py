#T0D0-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
#T0D0-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
#T0D0-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word
#T0D0-4 - If it is, print "Right!" and if it isn't, print "Wrong!".
import random
word_list = ["aardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(f"chosen_word is: {chosen_word}") # Debugging line
palceholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    palceholder += "_"
print(palceholder)
guess = input("Guess a letter: ").lower()
display = ""
for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)