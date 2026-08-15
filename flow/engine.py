from flow import attributes as un
from flow import characters as cc
from flow.history import node as no
import copy

game_state = {
    "tim_pemain": {},
    "monster": None,
    "history": None,
    "nomor_turn": 0,
    "game_active": False
}


def inisialisasi_game():
    global game_state
    
    # tim pemain masih dummy, karna masih tahap development(nanti dihapus)
    # Tim pemain akan diisi melalui pemilihan karakter di web.
    game_state["tim_pemain"] = {} # cc.pemilihan_karakter(*daftar_karakter)
    game_state["monster"] = un.Monster('ORC GURUN', 250)
    game_state["history"] = no.TurnHistory()
    game_state["nomor_turn"] = 1
    game_state["game_active"] = True
    
    # Setup statistik awal
    for karakter in game_state["tim_pemain"].values():
        if hasattr(karakter, 'setup_statistik_awal'):
            karakter.setup_statistik_awal()
            
    return "Game Dimulai!"


def proses_aksi(aksi):
    global game_state
    if not game_state["game_active"]:
        return "Game belum dimulai atau sudah selesai."

    tim = game_state["tim_pemain"]
    monster = game_state["monster"]
    history = game_state["history"]

    history.catat_turn(game_state["nomor_turn"], tim, monster)

    for char in tim.values():
        if char.hp > 0 and hasattr(char, 'aktifkan_pasif'):
            char.aktifkan_pasif(tim)

    pesan = ""
    if aksi == 'kabur':
        game_state["game_active"] = False
        return "Kamu melarikan diri!"
    if aksi == '1':
        pesan = "Game sedang berjalan! Silakan lakukan aksi berikutnya."
    elif aksi == '2':
        pesan = "Menu Settings belum tersedia."
    elif aksi in tim:
        karakter = tim[aksi]
        if karakter.hp > 0:
            if hasattr(karakter, 'skill_pasif') and karakter.skill_pasif:
                pesan = karakter.menyerang(monster)
            else:
                karakter.skill_aktif(monster=monster, tim_pemain=tim)
                pesan = f"{karakter.nama} menggunakan skill aktif!"
            
            if monster.hp > 0:
                pesan += f" | Monster menyerang balik!"
                monster.menyerang(karakter)
            
            game_state["nomor_turn"] += 1
        else:
            pesan = "Karakter tersebut sudah mati!"
    else:
        pesan = f"Aksi '{aksi}' diterima oleh server."

    if monster.hp <= 0:
        game_state["game_active"] = False
        pesan += " Kamu Menang!"
        
    return pesan