from main_menu import character_choose as cc
from flow import utills as ut

def game_loop():
    while True:
        print('==={ CRONOS TACTICS: The Linked Battle }===')
        print()
        print("         ╔══════════════════╗")
        print("         ║   GAME MENU      ║")
        print("         ╠══════════════════╣")
        print("         ║ 1. Mulai         ║")
        print("         ║ 2. Options       ║")
        print("         ║ 3. Keluar        ║")
        print("         ╚══════════════════╝")

        print('\npilih angka pada nomor diatas sebagai input...')
        pilih = input("Pilih (1-3): ")
        
        if pilih == '1':
            ut.bersihkan_terminal()
            print("Game dimulai!")
            print("Selamat bermain...")
            cc.pilih_karakter()
            input("\nTekan Enter saja buat kembali ke menu")
            
        elif pilih == '2':
            #ini gak ada gunanya,hanya formalitas,mungkin nanti dikembangkan
            ut.bersihkan_terminal()
            print("=== SETTINGS ===")
            print("1. Difficulty: indonesia")
            print("2. Sound: Off")
            input("\nTekan Enter untuk kembali ke menu: ")
            
        elif pilih == '3':
            ut.bersihkan_terminal()
            print("Bye bye!\n")
            break

game_loop()