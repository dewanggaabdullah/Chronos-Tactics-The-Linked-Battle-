from flow import attributes as at
from flow import characters as ch
from flow.history import node as no


# ============================================================
# GAME STATE
# ============================================================

game_state = {
    "tim_pemain": {},
    "monster": None,
    "history": None,
    "nomor_turn": 0,
    "karakter_aktif": None,
    "game_active": False,
    "fase": "menu"
}


# ============================================================
# GAME SETUP
# ============================================================

def inisialisasi_game():
    """
    Membuat state awal permainan.

    Fungsi ini dipanggil ketika pemain menekan
    tombol 'Mulai' dari menu utama.
    """

    global game_state

    game_state["tim_pemain"] = {}
    game_state["monster"] = at.Monster(
        "ORC GURUN",
        250
    )
    game_state["history"] = no.TurnHistory()
    game_state["nomor_turn"] = 1
    game_state["karakter_aktif"] = None
    game_state["game_active"] = True
    game_state["fase"] = "pemilihan"

    return "Game Dimulai!"


# ============================================================
# PEMILIHAN KARAKTER
# ============================================================

def pilih_karakter(nama_karakter):
    """
    Menambahkan atau membatalkan karakter dari tim pemain.

    Klik pertama:
        Karakter ditambahkan.

    Klik kedua:
        Karakter dibatalkan.

    Maksimal:
        3 karakter.
    """

    global game_state

    if not game_state["game_active"]:
        return {
            "berhasil": False,
            "log": "Game belum dimulai."
        }

    if game_state["fase"] != "pemilihan":
        return {
            "berhasil": False,
            "log": "Pemilihan karakter sudah dikunci."
        }

    nama_karakter = str(nama_karakter).lower()

    if not ch.validasi_karakter(nama_karakter):
        return {
            "berhasil": False,
            "log": "Karakter tidak valid."
        }

    tim_pemain = game_state["tim_pemain"]

    # --------------------------------------------------------
    # BATALKAN KARAKTER
    # --------------------------------------------------------

    if nama_karakter in tim_pemain:
        del tim_pemain[nama_karakter]

        return {
            "berhasil": True,
            "dipilih": False,
            "log": f"{nama_karakter.capitalize()} dibatalkan.",
            "karakter": nama_karakter,
            "jumlah_tim": len(tim_pemain)
        }

    # --------------------------------------------------------
    # BATAS TIM
    # --------------------------------------------------------

    if len(tim_pemain) >= 3:
        return {
            "berhasil": False,
            "dipilih": False,
            "log": "Tim sudah penuh. Maksimal 3 karakter.",
            "karakter": nama_karakter,
            "jumlah_tim": len(tim_pemain)
        }

    # --------------------------------------------------------
    # TAMBAHKAN KARAKTER
    # --------------------------------------------------------

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


# ============================================================
# MULAI PERTARUNGAN
# ============================================================

def siap_bertarung():
    """
    Mengunci pemilihan karakter dan memulai pertarungan.
    """

    global game_state

    if not game_state["game_active"]:
        return {
            "berhasil": False,
            "log": "Game belum dimulai."
        }

    if game_state["fase"] != "pemilihan":
        return {
            "berhasil": False,
            "log": "Pemilihan karakter sudah selesai."
        }

    tim_pemain = game_state["tim_pemain"]

    if len(tim_pemain) != 3:
        return {
            "berhasil": False,
            "log": "Kamu harus memilih 3 karakter."
        }

    # --------------------------------------------------------
    # SETUP STATISTIK KARAKTER
    # --------------------------------------------------------

    for karakter in tim_pemain.values():

        if hasattr(
            karakter,
            "setup_statistik_awal"
        ):
            karakter.setup_statistik_awal()

    # --------------------------------------------------------
    # PINDAH KE FASE PERTARUNGAN
    # --------------------------------------------------------

    game_state["fase"] = "pertarungan"

    return {
        "berhasil": False,
        "log": "TES: Tombol Siap berhasil mencapai engine."
    }

    '''
    "berhasil": True,
    "log": "Pertarungan dimulai!",
    "tim": list(tim_pemain.keys()),
    "jumlah_tim": len(tim_pemain),
    "monster": game_state["monster"].nama,
    "hp_monster": game_state["monster"].hp,
    "turn": game_state["nomor_turn"]
    '''
    '''}'''


# ============================================================
# PERTARUNGAN
# ============================================================

def proses_aksi(aksi):
    """
    Memproses satu aksi selama pertarungan.
    """

    global game_state

    # --------------------------------------------------------
    # VALIDASI GAME
    # --------------------------------------------------------

    if not game_state["game_active"]:
        return {
            "berhasil": False,
            "log": "Game belum dimulai atau sudah selesai."
        }

    if game_state["fase"] != "pertarungan":
        return {
            "berhasil": False,
            "log": "Pertarungan belum dimulai."
        }

    # --------------------------------------------------------
    # AMBIL STATE PERTARUNGAN
    # --------------------------------------------------------

    tim = game_state["tim_pemain"]
    monster = game_state["monster"]
    history = game_state["history"]

    # --------------------------------------------------------
    # CATAT TURN
    # --------------------------------------------------------

    history.catat_turn(
        game_state["nomor_turn"],
        tim,
        monster
    )

    # --------------------------------------------------------
    # AKTIFKAN PASSIVE
    # --------------------------------------------------------

    for karakter in tim.values():

        if (
            karakter.hp > 0
            and hasattr(karakter, "aktifkan_pasif")
        ):
            karakter.aktifkan_pasif(tim)

    # --------------------------------------------------------
    # PROSES AKSI
    # --------------------------------------------------------

    pesan = ""

    # Kabur
    if aksi == "kabur":

        game_state["game_active"] = False
        game_state["fase"] = "selesai"

        return {
            "berhasil": True,
            "log": "Kamu melarikan diri!"
        }

    # Menu game
    if aksi == "1":

        pesan = (
            "Game sedang berjalan! "
            "Silakan lakukan aksi berikutnya."
        )

    # Settings
    elif aksi == "2":

        pesan = "Menu Settings belum tersedia."

    # Karakter menyerang
    elif aksi in tim:

        karakter = tim[aksi]

        if karakter.hp <= 0:

            pesan = "Karakter tersebut sudah mati!"

        else:

            if (
                hasattr(karakter, "skill_pasif")
                and karakter.skill_pasif
            ):
                pesan = karakter.menyerang(monster)

            else:
                karakter.skill_aktif(
                    monster=monster,
                    tim_pemain=tim
                )

                pesan = (
                    f"{karakter.nama} "
                    f"menggunakan skill aktif!"
                )

            # Monster melakukan serangan balik
            if monster.hp > 0:

                pesan += " | Monster menyerang balik!"

                monster.menyerang(karakter)

            game_state["nomor_turn"] += 1

    else:

        pesan = f"Aksi '{aksi}' diterima oleh server."

    # --------------------------------------------------------
    # CEK KEMENANGAN
    # --------------------------------------------------------

    if monster.hp <= 0:

        game_state["game_active"] = False
        game_state["fase"] = "selesai"

        pesan += " Kamu Menang!"

    return {
        "berhasil": True,
        "log": pesan,
        "turn": game_state["nomor_turn"],
        "hp_monster": monster.hp
    }