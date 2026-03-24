import random

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
        self.abillity = 7

    def pasif_healer(self, daftar_tim):
        for anggota in daftar_tim.values():
            if anggota.hp > 0:
                anggota.hp += self.abillity
                if anggota.hp > anggota.maks_hp:
                    anggota.hp = anggota.maks_hp
        print(f'{self.nama} mengobati hp tim sebanyak {self.abillity} \nhp setiap tim menjadi {daftar_tim.max(100)}')

class Bruno(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(nama, hp, atk)
        self.tangkis = False

    def menangkis_serangan(self, damage):
        if self.tangkis:
            self.tangkis = False
            pesan = f"{self.nama} menggunakan barbel super nya..!!! Tidak ada serangan monster yang terasa."
            return pesan, True

        return super().menerima_serangan(damage)

#monster

class Monster(Dasar_Karakter):
    def __init__(self, nama, hp, atk):
        super().__init__(hp, nama, atk)
        self.daftar_atk = [40,15,17,13]
       
    def serang(self, target):
        if self.hp > 0:
            serangan_sekarang = random.choice(self.daftar_atk)
            target.hp -= serangan_sekarang
            print(f'sekarang {self.nama} mulai menyerang...!, kali ini serangannya menghasilkan kerusakan setara {serangan_sekarang} untuk target')
        else:
            print(f'{self.nama} sudah kalah dan tidak bisa menyerang.')

