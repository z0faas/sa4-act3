'''
Number guessing game
'''

number = 10

print("I'm thinking of a number...")
print('Beware! There are a limited amount of guesses!')
guess = input("What number am I thinking of? Enter q if you give up. ")

guess_amount = 5
again = True
while again:

    if guess == 'q':
        print(f"Thanks for trying! The number was {number}")
        again = False

    elif int(guess) == number:
        print("Congratulations! You guessed the right number.")
        again = False

    else:
        if guess_amount != 1:
            print(f"Sorry! That's the wrong number. Try again! ")

        if guess_amount > 1:
            print(f"You have {guess_amount} guesses remaining.")
            guess_amount -= 1
            guess = input("What number am I thinking of? Enter q to give up. ")
        
        elif guess_amount == 1:
            print(f"You have 1 guess remaining. Be careful!")
            guess_amount -= 1
            guess = input("What number am I thinking of? Enter q to give up. ")

        else:
            print(f"Sorry! You've run out of guesses! The number was {number}")
            again = False