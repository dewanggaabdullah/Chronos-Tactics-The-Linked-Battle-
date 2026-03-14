from flow import utills as ut

def elsa():
    print("-- elsa --")
    print("elsa merupakan seorang gadis manis yang suka membantu teman-temannya")
    print("dan bercita cita menjadi dokter yang manis pula")
    print("statistik:")
    print("hp: 30")
    print("atk: 3")
    print("abilitiy: dapat menambah hp rekan tiap ronde sebanyak 3")
    print()

def bruno():
    print('-- bruno --')
    print('dia seorang anak kuat yang hobi nge-gym dan melakukan aktifitas fisik lainnya')
    print('statistik:\nhp: 90\natk: 8')
    print('abillitiy: punya barbel raksasa yang dapat menangkis serangan monster apapun dengan tidak melakukan penyerangan saat ronde berlangsung')
    print()

def dewa():
    print("-- dewa --")
    print("seorang anak yang suka mengotak atik barang dan belajar teknologi,")
    print("dia pernah merakit drone kamikaze berbasis AIG untuk menghancurkan rumah")
    print("tetangganya karna dia mengira tetangganya menciptakan nuklir,namun")
    print("ternyata tidak ada apapun setelah diperiksa disana")
    print("\nstatistik:")
    print("hp: 52")
    print("atk: 30")
    print("\nabillitiy:")
    print("karna marsya menyuruhnya membawa peralatan siaga untuk")
    print("jaga-jaga (marsya suka dengan dewa jir...hahaha),dewa membawa banyak drone")
    print("kamikaze untuk berpetualang ke antah-brantah yang jauh disana")
    print()

def joy():
    print('-- joy --')
    print('ayah joy seorang ilmuan gila yang tergila gila pada kekebalan dan daya tahan tubuh,') 
    print('semenjak ibu joy meninggal dunia karna terpeleset dari lantai kamar mandi,')
    print('joy mengambil suntikan eksperimen ayah nya secara diam-diam untuk dibawa')
    print('(ku harap joy masih hidup setelah dari petualangan dan menjelaskan pada ayahnya apa yang terjadi agar ayahnya tidak semakin gila...)')
    print('statistik:\nhp: 55\natk: 5')


    
    print('abillitiy: joy menyuntikan zat yang membuat semua temannya di dalam petualangan mendapatkan hp tambahan sebanyak 20. (waktu tunggu 3 babak)')
    print()

def marsya():
    print('-- marsya ackerman --')
    print('marsya seorang anak yatim piatu yang dulunya terlantar di alun-alun kota.')
    print('keluarga dewa mengadopsinya dan menganggapnya sebagai anak sendiri dan jadi saudara angkat bagi dewa.')
    print('tidak tau kenapa, tapi marsya sangat kuat dan lincah saat bertengkar dengan bruno dan hampir mengalahkannya demi dewa saat dewa berselisih dengan bruno dulu.')
    print('padahal dia tidak pernah latihan fisik sangat keras seperti bruno')
    print('statistik:')
    print('hp: 45')
    print('atk: 6')
    print('abillitiy: saat bersama dewa, poin serangan marsya bertambah sebanyak 6 poin,dan saat hp dewa berada di bawah 30, poin serangan marsya meningkat sebanyak 100 persen')
    print()


def pilih_karakter():
    ut.bersihkan_terminal()
    print('=== PEMILIHAN KARAKTER ===')
    print()
    print('silahkan pilih 3 dari teman kita untuk dibawa berpetualang...')
    elsa()
    bruno()
    dewa()
    joy()
    marsya()

    try:
        pilih = int(input('apakah lanjut?...\ny/n >>> '))
    except ValueError:
        print('pilih kembali ke menu dengan huruf "n", atau lanjut ke game dengan huruf "y".')
    if pilih == 'y':
        pass
    elif pilih == 'n':
        return 'kembali...'

    print()
    karakter_1 = int(input('silahkan pilih karakter pertama:\n>>>  '))
    karakter_2 = int(input('karakter kedua:\n>>>  '))
    karakter_2 = int(input('karakter ketiga:\n>>>  '))
    

pilih_karakter()