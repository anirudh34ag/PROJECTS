import random

def guess(x):
    random_number = random.randint(1,x)
    guess = 0
    Tries = 0
    while guess != random_number:
        guess = int(input(f'Guess a number between 1 and {x} : '))
        Tries += 1
        if guess < random_number:
            print('Sorry, guess again. Too low.')
        elif guess > random_number:
            print('Sorry, guess again. Too high.')

    print(f'Yay, congrats. You have guessed the number {random_number} correctly')
    print("Number of tries: ",Tries)
    
    
x = int(input(f'Number you want to guess between : '))
guess(x)
