# This program will check if the number is even or odd
print("Please enter any number from 1 to 10")
Num = int(input("Enter your number here: "))

if 1 <= Num <= 10:  # Ensuring the number is within the valid range
    if Num % 2 == 0:
        print("Your number is even")
    else:
        print("Your number is odd")
else:
    print("Number is not in the range of 1 to 10")
