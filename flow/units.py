#karakter

class Dasar_Karakter:
    def __init__(self, nama, hp, atk):
        self.nama = nama
        self.hp = hp
        self.atk = atk
        self.max_hp = hp

    def menyerang(self, target):
        damage = self.atk
        return target.menerima_serangan(damage)

    def menerima_serangan(self, damage):
        self.hp -= damage
        pesan = f'{self.nama} terkena damage, hp berkurang sebanyak {damage} \ndarah {self.nama} tersisa: {self.hp}'

        if self.hp <= 0:
            kalah = f'{self.nama} menyerah, pertarungan berakhir'
            return kalah, False

        return pesan, True
        

class Elsa(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__ (nama, hp, atk)
        self.healing = 7

    def pasif_healer(self, daftar_tim):
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

    def menangkis_serangan(self, damage):
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

    def tambah_darah(self):
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

    def bersama_dewa(self, dewa):
        damage_total = self.atk + self.bonus_serangan

        if dewa.hp < 30:
            damage_total = damage_total * 2
            print(f'MIKASA MENGAMUK...! HP {dewa.nama} kritis, damage {self.nama} meningkat pesat')

        return damage_total

#monster

class Monster(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(hp, nama, atk)
        self.daftar_atk = [40,15,17,13]
       
    def serang(self, target):
        if self.hp > 0:
            serangan_sekarang = self.daftar_atk
            target.hp -= serangan_sekarang
            print(f'sekarang {self.nama} mulai menyerang...!, kali ini serangannya menghasilkan kerusakan setara {serangan_sekarang} untuk target')
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

pilihan_karakter = {
    'elsa': elsa,
    'bruno': bruno,
    'dewa': dewa,
    'joy': joy,
    'mikasa': mikasa
}
