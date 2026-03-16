class Dasar_Karakter:
    def __init__(self, hp, nama):
        self.hp = hp
        self.nama = nama

    def status(self):
        return f'status pertempuran kita sekarang\nnama: {self.nama}\nHP: {self.hp}'
    
class Elsa(Dasar_Karakter):
    def __init__(self, hp, nama):
        super().__init__(nama, hp)
        self.atk = 3
        self.ability = 3

    def pasif_heal(self, daftar_tim):
        print(f'{self.nama} mengobati hp tim sebanyak {self.ability}')
        for anggota in daftar_tim:
            anggota.hp += self.ability

