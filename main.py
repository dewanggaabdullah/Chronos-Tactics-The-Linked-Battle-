# modul error handling
import traceback
        
from flow import engine as en
from flow import utils as ut
from flow import story as st
from flow import char_choice as cc

def main_menu():
    ut.bersihkan_terminal()
    while True:
        print('==={ CRONOS TACTICS: The Linked Battle }===')
        print()
        print("           ╔══════════════════╗")
        print("           ║   GAME MENU      ║")
        print("           ╠══════════════════╣")
        print("           ║ 1. Mulai         ║")
        print("           ║ 2. Settings      ║")
        print("           ║ 3. Keluar        ║")
        print("           ╚══════════════════╝")

        print('\npilih angka pada nomor diatas sebagai input...')

        def game_dimulai():
            st.prolog()
            en.inisialisasi_karakter()

        def settings():
        #ini sekarang gak ada gunanya,hanya formalitas,mungkin nanti dikembangkan
            ut.bersihkan_terminal()
            print("=== SETTINGS ===")
            print("1. Difficulty: indonesia")
            print("2. Sound: Off")

        try:
            pilih = input("Pilih (1-3): ")

            pilihan_user = {
                '1': game_dimulai,
                '2': settings
            }
        
            if pilih in pilihan_user:
                eksekusi = pilihan_user[pilih]  # Ambil 'alamat' fungsi
                eksekusi()                      # DI SINI KASIH PARAMETER/KURUNG.lower()
            elif pilih == '3':
                ut.bersihkan_terminal()
                print("Bye bye!\n")
                break
            else:
                raise ValueError

        except NameError:
            traceback.print_exc()
        except ValueError:
            print('harap masukkan nomor menu yang benar...')   
        except Exception as e:
            print(f'ada kesalahan yang tak terduga... \npesan buat developer\n')
            traceback.print_exc() # ini bakal nampilin tulisan error traceback buat mempermudah debug

        try:
            input("\n<< Tekan Enter saja buat kembali ke menu >> ")
        except EOFError:
            print('output habis')

ut.bersihkan_terminal()
main_menu()



