from flow import engine as en
from flow import story as st


def mulai_game():
    en.inisialisasi_game()

    return {
        "menu": "game",
        "prolog": st.ambil_prolog(),
        "hp_monster": en.game_state["monster"].hp,
        "turn": en.game_state["nomor_turn"]
    }