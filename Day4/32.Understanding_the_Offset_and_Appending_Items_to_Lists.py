
New_List=["apple","banana","cherry"]
New_List[0]="kiwi" # change the first item
print(f"{New_List[-2]}") # ['kiwi', 'banana', 'cherry']
New_List.append("orange") # add to the end of the list
print(f"{New_List}") # ['kiwi', 'banana', 'cherry', 'orange']

fruits = ["Strawberries", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears"]
vegetables = ["Spinach", "Kale", "Tomatoes", "Celery", "Potatoes"]
 
dirty_dozen = [fruits, vegetables]
 
print(dirty_dozen[1][1])