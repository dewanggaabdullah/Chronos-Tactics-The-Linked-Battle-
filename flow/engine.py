from flow import units as un
from flow import character_choise as cc
from flow import utills as ut

def jalankan_game():
    pengenalan_char = cc.cerita_karakter
    pilihan_karakter = cc.validasi_karakter()

    print(pengenalan_char)
    print(pilihan_karakter)

    while True:
        for hero in pilihan_karakter.values():
            hero.hp = hero.max_hp

    print('\n' + '='*30)
    print('PERTARUNGAN DIMULAI')
    print('='*30)

    print('pilih siapa yang akan menyerang o=|:::>')


def game_dimulai():
    ut.bersihkan_terminal()
    print('=== PEMILIHAN KARAKTER ===')
    print('silahkan pilih 3 dari teman kita untuk dibawa berpetualang...')
    print()
    jalankan_game()

