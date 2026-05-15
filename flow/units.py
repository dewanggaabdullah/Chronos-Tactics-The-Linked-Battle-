import traceback
from flow import utils as ut
from flow import story as st

#karakter
class Dasar_Karakter:
    def __init__(self, nama, hp, atk):
        self.nama = nama
        self.hp = hp
        self.atk = atk
        self.max_hp = hp
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

            print(f"✨ {self.nama} memberikan pemulihan pasif ke tim!")

    """
    nah, kalau char jenis ini saat dipilih user, maka game akan masuk ke menu pemilihan
    apakah user mau basic attack, atau mau pakai skill aktifnya
    """

class Bruno(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.menangkis = False # status awal

    def gunakan_skill(self, **kwargs):
        # bruno dalam mode fokus bertahan, jadi dia gak nyerang
        print(f'{self.nama} mengunakan barbelnya, fokus menangkis serangan!')
        self.menangkis = True
        return True

    def menerima_serangan(self, damage):
        if  self.menangkis:
            print(f'{self.nama} memakai barbelnya...! menghalau serangan monster dengan barbel yang kelihatannya berat itu')
            damage = 0 # buat damage jadi nol, agar tidak ngurangin hp bruno
            self.menangkis = False

        # pas udah di manipulasi damagenya, baru serangan masuk
        return super().menerima_serangan(damage)

class Dewa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.waktu_tunggu = 3
        self.damage_dasar = atk # simpan nilai asli agar serangan bisa direset
        self.damage_critical = 40
        self.skill_pasif = True

    def gunakan_skill_pasif(self, **kwargs):
        musuh = kwargs.get('target')

        if self.waktu_tunggu == 0:
            self.atk = self.damage_critical # damage critical yang dikasih dewa

            ut.bersihkan_terminal()
            print(f"!!! {self.nama} MENGELUARKAN SERANGAN CRITICAL... damage sebesar {self.atk} diberikan...!!!")
            
            # Kita tidak perlu memanggil self.menyerang(musuh) di sini
            # karena Class Dasar akan memanggilnya setelah fungsi ini selesai.
            # Cukup biarkan self.atk dalam kondisi tinggi saat fungsi ini berakhir.
            
            self.waktu_tunggu = 3
            return True
        else:
            # jika belum seharusnya critical, atk harus kembali ke normal
            self.atk = self.damage_dasar
            self.kurangi_cooldown()
            return False

    def kurangi_cooldown(self):
        if self.waktu_tunggu > 0:
            self.waktu_tunggu -= 1 







































class Joy(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.suntik_daya_tahan = 20
        self.waktu_tunggu = 0

    def gunakan_skill(self, **kwargs):
        # joy mengambil paket dari yang kita bikin
        # di parameter ambil_tindakan pakai **kwargs
        tim = kwargs.get('tim_pemain')

        # kasih cooldown biar skill nya seimbang
        # sekalian sama logika skill nya disini
        if self.waktu_tunggu == 0:
            if tim:
                for anggota in tim.values():
                    # joy gak pakai batas max_hp, biar joy op
                    anggota.hp += self.suntik_daya_tahan

            self.waktu_tunggu = 3  

            ut.bersihkan_terminal()
            print(f"{self.nama} memberikan suntikan! {self.suntik_daya_tahan} HP ditambahkan ke semua rekan.")
            return True
        else:
            print(f"Skill sedang cooldown! tunggu {self.waktu_tunggu} babak lagi")
            return False

    def kurangi_cooldown(self):
        if self.waktu_tunggu > 0:
            self.waktu_tunggu -= 1

class Mikasa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super(). __init__(nama, hp, atk)
        self.bonus_serangan = 10
        
        # dekralasi awal buat nanti diubah jadi True
        # kalau dewa sama mikasa, dan hp dewa rendah 
        self.mode_ngamuk = False
        self.skill_pasif = True

    def gunakan_skill(self, **kwargs):
        # siapin variabel dewa buat loop, kalau dewa gak jumpa
        # dewa tetap none(gak ada), ambil data dari kwargs buat liat isi tim_pemain
        daftar_tim = kwargs.get('tim_pemain, []')
        dewa = None

        for char in daftar_tim:
            if char.nama == 'Dewa' and char.hp > 0:
                dewa = char # karna dewa jumpa, dan masih hidup, jadi keynya di aktifkan
                break

        if dewa:
            # kalau dewa ada, mikasa dapat bonus serangan
            if not hasattr(self, 'bersama_dewa'): # cek pakai string attr mikasanya
                self.atk += self.bonus_serangan
                self.bersama_dewa = True # attr di buat dadakan dan langsung dipakai

            if dewa.hp < 30 and not self.mode_ngamuk:
                self.atk *= 2 # meningkat 100 persen
                self.mode_ngamuk = True
                print(f"!!! MIKASA MENGAMUK !!! HP {dewa.nama} kritis!")

            if dewa.hp > 30 and self.mode_ngamuk:
                self.atk /= 2 # kembali ke normal, cuman bonus bersama dewa yang masih valid 
                self.mode_ngamuk = False

        # kalau dewa mati, semua attribute mikasa hilang dan mengalami debuff parah
        # agar game jadi lebih taktis(juga dewa gak ditumbalin sampe mati)  ;)
        else:
            # cek mikasa sebelumnya jika punya bonus dari dewa
            if hasattr(self, 'bersama_dewa'):
                print(f"!!! {self.nama.upper()} DEPRESI !!! {self.nama} kehilangan semangat bertarung...")

                # reset bonus pertambahan basic attack bersama dewa
                self.atk -= self.bonus_serangan

                # buff mikasa hilang karna dewa udah mati
                if self.mode_ngamuk:
                    self.mode_ngamuk = False
                    self.atk /= 2

                # hapus attribute agar mikasa gak dibagi 2 terus damagenya tiap ronde
                delattr(self, 'bersama_dewa')

                # kasih debuff gak ngotak buat mikasa
                self.atk /= 2

        #Karena ini pasif, kita return True 
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
bruno = Bruno('Bruno', 150, 15)
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