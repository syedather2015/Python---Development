print("Welcome to python pizza deliveries!")
size=input("What size pizza do you want? S, M, or L: ")
add_pepperoni=input("Do you want pepperoni? Y or N: ")
extra_cheese=input("Do you want extra cheese? Y or N: ")

if size=="S":
    bill=15
elif size=="M":
    bill=20
elif size=="L":
    bill=25
else:
    print("Invalid size")
    bill=0
if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese=="Y":   
    bill+=1
print(f"Your final bill is: ${bill}")
# The code above is a simple pizza ordering program that calculates the total bill based on the size of the pizza, whether pepperoni is added, and if extra cheese is requested. It uses conditional statements to determine the base price and any additional charges. The final bill is printed at the end.