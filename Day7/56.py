import random
word_list = ["aardvark","baboon","camel"]
chosen_word = random.choice(word_list)
print(chosen_word) # Debugging line
palceholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    palceholder += "_"
print(palceholder)

#Todo-1 - Use whileloop to let the user guess again.

guess = input("Guess a letter: ").lower()

display = ""

#Todo-2 - change the for loop so that you keep the previous correct letters in display.

for letter in chosen_word:
    if letter == guess:
        display += letter
    else:
        display += "_"

print(display)
