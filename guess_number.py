'''
Number guessing game
'''

number = 10

print("I'm thinking of a number...")
guess = input("What number am I thinking of? Enter q to give up. ")

again = True
while again:

    if guess == 'q':
        print(f"Thanks for trying! The number was {number}")
        again = False

    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        again = False

    else:
        print(f"Sorry! That's the wrong number. Try again! ")
        guess = input("What number am I thinking of? Enter q to give up. ")