from flow import units as un
from flow import char_choice as cc
from flow import utils as ut
from flow import story as st


def inisialisasi_karakter():
    global tim_pemain, monster

    st.cerita_karakter()
    daftar_karakter = cc.validasi_karakter()

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
        
            # status semua entitas
            print('\n' + '_' *10 + 'STATUS_UNIT' + '_' *10)
            for p in tim_pemain.values():
                # kasih tau kalau ada karakter mati nanti ada "-" di hp nya
                status = f'{p.hp} HP' if p.hp > 0 else '-'
                print()
                print(      f'{p.nama.upper()}: {status}')
                print(      f'{monster.nama.upper()}: {monster.hp} HP')
                print()
                print('_' *40)

            # pilihan aksi yang dapat dipilih pemain
            aksi = input('\n[i] Pilih nama karakter untuk menyerang atau ketik "kabur" buat melarikan diri\n>>>  ').lower().strip()

            if aksi == 'kabur':
                print('[lol] kalian melarikan diri...!, monster itu terlalu kuat dan kalian ternyata hanya seekor anak ayam di mata seorang monster perkasa...(wkwk)\n<<< GAME OVER >>>')
                break

            if aksi in tim_pemain:
                ut.bersihkan_terminal()
                penyerang = tim_pemain[aksi]

                if penyerang.hp < 0:
                    print(f'\n~ [!] {penyerang.nama} sudah tidak berdaya, pilih teman yang lain!')
                    continue

                penyerang.menyerang(monster)
                print(f"\n[x] {penyerang.nama} menyerang! memberikan damage sebesar {penyerang.atk}.")

                if monster.hp <= 0:
                    print(f'[!] berhasil...!!!, {monster.nama} telah dikalahkan...')
                    break

                balasan_monster = monster.menyerang(penyerang)
                print(f"\n[x] {monster.nama} murka dan menyerang balik {penyerang.nama}, memberikan damage sebesar {monster.atk}")

                if penyerang.hp <= 0:
                    print()
                    print(f'[!] {penyerang.nama} tidak sanggup melanjutkan pertempuran... terus berjuang..!!!')
                else:
                    print()
                    print(f'[-] {penyerang.nama} bertahan! Hp tersisa: {penyerang.hp}')
            else:
                print('\nnama tersebut tidak ada di dalam tim atau salah ketik')

# [i] = input pemain dari terminal
# [!] = momen penting
# [X] = info pertarungan(serangan)
# [-] = info pertarungan(menerima serangan)
# [lol] = tolol(tertawa terbahak-bahak)

    jalankan_game(tim_pemain, monster)
    
def game_dimulai():
    ut.bersihkan_terminal()
    print('=== PEMILIHAN KARAKTER ===')
    print('silahkan pilih 3 dari teman kita untuk dibawa berpetualang...')
    print()
    inisialisasi_karakter()

