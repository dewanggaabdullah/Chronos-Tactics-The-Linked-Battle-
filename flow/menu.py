from components import story as st
from flow import game_menu


def mulai_game(data=None):
    game_menu.mulai_game()

    return {
        "menu": "game",
        "prolog": st.ambil_prolog(),
        "hp_monster": game_menu.game_state["monster"].hp,
        "turn": game_menu.game_state["nomor_turn"]
    }


def mulai_game(data=None):
    game
    game_state["tim_pemain"] = {}
    game_state["monster"] = at.Monster(
        "ORC GURUN",
        250
    )
    game_state["history"] = no.TurnHistory()
    game_state["nomor_turn"] = 1
    game_state["game_active"] = True
    game_state["karakter_aktif"] = None

    return {
        "menu": "game",
        "hp_monster": game_state["monster"].hp,
        "turn": game_state["nomor_turn"]
    }


def pilih_karakter(data):
    nama_karakter = str(
        data.get("karakter", "")
    ).lower()

    if not game_state["game_active"]:
        return {
            "berhasil": False,
            "log": "Game belum dimulai."
        }

    if not ch.validasi_karakter(nama_karakter):
        return {
            "berhasil": False,
            "log": "Karakter tidak valid."
        }

    tim_pemain = game_state["tim_pemain"]

    if nama_karakter in tim_pemain:
        del tim_pemain[nama_karakter]

        return {
            "berhasil": True,
            "dipilih": False,
            "log": f"{nama_karakter.capitalize()} dibatalkan.",
            "karakter": nama_karakter,
            "jumlah_tim": len(tim_pemain)
        }

    if len(tim_pemain) >= 3:
        return {
            "berhasil": False,
            "dipilih": False,
            "log": "Tim sudah penuh. Maksimal 3 karakter.",
            "karakter": nama_karakter,
            "jumlah_tim": len(tim_pemain)
        }

    karakter = ch.pemilihan_karakter(
        nama_karakter
    )

    tim_pemain.update(karakter)

    return {
        "berhasil": True,
        "dipilih": True,
        "log": f"{nama_karakter.capitalize()} berhasil dipilih.",
        "karakter": nama_karakter,
        "jumlah_tim": len(tim_pemain)
    }


def siap_bertarung():
    tim_pemain = game_state["tim_pemain"]

    if len(tim_pemain) != 3:
        return {
            "berhasil": False,
            "log": "Pilih tepat 3 karakter sebelum bertarung."
        }

    return {
        "berhasil": True,
        "log": "Tim siap bertarung.",
        "status": "Game masih dalam tahap development."
    }