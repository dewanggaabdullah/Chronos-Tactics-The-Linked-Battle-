import traceback
from flow import utils as ut
from flow import story as st

#karakter
class Dasar_Karakter:
    def __init__(self, nama, hp, atk):
        self.nama = nama
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.atk_dasar = atk
        self.skill_pasif = False # buat default nya char gak punya pasif


    def menyerang(self, target):
        """basic attack mengurangi hp target"""
        damage = self.atk
        target.menerima_serangan(damage)
        return st.tim_menyerang.format(
            nama = self.nama,
            damage = self.atk,
        )

    def menerima_serangan(self, damage):
        self.hp -= damage

        if self.hp <= 0:
            self.hp = 0
            return st.karakter_kalah.format(nama = self.nama), False

        return st.karakter_diserang.format(nama = self.nama, hp = self.hp), True

    def jalankan_pasif(self, **kwargs):
        """
        kwargs akan menampung apapun yang dikasih,target, tim pemain, musuh, dll
        """
        if self.skill_pasif:
            # teruskan **kwargs ke fungsi logika
            self.gunakan_skill_pasif(**kwargs)

    def skill_pasif(self, **kwargs):
        """fungsi ini nanti akan diisi oleh char pasif"""
        pass

    def skill_aktif(self, **kwargs):
        """
        menu opsi pilihan char waktu karakter aktif dipanggil
        """
        # bongkar kwargs
        target = kwargs.get('monster')
        tim_pemain = kwargs.get('tim_pemain')

        # nge check apakah ada fungsi "gunakan_skill_aktif" (kaya bruno)
        fungsi_skill = getattr(self, 'gunakan_skill', None)

        if self.gunakan_skill and callable(fungsi_skill):
            while True:
                print(f'\n--- putaran {self.nama} ---')
                print('1. menyerang')
                print('2. gunakan skill')

                pilih = input('pilih opsi berdasarkan nomor, ambil keputusanmu!...\n>>> ')
                
                if pilih == '1':
                    print(self.menyerang(target))
                    return False # giliran selesai

                # pakai variabel yang udah didefinisikan dari kwargs
                elif pilih == '2':
                    status = fungsi_skill(target = target, tim_pemain = tim_pemain)

                    if status: 
                        return True # skill berhasil dijalankan
                    
                    else: 
                        print(f"{self.nama} tidak punya skill aktif, otomatis menyerang!")
                        print("Skill gagal/cooldown! Pilih lagi.")
                        continue # skill cooldown atau gagal, ulangi menu
        else:
            # kalau char gak punya skill aktif, suruh pukul aja
            print(self.menyerang(target))
            return False

    def kurangi_cooldown(self):
        """
        fungsi universal, buat dipakein super(). di char yang butuh
        """
        if self.cooldown > 0:
            self.cooldown -= 1

    def setup_statistik_awal(self):
        """
        Standar permainan: Mengembalikan semua buff/debuff 
        dan modifikasi stat ke angka dasar asli mereka.
        """
        self.atk = self.atk_dasar
        self.hp = self.max_hp
        # Jika nanti ada stat lain seperti defense atau speed, reset juga di sini
        # self.defense = self.defense_dasar

    """
    elsa punya pasif menyembuhkan, tapi tetap bisa mukul, jadi karna char jenis ini skill nya
    gak perlu dipanggil, maka dia gak masuk menu kaya karakter aktif
    """

class Elsa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        # aku pakai super() biar ngambil apa yang dasar karakter isi di __init__nya
        super().__init__ (nama, hp, atk) 
        self.healing = 7
        self.skill_pasif = True

    def gunakan_skill_pasif(self, **kwargs):
        # elsa mengambil paket dari yang kita bikin
        # di parameter ambil_tindakan pakai **kwargs
        tim = kwargs.get('tim_pemain')

        if tim:
            for anggota in tim.values():
                # pasif jalan kalau hp tim dibawah hp awalnya
                if 0 < anggota.hp < anggota.max_hp:
                    anggota.hp = min(anggota.hp + self.healing, anggota.max_hp)

            print(f"\n[*] {self.nama} memberikan pemulihan pasif ke tim!")

    """
    nah, kalau char jenis ini saat dipilih user, maka game akan masuk ke menu pemilihan
    apakah user mau basic attack, atau mau pakai skill aktifnya
    """

class Bruno(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.cooldown = 0
        self.menangkis = False # status awal

    def gunakan_skill(self, **kwargs):
        if self.cooldown == 0:
            # bruno dalam mode fokus bertahan, jadi dia gak nyerang
            self.menangkis = True
            return True
        else:
            print(st.skill_cooldown.format(nama = self.nama, cooldown = self.cooldown))
            return False

    def menerima_serangan(self, damage):
        if  self.menangkis:
            print(f'\n[*] {self.nama} memakai barbelnya...! menghalau serangan monster dengan barbel yang kelihatannya berat itu')
            damage = 0 # buat damage jadi nol, agar tidak ngurangin hp bruno
            self.menangkis = False

            # balikin cooldownnya
            self.cooldown = 3

        # pas udah di manipulasi damagenya, baru serangan masuk
        return super().menerima_serangan(damage)

    def setup_statistik_awal(self):
        # kita jalanin reset dari dasar_karakter, baru yang lokal
        super().setup_statistik_awal()

        # atur kondisi char biar tiga dan berkurang saat ronde berjalan
        self.cooldown = 0

    def kurangi_cooldown(self):
        super().kurangi_cooldown()

class Dewa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.cooldown = 3
        self.damage_dasar = atk # simpan nilai asli agar serangan bisa direset
        self.damage_critical = 40
        self.skill_pasif = True

    def gunakan_skill_pasif(self, **kwargs):
        musuh = kwargs.get('target')

        if self.cooldown == 0:
            self.atk = self.damage_critical # damage critical yang dikasih dewa

            print(f"\n[*] !!! {self.nama} MENGELUARKAN SERANGAN CRITICAL... damage sebesar {self.atk} diberikan...!!!")
            
            # Kita tidak perlu memanggil self.menyerang(musuh) di sini
            # karena Class Dasar akan memanggilnya setelah fungsi ini selesai.
            # Cukup biarkan self.atk dalam kondisi tinggi saat fungsi ini berakhir.
            
            self.cooldown = 4
            return True
        else:
            # jika belum seharusnya critical, atk harus kembali ke normal
            self.atk = self.damage_dasar
            return False 

    def setup_statistik_awal(self):
        # kita jalanin reset dari dasar_karakter, baru yang lokal
        super().setup_statistik_awal()

        # atur kondisi char biar tiga dan berkurang saat ronde berjalan
        self.cooldown = 3

    def kurangi_cooldown(self):
        super().kurangi_cooldown()

# sistem cooldown joy beda sama punya dewa, kalau dewa charging, namun joy bisa
# dipakai langsung di awal pertarungan

class Joy(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.suntik_daya_tahan = 20
        self.cooldown = 0
        self.skill_pasif = False

    def gunakan_skill(self, **kwargs):
        # joy mengambil paket dari yang kita bikin
        # di parameter ambil_tindakan pakai **kwargs
        tim = kwargs.get('tim_pemain')

        # kasih cooldown biar skill nya seimbang
        # sekalian sama logika skill nya disini
        if self.cooldown == 0:
            if tim:
                for anggota in tim.values():
                    # kita sembuhin yang idup idup aja
                    if anggota.hp > 0:
                        # joy gak pakai batas max_hp, biar joy op
                        anggota.hp += self.suntik_daya_tahan

            self.cooldown = 4 

            ut.bersihkan_terminal()
            print(f"[*] {self.nama} memberikan suntikan! {self.suntik_daya_tahan} HP ditambahkan ke semua rekan.")
            return True
        else:
            print(st.skill_cooldown.format(nama = self.nama, cooldown = self.cooldown))
            return False

    def setup_statistik_awal(self):
        # kita jalanin reset dari dasar_karakter, baru yang lokal
        super().setup_statistik_awal()

        # atur kondisi char biar nol dan bisa langsung dipakai
        self.cooldown = 0

    def kurangi_cooldown(self):
        super().kurangi_cooldown()

class Mikasa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super(). __init__(nama, hp, atk)
        self.bonus_serangan = 10
        
        # dekralasi awal buat nanti diubah jadi True, kalau dewa sama mikasa, dan hp dewa rendah
        # kalau skill pasif harus true, karna skill mikasa pasif  
        self.mode_ngamuk = False
        self.skill_pasif = True
        self.sudah_defpresi = False

    def gunakan_skill_pasif(self, **kwargs):
        # siapin variabel dewa buat loop, kalau dewa gak jumpa
        # dewa tetap none(gak ada), ambil data dari kwargs buat liat isi tim_pemain
        tim = kwargs.get('tim_pemain, {}')
        daftar_tim = tim.values() if hasattr(tim, 'values') else tim # gini aja biar ringkas
        
        dewa = None
        for char in daftar_tim:
            # Pastikan char adalah objek dan memiliki atribut nama
            if hasattr(char, 'nama') and char.nama.lower() == 'dewa' and char.hp > 0:
                dewa = char # karna dewa jumpa, dan masih hidup, jadi key-nya di aktifkan
                break

        if dewa:
            if self.sudah_depresi:
                self.sudah_depresi = false # reset status nya kalau dewa hidup/pulih lagi hp nya

            # kondisi 1, mikasa dapat bonus atk karna ada dewa
            if not hasattr(self, 'bersama_dewa'):
                self.atk += self.bonus_serangan
                self.bersama_dewa = True

            # kondisi 2, dewa sekarat --> mikasa mengamuk, atk nya dikali 2 biar makin op
            if dewa.hp < 30 and not self.mode_ngamuk:
                self.atk *= 2
                self.mode_ngamuk = True
                print('\n [*] !!! MIKASA MENGAMUK !!! {dewa.nama} kritis! serangan mikasa meningkat tajam ')

            # kondisi 3, hp dewa balik ke atas 30 --> mikasa tenang, attribut ngamuknya hilang
            if dewa.hp >= 30 and self.mode_ngamuk:
                self.atk /= 2
                self.mode_ngamuk = False
                print(f'\n [*] ...mikasa tenang... mode ngamuk {self.nama} mereda seiring {dewa.nama} membaik')

            """
            kondisi 4
            kalau dewa mati, semua attribute mikasa hilang dan mengalami debuff parah
            agar game jadi lebih taktis(dan juga agar dewa gak ditumbalin sampe mati)  ;)
            """
        else:
            # jika dewa mati/tidak ada di tim
            if hasattr(self, 'bersama_dewa') or not self.sudah_depresi:
                print(f"[*] !!! {self.nama.upper()} DEPRESI !!! {self.nama} kehilangan semangat bertarung...")

                # kurangi bonus kalau tadi bertarung bersama dewa
                if hasattr(self, 'bersama_dewa'):
                    self.atk -= self.bonus_serangan
                    delattr(self, 'bersama_dewa')

                # matikan mode ngamuk jika sedang aktif
                if self.mode_ngamuk:
                    self.atk /= 2
                    self.mode_ngamuk = False

                # berikan debuff parah ke mikasa (hanya sekali)
                if not self.sudah_depresi:
                    self.atk /= 2
                    self.sudah_depresi = True # mengunci debuff biar gak infinite loop 

        # Karena ini pasif, kita return True 
        # supaya sistem tahu "skill pasif" sudah diproses
        return True

#monster

class Monster(Dasar_Karakter):
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp
        self.daftar_atk = [40,15,17,13]
        self.index_serangan = 0 # pengarah balasan damage yang diberikan monster
       
    def menyerang(self, target):
        if self.hp > 0:
            # serangan yang mau di kasih monster di arahin pakai index_serangan
            serangan_sekarang = self.daftar_atk[self.index_serangan]

            target.menerima_serangan(serangan_sekarang)

            print(st.monster_menyerang.format(
                monster = self.nama, 
                damage = serangan_sekarang,
                target = target.nama
            ))        

            # index di tambah buat nuntun monster lanjut ke serangan berikutnya
            self.index_serangan += 1

            if self.index_serangan >= len(self.daftar_atk):
                self.index_serangan = 0

        else:            
            print(f'{self.nama} sudah kalah dan tidak bisa menyerang.')

# setelah permainan berakhir, pakai fungsi ini buat riset
def reset_entitas():
    for hero in pilihan_karakter.values():
        hero.hp = hero.max_hp

    monster_obj.hp = monster_obj.max_hp

# menginisialisasi nama karakter
elsa = Elsa('Elsa', 75, 5)
bruno = Bruno('Bruno', 150, 9)
dewa = Dewa('Dewa', 85, 15)
joy = Joy('Joy', 90, 10)
mikasa = Mikasa('Mikasa', 90, 10)

attribute_karakter = {
    'elsa': elsa,
    'bruno': bruno,
    'dewa': dewa,
    'joy': joy,
    'mikasa': mikasa
}