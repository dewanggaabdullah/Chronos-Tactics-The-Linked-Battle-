from flow import units as un
from flow import character_choice as cc
from flow import utils as ut

def inisialisasi_karakter():
    cc.cerita_karakter()
    karakter = cc.validasi_karakter()

    if karakter in un.pilihan_karakter:
        tim_pemain = un.pilihan_karakter[karakter]
    else:
        print('karakter tidak ditemukan')

def jalankan_game():
    pass


def game_dimulai():
    ut.bersihkan_terminal()
    print('=== PEMILIHAN KARAKTER ===')
    print('silahkan pilih 3 dari teman kita untuk dibawa berpetualang...')
    print()
    jalankan_game()

