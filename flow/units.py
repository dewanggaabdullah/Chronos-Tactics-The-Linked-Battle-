import traceback
import utils as ut

#karakter
class Dasar_Karakter:
    def __init__(self, nama, hp, atk):
        self.nama = nama
        self.hp = hp
        self.atk = atk
        self.max_hp = hp

    def menyerang(self, target):
        damage = self.atk
        target.menerima_serangan(damage)
        return f"\n[x] {self.nama} menyerang! memberikan damage sebesar {damage}."

    def menerima_serangan(self, damage):
        self.hp -= damage
        pesan = f'{self.nama} terkena damage, hp berkurang sebanyak {damage} \ndarah {self.nama} tersisa: {self.hp}'

        if self.hp <= 0:
            kalah = f'{self.nama} menyerah, pertarungan berakhir'
            return kalah, False

        return pesan, True

    def ambil_tindakan(self, target):
        # cek apakah karakter punya skill aktif atau tidak
        aksi = getattr(self, 'gunakan_skill', None)

        if aksi and callable(aksi):
            # disini kalau skill aktif cooldown, dan pemain masih panggil,
            # maka monster gak nyerang dulu dan loop disini 
            while True:
                print(f'\n--- giliran {self.nama} ---')
                print('1.menyerang')
                print('2.gunakan skill')

                try:
                    pilih = input('pilih nomor pada opsi,buat strategimu..!\n>>> ')

                    if pilih == '1':
                        # kalau serangannya pasif, langsung menyerang musuh
                        # langsung lolos fungsi...
                        return False

                    elif pilih == '2':
                        # disini kirim target buat karakter dan objek tim_pemain
                        # sekaligus sebagai paket agar lebih scalable buat banyak 
                        # karakteristik skill karakter
                        status_skill = aksi(target=target, tim_pemain=tim_pemain)

                        if status_skill True:
                            return True # kita tandai kalo skill udah aktif dan dipakai
                        else:
                            # skill lagi cooldown, jadi putaran gak valid dan ulang dari awal
                            # agar pemain gak rugi giliran
                            continue
                    else:
                        # buat tutup celah kalau user bertingkah
                        raise ValueError

            except ValueError:
                print('harap masukkan input berupa angka pada opsi pilihan yang ada')
            except Exception as e:
                print(f'ada kesalahan yang tak terduga... \npesan buat developer\n{e}')

        return False


class Elsa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__ (nama, hp, atk)
        self.heal_max = hp
        self.healing = 7

    # skil pasif
    def gunakan_skill(self, **kwargs):
        # elsa mengambil paket dari yang kita bikin
        # di parameter ambil_tindakan pakai **kwargs
        tim = kwargs.get('tim_pemain')

        if tim:
            berhasil_obati = False
            for anggota in tim.values():
                # pasif jalan kalau hp tim dibawah hp awalnya
                if 0 < anggota.hp < anggota.heal_max:
                    anggota.hp += self.healing
                    berhasil_obati = True 
        
        if berhasil_obati:     
            print(f'{self.nama} mengobati hp tim sebanyak {self.healing} \nhp setiap tim menjadi {tim.max(100)}')

        return False # Agar Elsa tetap bisa menyerang biasa setelah nge-heal

class Bruno(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.menangkis = False # status awal
        self.waktu_tunggu = 0

    def gunakan_skill(self, **kwargs):
        # bruno dalam mode fokus bertahan, jadi dia gak nyerang
        self.menangkis = True
        return True

    def menangkis_serangan(self, damage):
        if  self.menangkis:
            print(f'{self.nama} memakai barbelnya...! menghalau serangan monster dengan barbel yang kelihatannya berat itu')
            self.menangkis = False
            damage = 0 # buat damage jadi nol, agar tidak ngurangin hp bruno

        # pas udah di manipulasi damagenya, baru serangan masuk
        super().menerima_serangan(damage)

class Dewa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)

    def gunakan_skill(self, **kwargs):
        musuh = kwargs.get('target')



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
        self.mode_ngamuk = False

    def skill_pasif(self, daftar_tim):
        # siapin variabel dewa buat loop, kalau dewa gak jumpa
        # dewa tetap none(gak ada)
        dewa = None

        for char in daftar_tim:
            if char.nama == 'Dewa':
                dewa = char # karna dewa jumpa, jadi diganti
                break

        if dewa:
            # kalau dewa ada, mikasa dapat bonus serangan
            if not hasattr(self, self.mode_ngamuk):
                self.atk += self.bonus_serangan
                self.bonus_dewa = True

            if dewa.hp < 30 and not self.mode_ngamuk:
                self.atk *= 2 # meningkat 100 persen
                self.mode_ngamuk = True
                print(f"!!! MIKASA MENGAMUK !!! HP {dewa.nama} kritis!")

            if dewa.hp > 30 and self.mode_ngamuk:
                self.atk /= 2 # kembali ke normal, cuman bonus bersama dewa yang masih valid 
                self.mode_ngamuk = False


#monster

class Monster(Dasar_Karakter):
    def __init__(self, nama, hp):
        self.nama = nama
        self.hp = hp
        self.daftar_atk = [40,15,17,13]
        self.index_serangan = 0 # pengarah berasan damage yang diberikan monster
       
    def menyerang(self, target):
        if self.hp > 0:
            # serangan yang mau di kasih monster di arahin pakai index_serangan
            serangan_sekarang = self.daftar_atk[self.index_serangan]

            target.hp -= serangan_sekarang
            print(f'sekarang {self.nama} menyerang...!, kali ini serangannya menghasilkan kerusakan setara {serangan_sekarang} untuk [kurung kurawal penyerang.hp]')        

            # index di tambah buat nuntun monster lanjut ke serangan berikutnya
            self.index_serangan += 1

            if self.index_serangan >= len(daftar_atk):
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