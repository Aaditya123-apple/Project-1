import random
print('Number Guessing Game')
Number=random.randint(1,100)
Chances=0
print('Guess a number between 1 and 100')
while Chances < 15:
    Guess=int(input('Enter your guess: '))
    if Guess==Number:
        print('Congrats, you won!!')
        break

    elif Guess>Number:
        print('Your guess is too high, guess a lower number')

    else:
        print('Your guess is too low, guess a higher number')

    Chances=Chances+1

if not Chances<5:
    print('You loss, the number was',Number)
