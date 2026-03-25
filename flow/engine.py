from flow import units as un

def logika_pemilihan_karakter(k1, k2, k3):
    karakter_valid = ['elsa', 'bruno', 'dewa', 'joy', 'mikasa']
    tim_pemain = []
    for karakter in [k1.lower, k2.lower, k3.lower]:
        if karakter in karakter_valid:
            data = attribute_karakter[karakter]
            objek_karakter = Karakter(nama = karakter, hp = data['hp'], attack=data['atk'])
            tim_pemain.append(objek_karakter)
    return tim_pemain

def ronde_pertarungan(tim_pemain, monster):
    print(f"\n--- RONDE DIMULAI: Melawan {monster['nama']} ---")
    
    for hero in tim_pemain:
        if monster['hp'] > 0:
            monster['hp'] -= hero.attack
            print(f"{hero.nama.capitalize()} menyerang! Damage: {hero.attack}. HP Monster: {max(0, monster['hp'])}")
    
    # Jika monster masih hidup, dia balas menyerang salah satu (misal yang pertama)
    if monster['hp'] > 0:
        target = tim_pemain[0] # Monster nyerang karakter pertama
        target.hp -= monster['atk']
        print(f"Monster balas menyerang {target.nama}! HP {target.nama} sisa: {target.hp}")

# CONTOH MENJALANKANNYA:
#team = logika_pemilihan_karakter('elsa', 'dewa', 'mikasa')
#monster_bos = {'nama': 'Giant Slime', 'hp': 200, 'atk': 20}
#battle_round(team, monster)

    