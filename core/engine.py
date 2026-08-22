from menu import main_menu
from menu import game_menu
from menu import settings_menu


ACTION_HANDLERS = {
    "mulai": main_menu.mulai_game,

    "pilih_karakter": game_menu.pilih_karakter,
    "siap": game_menu.siap_bertarung,
    "atur_karakter_turn": game_menu.atur_karakter_turn,

    "serang": game_menu.serang,
    "skill": game_menu.gunakan_skill,
    "kabur": game_menu.kabur,

    "audio": settings_menu.audio,
    "grafis": settings_menu.grafis,
}


def proses_aksi(aksi, data=None):
    handler = ACTION_HANDLERS.get(aksi)

    if handler is None:
        return {
            "berhasil": False,
            "log": "Aksi tidak dikenal."
        }

    return handler(data)
