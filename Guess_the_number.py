import random

i = 3
n = random.randint(1, 10)
print("Guess the number b/w 1-10")
while i > 0:
    i -= 1
    guess = int(input("Enter the guessed number:"))
    if guess > n:
        print("guessed number is higher")
        print("you have", i, "Chances left")
    elif guess < n:
        print("guessed number is lower")
        print("you have", i, "Chances left")
    else:
        print("guessed number is correct")
        exit(0)
print("Max guessing chances over\nGenerated number will be:", n)
