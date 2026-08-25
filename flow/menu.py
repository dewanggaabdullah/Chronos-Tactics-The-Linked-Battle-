from components import story as st
from components import characters as ch
from flow import game_menu


game_state = {
    "tim_pemain": {},
    "game_active": False
}


def mulai_game(data=None):
    game_state["tim_pemain"] = {}
    game_state["game_active"] = True

    return {
        "menu": "game",
        "prolog": st.ambil_prolog()
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

    karakter = ch.pemilihan_karakter(nama_karakter)
    tim_pemain.update(karakter)

    return {
        "berhasil": True,
        "dipilih": True,
        "log": f"{nama_karakter.capitalize()} berhasil dipilih.",
        "karakter": nama_karakter,
        "jumlah_tim": len(tim_pemain)
    }


def siap_bertarung(data=None):
    tim_pemain = game_state["tim_pemain"]

    if len(tim_pemain) != 3:
        return {
            "berhasil": False,
            "log": "Pilih tepat 3 karakter sebelum bertarung."
        }

    hasil = game_menu.mulai_battle(tim_pemain)

    return {
        "berhasil": True,
        "log": "Tim siap bertarung.",
        "battle": hasil
    }
