from flow import units as un
from flow import char_choice as cc
from flow import utils as ut
from flow import story as st
from history import node as no
import copy

game_state = {
    "tim_pemain": None,
    "monster": None,
    "history": None,
    "nomor_turn": 1,
    "game_active": False
}


def inisialisasi_game():
    global game_state
    daftar_karakter = cc.validasi_karakter()
    if daftar_karakter:
        game_state["tim_pemain"] = cc.pemilihan_karakter(*daftar_karakter)
        game_state["monster"] = un.Monster('ORC GURUN', 250)
        game_state["history"] = no.TurnHistory()
        game_state["nomor_turn"] = 1
        game_state["game_active"] = True
        
        for karakter in game_state["tim_pemain"].values():
            karakter.setup_statistik_awal()
        return "Game Dimulai!"
    return "Gagal inisialisasi karakter."


def proses_aksi(aksi):
    global game_state
    if not game_state["game_active"]:
        return "Game belum dimulai."

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

    if aksi in tim:
        karakter = tim[aksi]
        if karakter.hp > 0:
            # Eksekusi Aksi
            if karakter.skill_pasif:
                pesan = karakter.menyerang(monster)
            else:
                karakter.skill_aktif(monster=monster, tim_pemain=tim)
            
            # Balasan Monster
            if monster.hp > 0:
                pesan += f" | Monster menyerang {karakter.nama}!"
                monster.menyerang(karakter)
            
            game_state["nomor_turn"] += 1
        else:
            pesan = "Karakter sudah mati!"
    else:
        pesan = "Aksi tidak dikenal."

    # Cek Kondisi Menang/Kalah
    if monster.hp <= 0:
        game_state["game_active"] = False
        pesan += " Kamu Menang!"
        
    return pesan