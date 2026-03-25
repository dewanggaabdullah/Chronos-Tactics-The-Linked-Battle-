from flow import utills as ut
from flow import engine as en

def elsa():
    print("-- elsa --")
    print("elsa merupakan seorang gadis manis yang suka membantu teman-temannya")
    print("dan bercita cita menjadi dokter yang manis pula")
    print("statistik:")
    print("hp: 75")
    print("atk: 5")
    print("abilitiy: dapat menambah hp rekan tiap ronde sebanyak 7")
    print()
    ut.time.sleep(3)

def bruno():
    print('-- bruno --')
    print('dia seorang anak kuat yang hobi nge-gym dan melakukan aktifitas fisik lainnya')
    print('statistik:')
    print('hp: 150')
    print('atk: 12')
    print('abillitiy: punya barbel raksasa yang dapat menangkis serangan monster apapun dengan tidak melakukan penyerangan saat ronde berlangsung')
    print()
    ut.time.sleep(3)

def dewa():
    print("-- dewa --")
    print("seorang anak yang suka mengotak atik barang dan belajar teknologi,")
    print("dia pernah merakit drone kamikaze berbasis AIG untuk menghancurkan rumah")
    print("tetangganya karna dia mengira tetangganya menciptakan nuklir,namun")
    print("ternyata tidak ada apapun setelah diperiksa disana")
    print("statistik:")
    print("hp: 85")
    print("atk: 30")
    print("abillitiy:")
    print("karna marsya menyuruhnya membawa peralatan siaga untuk")
    print("jaga-jaga (marsya suka dengan dewa jir...hahaha),dewa membawa banyak drone")
    print("kamikaze untuk berpetualang ke antah-brantah yang jauh disana")
    print('(pasif damage dasar tertinggi dalam tim)')
    print()
    ut.time.sleep(3)

def joy():
    print('-- joy --')
    print('ayah joy seorang ilmuan gila yang tergila gila pada kekebalan dan daya tahan tubuh,') 
    print('semenjak ibu joy meninggal dunia karna terpeleset dari lantai kamar mandi,')
    print('joy mengambil suntikan eksperimen ayah nya secara diam-diam untuk dibawa')
    print('(ku harap joy masih hidup setelah dari petualangan dan menjelaskan pada ayahnya apa yang terjadi agar ayahnya tidak semakin gila...)')
    print('statistik:')
    print('hp: 90')
    print('atk: 10')
    print("abillitiy: joy menyuntikan zat yang membuat semua temannya di dalam petualangan mendapatkan hp tambahan sebanyak 20. (waktu tunggu 3 babak)")
    print()
    ut.time.sleep(3)

def mikasa():
    print('-- mikasa --')
    print('mikasa seorang anak yatim piatu yang dulunya terlantar di alun-alun kota.')
    print('keluarga dewa mengadopsinya dan menganggapnya sebagai anak sendiri dan jadi saudara angkat bagi dewa.')
    print('tidak tau kenapa, tapi mikasa sangat kuat dan lincah saat bertengkar dengan bruno dan hampir mengalahkannya demi dewa saat dewa berselisih dengan bruno dulu.')
    print('padahal dia tidak pernah latihan fisik sangat keras seperti bruno')
    print('statistik:')
    print('hp: 100')
    print('atk: 10')
    print('abillitiy: saat bersama dewa, poin serangan mikasa bertambah sebanyak 10 poin,dan saat hp dewa berada di bawah 30, seluruh poin serangan marsya meningkat sebanyak 100 persen')
    print()
    ut.time.sleep(1.5)

def validasi_karakter():
    from main import game_loop

    while True:
        try:
            tanya = input('apakah lanjut?...\ny/n >>> ')
    
            if tanya == 'y':
                print()
                karakter_1 = input('silahkan pilih karakter pertama:\n>>>  ')
                karakter_2 = input('karakter kedua:\n>>>  ')
                karakter_3 = input('karakter ketiga:\n>>>  ')
            elif tanya == 'n':
                ut.bersihkan_terminal()
                print('kembali...')
                game_loop()
                continue
            else:
                print('pilih kembali ke menu dengan huruf "n", atau "y" untuk melanjutkan game.')

            if karakter_1 not in [karakter_2, karakter_3]:
                pass
            else:
                raise ValueError
        
            if karakter_2 not in [karakter_1, karakter_3]:
                pass
            else:
                raise ValueError
        
            if karakter_3 not in [karakter_2, karakter_1]:
                pass
            else:
                raise ValueError
            
            en.logika_pemilihan_karakter(karakter_1, karakter_2, karakter_3)
        
        except NameError:
            print('tidak boleh memilih nama karakter yang sama...')
            continue
        #except Exception:
            #print('kesalahan tidak terduga... tolong kasih saran buat perbaikan.')

def pilih_karakter():
    ut.bersihkan_terminal()
    print('=== PEMILIHAN KARAKTER ===')
    print()
    print('silahkan pilih 3 dari teman kita untuk dibawa berpetualang...')
    elsa()
    bruno()
    dewa()
    joy()
    mikasa()

    validasi_karakter()