import random
word_list=["aardvark","baboon","camel"]
# TOD0 - 1 - Randomly choose a word from the word_list and assign it to a variable called_chosen word then print it. 
chosen_word = random.choice(word_list)
print(chosen_word)
# TOD0 - 2 - Ask the user to guess the letter and assign their answer to variable called guess. Make sure lowercase.
guess = input("Guess a letter: ").lower()
print(guess)
# TOD0 - 3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_words. Print "Right" if it is, "Wrong" if it's not.
for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")
