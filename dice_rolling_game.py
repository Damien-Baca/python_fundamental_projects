import random


def dice_rolling_game(num_sides=6, num_dice=2):
    counter = 0
    while True:
        command = input('Roll the dice? (y/n): ').strip().lower()
        if command == 'y':
            dice_rolls = []
            [dice_rolls.append(random.randint(1, num_sides))
             for _ in range(num_dice)]

            counter += num_dice
            print(tuple(dice_rolls))
        elif command == 'n':
            print(f'Thanks for playing! You rolled {counter} dice!')
            break
        else:
            print('Invalid Choice!')


dice_rolling_game()
