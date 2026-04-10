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
        return f"\n[x] {penyerang.nama} menyerang! memberikan damage sebesar {penyerang.atk}."

    def menerima_serangan(self, damage):
        self.hp -= damage
        pesan = f'{self.nama} terkena damage, hp berkurang sebanyak {damage} \ndarah {self.nama} tersisa: {self.hp}'

        if self.hp <= 0:
            kalah = f'{self.nama} menyerah, pertarungan berakhir'
            return kalah, False

        return pesan, True

    def ambil_tindakan():
        aksi = getattr(attribute_karakter, 'gunakan_skill', None)
        if aksi and callable(aksi):
            print('skill aktif')
        else:
            print('skill pasif')


class Elsa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__ (nama, hp, atk)
        self.healing = 7

    # skil pasif
    def skill_pasif():
        for anggota in daftar_tim.values():
            if anggota.hp > 0:
                anggota.hp += self.healing
                if anggota.hp > anggota.maks_hp:
                    anggota.hp = anggota.maks_hp
        print(f'{self.nama} mengobati hp tim sebanyak {self.healing} \nhp setiap tim menjadi {daftar_tim.max(100)}')

class Bruno(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.tangkis = False

    # skill aktif(liat huruf)
    def gunakan_skill(self, damage):
        if self.tangkis:
            self.tangkis = False
            pesan = f"{self.nama} menggunakan barbel super nya..!!! Tidak ada serangan monster yang terasa."
            return pesan, True

        super().menerima_serangan(damage)

class Dewa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)

class Joy(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.suntik_daya_tahan = 20
        self.waktu_tunggu = 0

    def gunakan_skill(self):
        if self.waktu_tunggu == 0:
            self.waktu_tunggu = 3

            for anggota in daftar_tim.values():
                anggota.hp += self.suntik_daya_tahan

            pesan = f"{self.nama} memberikan suntikan! {self.heal_power} HP ditambahkan ke semua rekan."
            return pesan, True

    def kurangi_cooldown(self):
        if self.cooldown > 0:
            self.cooldown -= 1

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
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.daftar_atk = [40,15,17,13]
        self.index_serangan = 0 # pengarah berasan damage yang diberikan monster
       
    def serang(self, target):
        if self.hp > 0:
            # serangan yang mau di kasih monster di arahin pakai index_serangan
            serangan_sekarang = self.daftar_atk[self.index_serangan]

            target.hp -= serangan_sekarang
            print(f'sekarang {self.nama} balas menyerang...!, kali ini serangannya menghasilkan kerusakan setara {serangan_sekarang} untuk [kurung kurawal penyerang.hp]')        

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