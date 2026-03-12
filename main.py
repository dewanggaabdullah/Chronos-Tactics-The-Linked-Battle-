import os
import subprocess

def clear_vscode_terminal():
    """Fungsi clear yang dioptimalkan untuk VS Code"""
    
    # Untuk Windows (biasanya default di VS Code)
    if os.name == 'nt':
        # Cara 1: cls command
        os.system('cls')
        
        # Atau cara 2: PowerShell specific (lebih bersih)
        # subprocess.run('Clear-Host', shell=True)
    
    # Untuk Mac/Linux
    else:
        os.system('clear')

# Contoh game sederhana di VS Code
def game_loop():
    while True:
        clear_vscode_terminal()
        
        print("╔══════════════════╗")
        print("║   GAME MENU      ║")
        print("╠══════════════════╣")
        print("║ 1. Mulai         ║")
        print("║ 2. Options       ║")
        print("║ 3. Keluar        ║")
        print("╚══════════════════╝")
        
        pilih = input("\nPilih (1-3): ")
        
        if pilih == '1':
            clear_vscode_terminal()
            print("Game dimulai!")
            print("Selamat bermain...")
            input("\nTekan Enter kembali ke menu")
            
        elif pilih == '2':
            clear_vscode_terminal()
            print("=== SETTINGS ===")
            print("1. Difficulty: Normal")
            print("2. Sound: On")
            input("\nTekan Enter kembali")
            
        elif pilih == '3':
            clear_vscode_terminal()
            print("Bye bye!")
            break

# Jalankan
game_loop()