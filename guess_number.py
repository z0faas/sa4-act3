'''
Number guessing game
'''

number = 10

print("I'm thinking of a number...")
print('You have 5 guesses to get the correct number!')
guess = input("What number am I thinking of? Enter q if you give up. ")

guess_amount = 5
again = True
while again: # keep looping and allowing user to guess until again becomes False

    if guess == 'q': # if the user quits
        print(f"Thanks for trying! The number was {number}")
        again = False

    elif int(guess) == number: # if the user guesses correctly
        print("Congratulations! You guessed the right number.")
        again = False

    else: # if the user guesses incorrectly
        print('Incorrect')
        guess_amount -= 1

        if guess_amount == 0:
            print(f"Sorry! You've run out of guesses! The number was {number}")
            again = False # breaks out of the loop
        else: 
            print(f"You have {guess_amount} guess(es) remaining.")

            if int(guess) < number:
                print('Hint: Your guess is too low. Try a higher number.')

            elif int(guess) > number:
                print('Hint: Your guess is too high. Try a lower number.')

            guess = input("What number am I thinking of? Enter q to give up. ")     