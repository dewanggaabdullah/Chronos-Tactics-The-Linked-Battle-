from flow import story as st
from menu import game_menu


def mulai_game(data=None):
    game_menu.mulai_game()

    return {
        "menu": "game",
        "prolog": st.ambil_prolog(),
        "hp_monster": game_menu.game_state["monster"].hp,
        "turn": game_menu.game_state["nomor_turn"]
    }