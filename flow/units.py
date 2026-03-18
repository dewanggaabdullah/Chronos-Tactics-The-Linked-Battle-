import random

class Dasar_Karakter:
    def __init__(self, hp, nama):
        self.hp = hp
        self.nama = nama

    def status(self):
        return f'status pertempuran kita sekarang\nnama: {self.nama}\nHP: {self.hp}'
    
class Elsa(Dasar_Karakter):
    def __init__(self, hp, nama):
        super().__init__(hp, nama)
        self.atk = 3
        self.ability = 3

    def pasif_heal(self, daftar_tim):
        for anggota in daftar_tim:
            anggota.hp += self.ability
        
        print(f'{self.nama} mengobati hp tim sebanyak {self.ability}')

    def serang(self, lawan):
        lawan.hp -= self.atk

        print(f'{self.nama} mencoba menyerang...!, dan berhasil mengurangi hp {lawan} sebanyak {self.atk}')

class Bruno(Dasar_Karakter):
    def __init__(self, hp, nama):
        super().__init__(hp, nama, tangkis = False)
        self.atk = 12

    def tangkis():
        print(f'bruno menggunakan barbelnya, menangkis serangan monster dengan mudah...!')




class Monster(Dasar_Karakter):
    def __init__(self, hp, nama):
        super().__init__(hp, nama)
        self.daftar_atk = [40,15,17,13]
       
    def serang(self, target):
        serangan_sekarang = random.choise(self.daftar_atk)
        target.hp -= serangan_sekarang

        print(f'{self.nama} menyerang...!, kali ini serangannya menghasilkan kerusakan setara {serangan_sekarang} untuk target')


