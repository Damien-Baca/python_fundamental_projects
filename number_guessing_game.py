import random


def number_guessing_game(min=1, max=100):
    target_number = random.randint(min, max+1)

    while True:
        try:
            guess = int(input(f'Guess the number between {min} and {max}: '))
            if guess > target_number:
                print('Too high!')
            elif guess < target_number:
                print('Too low!')
            else:
                print('Congratulations! You guessed the number.')
                break
        except ValueError:
            print('Please enter a valid number.')


number_guessing_game(1, 100)
# number_guessing_game(-50, 50)
