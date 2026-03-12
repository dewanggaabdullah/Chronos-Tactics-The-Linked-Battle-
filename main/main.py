import character_choose as cc
import utillities as ut

def game_loop():
    while True:
        ut.bersihkan_terminal()
        
        print("╔══════════════════╗")
        print("║   GAME MENU      ║")
        print("╠══════════════════╣")
        print("║ 1. Mulai         ║")
        print("║ 2. Options       ║")
        print("║ 3. Keluar        ║")
        print("╚══════════════════╝")
        
        pilih = input("\nPilih (1-3): ")
        
        if pilih == '1':
            ut.clear_vscode_terminal()
            print("Game dimulai!")
            print("Selamat bermain...")
            cc.pilih_karakter()
            input("\nTekan Enter  buat kembali ke menu")
            
        elif pilih == '2':
            #ini gak ada gunanya,hanya formalitas,mungkin nanti dikembangkan
            ut.clear_vscode_terminal()
            print("=== SETTINGS ===")
            print("1. Difficulty: indonesia")
            print("2. Sound: On")
            input("\nTekan Enter untuk kembali ke menu")
            
        elif pilih == '3':
            ut.clear_vscode_terminal()
            print("Bye bye!")
            break

game_loop()