import random

randomNumber = random.randint(1, 3)
print('I am thinking of a number between 1 and 20. Try to guess the number!')

guess = 0

for i in range(5):

    print('You have ' + str(5 - i) + ' guesses remaining.')
    guess = int(input())

    if guess == 69:
        print('NICE! But wrong, try again!')
    elif guess == 420:
        print('HeEeEey... Smoke weed every day. Nope, try again!')
    elif guess < randomNumber:
        print('Your guess is too low. Try again!')
    elif guess > randomNumber:
        print('Your guess is too high. Try again!')
    elif guess == randomNumber:
        print('Congratulations! You guessed the number in ' + str(i + 1) +
        ' tries!')
        break

if guess != randomNumber:
    print('Sorry, you ran out of guesses...')
