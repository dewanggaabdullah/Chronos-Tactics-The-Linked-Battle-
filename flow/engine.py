from flow import units as un
from flow import char_choice as cc
from flow import utils as ut
from flow import story as st
from history import node as no
from history import rewind as re
   
def inisialisasi_karakter():
    global tim_pemain, monster

    daftar_karakter = cc.validasi_karakter()

    if daftar_karakter == False:
        return
    else:
        tim_pemain = cc.pemilihan_karakter(*daftar_karakter)
        # aku pakai * agar dapat jumblah karakter dinamis
        # dan gak perlu nulis variabelnya satu satu pakai cara manual

        monster = un.Monster('ORC GURUN', 250)

    def jalankan_game(tim_pemain, monster):
        history = no.TurnHistory()
        nomor_turn = 1

        # =========================================================================
        # FASE 1: AWAL TURN (Pasif jalan di sini, CUMA SEKALI PER ROUND)
        # =========================================================================

        # --- DI LUAR CLASS, SEBELUM LOOP PERTARUNGAN ---
        for karakter in tim_pemain.values():
            # Variabel 'karakter' di bawah ini adalah pancingan objek aslinya
            karakter.setup_statistik_awal()
            
        # -----------------------------------------------
        # Baru setelah ini masuk ke loop pertarungan utama...

        ut.bersihkan_terminal()
        print(f"=== PERTARUNGAN DIMULAI ===")
        print(st.kedatangan_monster.format(monster = monster.nama))

        while monster.hp > 0:
            # [PENTING] 1. Catat state awal turn tepat di sini sebelum ada aksi/perubahan status
            history.catat_turn(nomor_turn, tim_pemain, monster)

            # jalankan semua efek pasif heal/buffer di awal turn, seperti elsa
            for char in tim_pemain.values():
                # setiap char yang punya skill pasif positif, jalanin duluan
                if char.hp > 0 and hasattr(char, 'aktifkan_pasif'):
                    char.aktifkan_pasif(tim_pemain)

            # cek anggota hidup
            if not any(tim_bertahan.hp > 0 for tim_bertahan in tim_pemain.values()):
                print()
                print('=' *30)
                print(game_kalah)
                print('=' *30)
                break
        
            # pasif char jalan
            target = monster

            for char in tim_pemain.values():
                # kita jalanin pasif universal, kaya dewa dan mikasa
                if char.hp > 0:
                    char.jalankan_pasif(target = target,tim_pemain = tim_pemain)
                else:
                    # kalau mati, lewati aja
                    pass
            else:
                pass

            # =========================================================================
            # FASE 2: INPUT PLAYER (Loop ini mengunci player sampai inputnya benar)
            # =========================================================================

            while True:
                # siapkan baris status buat anggota tim
                status_anggota = []
                for i, k in enumerate(tim_pemain.values(), 1):
                    hp_display = f'{k.hp} HP' if k.hp > 0 else '-'

                    # buat baris demi baris secara manual
                    teks_mentah = f'║ {i}. {k.nama.upper()}: {hp_display}'

                    # kita bikin text char hijau waktu skill bisa di gunain...!!
                    if hasattr(k,'cooldown') and k.cooldown == 0 and k.hp > 0:
                        nama_display = f'{ut.hijau}{i}. {k.nama.upper()}: {hp_display}{ut.RESET}'
                    else:
                        nama_display = f'{i}. {k.nama.upper()}: {hp_display}'

                    # hitung dulu sisa spasi pembatas kanan secara manual
                    lebar_tabel = 25
                    sisa_spasi = lebar_tabel - len(teks_mentah) - 1

                    # baru gabungkan teks berwarna dengan sisa spasi manual dan tutup dengan ║
                    baris = f'║ {nama_display}' + (' ' * sisa_spasi) + "║"
                    status_anggota.append(baris)


                # Cetak Tabel (Hanya Satu Kali per ronde)
                print(f'putaran - ( {nomor_turn} )') # Menggunakan variabel nomor_turn lokal
                print("\n╔═══════════════════════╗")
                print("║      STATUS UNIT      ║")
                print("╠═══════════════════════╣")
                print("║ TIM:                  ║")
                
                for baris in status_anggota:
                    print(baris)
                    
                print("║                       ║")
                print("╠═══════════════════════╣")
                print("║ MUSUH:                ║")
                
                # Status Monster
                status_monster = f"║ 1. {monster.nama.upper()}: {monster.hp} HP".ljust(24) + "║"
                print(status_monster)
                
                print("╚═══════════════════════╝")

                # pilihan aksi yang dapat dipilih pemain (Ditambahkan opsi "rewind")
                aksi = input('\n[i] Ketik nama karakter untuk menyerang/skill, "rewind" untuk putar waktu, atau "kabur"\n>>>  ').lower().strip()

                if aksi == 'kabur':
                    ut.bersihkan_terminal()
                    print(st.kabur)
                    print()
                    return

                # [PENTING] Proses pemanggilan menu rewind interaktif pynput
                if aksi == 'rewind':
                    import copy
                    turn_terpilih = re.menu_interaktif(history, ut)
                    
                    if turn_terpilih:
                        # Kembalikan seluruh state game ke turn terpilih
                        tim_pemain = copy.deepcopy(turn_terpilih.data_tim)
                        monster = copy.deepcopy(turn_terpilih.data_monster)
                        nomor_turn = turn_terpilih.nomor_turn
                        
                        ut.bersihkan_terminal()
                        print(f"\n[!] Waktu berhasil diputar kembali ke Turn {nomor_turn}!")
                        input("Tekan Enter untuk melanjutkan turn...")
                        
                        # Keluar dari while True input, langsung loncat ke awal while monster.hp
                        break 
                    else:
                        ut.bersihkan_terminal()
                        print("\n[!] Rewind dibatalkan.")
                        continue

                # kalau pemain menyerang monster
                if aksi in tim_pemain:
                    karakter = tim_pemain[aksi]

                    if karakter.hp <= 0:
                        print(st.pilihan_char_kalah.format(nama = karakter.nama))
                        continue

                    break
                else:
                    ut.bersihkan_terminal()
                    print(st.nama_char_tidak_ada) 
                    continue

            # Jika user memilih rewind, kita skip eksekusi aksi di bawah dan langsung mengulang loop utama
            if aksi == 'rewind' and turn_terpilih:
                continue

            # =========================================================================
            # FASE 3: EKSEKUSI AKSI & BALASAN MONSTER
            # =========================================================================

            # char pasif langsung menyerang
            if karakter.skill_pasif:
                print(karakter.menyerang(monster))
            else:
                # Char aktif memilih basic attack atau pakai skill (seperti Bruno)
                karakter.skill_aktif(monster=monster, tim_pemain=tim_pemain)

            if monster.hp <= 0:
                print(st.monster_kalah.format(monster = monster.nama))
            else:
                # monster otomatis membalas menyerang
                balasan_monster = monster.menyerang(karakter)

                if karakter.hp <= 0:
                    print()
                    print(st.karakter_kalah.format(nama = karakter.nama))
                else:
                    print()
                    print(st.karakter_diserang.format(nama = karakter.nama, hp = karakter.hp))

            # =========================================================================
            # FASE AKHIR: AKHIR BABAK/ SEBELUM RONDE BERIKUTNYA
            # =========================================================================

            for char in tim_pemain.values(): # Memperbaiki typo tim_pemain_values() -> tim_pemain.values()
                # cek char masih hidup dan punya skill aktif/pasif yang cooldown 
                if hasattr(char, 'cooldown') and char.hp > 0:
                    char.kurangi_cooldown()
                    
            # [PENTING] Tambah hitungan nomor turn untuk babak berikutnya
            nomor_turn += 1

    jalankan_game(tim_pemain, monster)