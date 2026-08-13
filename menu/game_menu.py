from flow import engine as en


def proses_aksi(aksi):
    hasil_log = en.proses_aksi(aksi)

    monster = en.game_state.get("monster")
    hp_monster = monster.hp if monster else 0

    return {
        "menu": "game",
        "log": hasil_log,
        "hp_monster": hp_monster,
        "turn": en.game_state.get("nomor_turn", 1)
    }