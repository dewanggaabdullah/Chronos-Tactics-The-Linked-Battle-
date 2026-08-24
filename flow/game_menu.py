from components import attributes as at
from components.history import node as no


game_state = {
    "tim_pemain": {},
    "monster": None,
    "history": None,
    "nomor_turn": 0,
    "game_active": False,
    "karakter_aktif": None
}


def mulai_battle(tim_pemain):
    game_state["tim_pemain"] = tim_pemain
    game_state["monster"] = at.Monster(
        "ORC GURUN",
        250
    )
    game_state["history"] = no.TurnHistory()
    game_state["nomor_turn"] = 1
    game_state["game_active"] = True
    game_state["karakter_aktif"] = None

    return {
        "hp_monster": game_state["monster"].hp,
        "turn": game_state["nomor_turn"]
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
