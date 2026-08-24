from flow import menu
from flow import game_menu
from flow import settings_menu


ACTION_HANDLERS = {
    "mulai": menu.mulai_game,

    "pilih_karakter": menu.pilih_karakter,
    "siap": menu.siap_bertarung,
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
