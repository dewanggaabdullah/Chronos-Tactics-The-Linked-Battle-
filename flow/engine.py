from flow import units as un
from flow import char_choice as cc
from flow import utils as ut
from flow import story as st


def inisialisasi_karakter():
    global tim_pemain, monster

    daftar_karakter = cc.validasi_karakter()

    if daftar_karakter == False:
        return
    else:
        tim_pemain = cc.pemilihan_karakter(*daftar_karakter)
        monster = un.Monster('ORC GURUN', 250, 40)

    def jalankan_game(tim_pemain, monster):
        ut.bersihkan_terminal()
        print(f"=== PERTARUNGAN DIMULAI ===")
        print(f'sebuah {monster.nama} muncul di perjalanan...!')

        while monster.hp > 0:
            # cek anggota hidup
            if not any(tim_bertahan.hp > 0 for tim_bertahan in tim_pemain.values()):
                print()
                print('=' *30)
                print('GAME OVER.. tidak ada lagi anggota dalam tim yang sanggup melanjutkan pertarungan')
                print('CRONOS SPARKLE DIAKTIFKAN... KEMBALI KE MASA LALU!!!')
                print('=' *30)
                break
        
            # siapkan baris status buat anggota tim
            status_anggota = []
            for i, k in enumerate(tim_pemain.values(), 1):
                hp_display = f'{k.hp} HP' if k.hp > 0 else '-'
                # ljust(left justify) membuat nama karakter bila kurang dari 51 karakter,
                # maka python akan membuat spasi buat mengisi kekosongan sampai cukup
                baris = f'║ {i}. {k.nama.upper()}: {hp_display}'.ljust(51) + '║'
                status_anggota.append(baris)

            # Cetak Tabel (Hanya Satu Kali per ronde)
            print("\n╔══════════════════════════════════════════════════╗")
            print("║                   STATUS UNIT                    ║")
            print("╠══════════════════════════════════════════════════╣")
            print("║ TIM:                                             ║")
            
            for baris in status_anggota:
                print(baris)
                
            print("║                                                  ║")
            print("╠══════════════════════════════════════════════════╣")
            print("║ MUSUH:                                           ║")
            
            # Status Monster
            status_monster = f"║ 1. {monster.nama.upper()}: {monster.hp} HP".ljust(51) + "║"
            print(status_monster)
            
            print("╚══════════════════════════════════════════════════╝")

            # pilihan aksi yang dapat dipilih pemain
            aksi = input('\n[i] Pilih nama karakter untuk menyerang/menggunakan skill, atau ketik "kabur" buat melarikan diri\n>>>  ').lower().strip()

            if aksi == 'kabur':
                print('[lol] kalian melarikan diri...!, monster itu terlalu kuat dan kalian ternyata hanya seekor anak ayam di mata seorang monster perkasa...(wkwk)\n<<< GAME OVER >>>')
                ut.bersihkan_terminal()
                break

            # kalau pemain menyerang monster
            if aksi in tim_pemain:
                penyerang = tim_pemain[aksi]

                if penyerang.hp < 0:
                    print(f'\n~ [!] {penyerang.nama} sudah tidak berdaya, pilih teman yang lain!')
                    continue

                penyerang.ambil_tindakan(monster)

                if monster.hp <= 0:
                    print(f'[!] berhasil...!!!, {monster.nama} telah dikalahkan...')
                    break

                # monster otomatis membalas menyerang    
                balasan_monster = monster.menyerang(penyerang)
                print(f"\n[x] {monster.nama} murka dan menyerang {penyerang.nama}, memberikan damage sebesar {monster.atk}")

            # kalau tim pemain ada yang hpnya setara/di bawah 0
                if penyerang.hp <= 0:
                    print()
                    print(f'[!] {penyerang.nama} tidak sanggup melanjutkan pertempuran... terus berjuang..!!!')
                else:
                    print()
                    print(f'[-] {penyerang.nama} bertahan! Hp tersisa: {penyerang.hp}')
            else:
                ut.bersihkan_terminal()
                print('\nnama tersebut tidak ada di dalam tim atau salah ketik')

# [i] = input pemain dari terminal
# [!] = momen penting
# [X] = info pertarungan(serangan)
# [-] = info pertarungan(menerima serangan)
# [lol] = tolol(tertawa terbahak-bahak)

    jalankan_game(tim_pemain, monster)
    


