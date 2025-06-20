import random

ROCK = 'r'
PAPER = 'p'
SCISSORS = 's'
YES = 'y'
NO = 'n'

continue_choices = (YES, NO)
game_choices = (ROCK, PAPER, SCISSORS)
choice_counter_picks = {ROCK: SCISSORS, SCISSORS: PAPER, PAPER: ROCK}
choice_display = {ROCK: 'rock \u270a',
                  PAPER: 'paper \u270b',
                  SCISSORS: 'scissors \u270c'}


def get_user_choice(game_choices):
    while True:
        user_choice = input(
            f'Rock, paper, or scissors? ({ROCK}/{PAPER}/{SCISSORS}): ')
        user_choice = user_choice.strip().lower()
        if user_choice in game_choices:
            return user_choice
        else:
            print('Invalid Choice!')


def print_game_result(user_choice, computer_choice):
    print(f'You chose {choice_display[user_choice]}')
    print(f'Computer chose {choice_display[computer_choice]}')
    if user_choice == computer_choice:
        print('Tie')
    elif choice_counter_picks[user_choice] == computer_choice:
        print('You win')
    else:
        print('You lose')


def get_continue_choice():
    while True:
        should_continue = input(f'Continue? ({YES}/{NO}): ').strip().lower()
        if should_continue in continue_choices:
            break
        else:
            print('Invalid Choice!')
    return should_continue


def rock_paper_scissors():

    while True:
        user_choice = get_user_choice(game_choices)
        computer_choice = random.choice(game_choices)

        print_game_result(user_choice, computer_choice)

        if get_continue_choice() == NO:
            break


rock_paper_scissors()
