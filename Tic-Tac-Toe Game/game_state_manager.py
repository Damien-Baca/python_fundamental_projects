import main_menu
import single_player
import multi_player


STATE_MAIN_MENU = 'GAME_STATE_MAIN_MENU'
STATE_SINGLE_PLAYER = 'GAME_STATE_SINGLE_PLAYER'
STATE_MULTI_PLAYER = 'GAME_STATE_MULTI_PLAYER'

current_game_state = STATE_MAIN_MENU
previous_game_state = STATE_MAIN_MENU
next_game_state = STATE_MAIN_MENU

update = main_menu.update


def change_gamestate():
    if current_game_state == STATE_MAIN_MENU:
        pass
    #    update = main_menu.update
    elif current_game_state == STATE_SINGLE_PLAYER:
        pass
    #    update = single_player.update
    elif current_game_state == STATE_MULTI_PLAYER:
        pass
    #    update = multi_player.update
