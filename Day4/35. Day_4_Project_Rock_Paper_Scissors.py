print("What dou you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.")
import random  
user_choice = int(input("Your choice: "))
computer_choice = random.randint(0, 2)
choices = ["Rock", "Paper", "Scissors"]
print(f"Your choice: {choices[user_choice]}")
print(f"Computer choice: {choices[computer_choice]}")
if user_choice == computer_choice:
    print("It's a draw.")
elif (user_choice == 0 and computer_choice == 2) or (user_choice == 1 and computer_choice == 0) or (user_choice == 2 and computer_choice == 1):
    print("You win!")
elif (user_choice >=3 or user_choice < 0):
    print("Invalid Number. Please try again.")    
else:  
    print("You lose.")
# Compare this snippet from Day4/32.Understanding_the_Offset_and_Appending_Items_to_Lists.py:   
# '''
# New_List=["apple","banana","cherry"]
# New_List[0]="kiwi" # change the first item
# print(f"{New_List[-2]}") # ['kiwi', 'banana', 'cherry']
# New_List.append("orange") # add to the end of the list
# print(f"{New_List}") # ['kiwi', 'banana', 'cherry', 'orange']
# '''
# fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
# vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]