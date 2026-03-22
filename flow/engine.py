def logika_pemilihan_karakter(karakter_1, karakter_2, karakter_3):
    
    karakter_valid = ['elsa', 'bruno', 'dewa', 'joy', 'mikasa']

    tim_pemain = []

    for k in [karakter_1, karakter_2, karakter_3]:
        if karakter.lower() in karakter_valid:
            # Di sini kamu harus melakukan instansiasi objek, contoh:
            # tim_pemain.append(Dewa(hp=100, nama=k))
            tim_pemain.append(k) 
    
    return tim_pemain


# nanti tulis whale (loop ronde disini)
def ronde_pertarungan():
    while True:
        print(f'\n--- giliran pemain ---')
        #pemain.serang(monster)

        if monster.hp < 1:
            print(f'{monster.nama} telah dikalahkan!')
            return 'pertarungan selesai...!'
    
        print(f"--- Giliran {monster.nama} ---")
        monster.serang(pemain)

        if pemain.hp < 1:
            print(f'{pemain.nama} telah dikalahkan!')
            return 'pertarungan selesai...!'

    