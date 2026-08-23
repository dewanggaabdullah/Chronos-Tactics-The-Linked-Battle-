from components import attributes as at
from components import characters as ch
from components.history import node as no


game_state = {
    "tim_pemain": {},
    "monster": None,
    "history": None,
    "nomor_turn": 0,
    "game_active": False,
    "karakter_aktif": None
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


def atur_karakter_turn(data):
    nama_karakter = str(
        data.get("karakter", "")
    ).lower()

    if nama_karakter not in game_state["tim_pemain"]:
        return {
            "berhasil": False,
            "log": "Karakter tidak ditemukan."
        }

    game_state["karakter_aktif"] = nama_karakter

    return {
        "berhasil": True,
        "karakter": nama_karakter,
        "log": f"{nama_karakter.capitalize()} siap bertindak."
    }


def serang(data):
    nama_karakter = str(
        data.get("karakter", "")
    ).lower()

    return {
        "berhasil": True,
        "log": f"{nama_karakter.capitalize()} menyerang."
    }


def gunakan_skill(data):
    nama_karakter = str(
        data.get("karakter", "")
    ).lower()

    nama_skill = str(
        data.get("skill", "")
    ).lower()

    return {
        "berhasil": True,
        "log": (
            f"{nama_karakter.capitalize()} "
            f"menggunakan {nama_skill}."
        )
    }


def kabur(data=None):
    game_state["game_active"] = False

    return {
        "berhasil": True,
        "log": "Kamu melarikan diri!"
    }
