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
        monster = un.Monster('ORC GURUN', 250)

    def jalankan_game(tim_pemain, monster):
        ut.bersihkan_terminal()
        print(f"=== PERTARUNGAN DIMULAI ===")
        print(st.kedatangan_monster.format(monster = monster.nama))

        while monster.hp > 0:
            # cek anggota hidup
            if not any(tim_bertahan.hp > 0 for tim_bertahan in tim_pemain.values()):
                print()
                print('=' *30)
                print(game_kalah)
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
                print(kabur)
                ut.bersihkan_terminal()
                break

            # kalau pemain menyerang monster
            if aksi in tim_pemain:
                karakter = tim_pemain[aksi]

                if karakter.hp <= 0:
                    print(st.karakter_kalah.format(nama = karakter.nama))
                    continue

                karakter.ambil_tindakan(monster, tim_pemain)

                if monster.hp <= 0:
                    print(st.monster_kalah.format(monster = monster.nama))
                    break

                # monster otomatis membalas menyerang    
                balasan_monster = monster.menyerang(karakter)

            # kalau tim pemain ada yang hpnya setara/di bawah 0
                if karakter.hp <= 0:
                    print()
                    print(st.karakter_kalah.format(nama = karakter.nama))
                else:
                    print()
                    print(st.karakter_diserang.format(nama = karakter.nama, hp = karakter.hp))
            else:
                ut.bersihkan_terminal()
                print(st.nama_char_tidak_ada) 
                # disini gak pakai format karna gak perlu
                #(gak ada kata khusus yang dinamis dan pakai {})


# [i] = input pemain dari terminal
# [!] = momen penting
# [X] = info pertarungan(serangan)
# [-] = info pertarungan(menerima serangan)
# [lol] = tolol(tertawa terbahak-bahak)

    jalankan_game(tim_pemain, monster)
    


