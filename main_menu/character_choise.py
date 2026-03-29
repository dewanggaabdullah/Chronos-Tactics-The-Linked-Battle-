from flow import utills as ut
from flow import engine as en

def cerita_karakter():
    deskripsi_elsa = """        -- elsa --
    elsa merupakan seorang gadis manis yang suka membantu teman-temannya
    dan bercita cita menjadi dokter yang manis pula.

    statistik:
    hp: 75
    atk: 5
    kemampuan:  dapat menambah hp rekan tiap ronde sebanyak 7"""

    deskripsi_bruno ="""        -- bruno --
    dia seorang anak kuat yang hobi nge-gym dan suka melakukan aktifitas fisik berat.

    statistik:
    hp: 150
    atk: 12
    kemampuan:  punya barbel raksasa yang dapat menangkis serangan monster apapun 
                dengan tidak melakukan penyerangan saat ronde berlangsung"""

    deskripsi_dewa = """        -- dewa --
    seorang anak yang suka mengotak atik barang dan belajar teknologi
    dia pernah merakit drone kamikaze berbasis AGI untuk menghancurkan rumah
    tetangganya karna dia mengira tetangganya menciptakan nuklir,namun
    ternyata tidak ada apapun setelah diperiksa disana...

    statistik:
    hp: 85
    atk: 30
    kemampuan:  karna marsya menyuruhnya membawa peralatan siaga untuk
                jaga-jaga (marsya suka dengan dewa jir...hahaha),dewa membawa 
                banyak drone kamikaze untuk berpetualang ke antah-brantah yang 
                jauh disana pasif damage dasar tertinggi dalam tim"""

    deskripsi_joy =  """        -- joy --
    ayah joy seorang ilmuan gila yang tergila gila pada kekebalan dan daya tahan tubuh. 
    semenjak ibu joy meninggal dunia karna terpeleset dari lantai kamar mandi. 
    joy mengambil suntikan eksperimen ayah nya secara diam-diam untuk dibawa
    (ku harap joy masih hidup setelah kembali dari petualangan dan menjelaskan 
    pada ayahnya apa yang terjadi agar ayahnya tidak semakin gila...).

    statistik:
    hp: 90
    atk: 10
    kemampuan:  joy menyuntikan zat yang membuat semua temannya di dalam petualangan 
                mendapatkan hp tambahan sebanyak 20. (waktu tunggu 3 babak)"""

    deskripsi_mikasa ="""       -- mikasa --
    mikasa seorang anak yatim piatu yang dulunya terlantar di alun-alun kota.
    keluarga dewa mengadopsinya dan menganggapnya sebagai anak sendiri dan jadi 
    saudara angkat bagi dewa. tidak tau kenapa, tapi mikasa sangat kuat dan lincah 
    saat bertengkar dengan bruno dan hampir mengalahkannya demi dewa saat dewa 
    berselisih dengan bruno dulu,
    padahal dia tidak pernah latihan fisik sangat keras
    seperti bruno.

    statistik:
    hp: 100
    atk: 10
    kemampuan:  saat bersama dewa, poin serangan mikasa bertambah sebanyak 10 poin
                dan saat hp dewa berada di bawah 30, seluruh poin serangan marsya 
                meningkat sebanyak 100 persen"""

    def prolog_karakter(karakter, durasi = 0.5):
        ut.print_story(karakter)
        print()
        ut.time.sleep(durasi)

    prolog_karakter(deskripsi_elsa)
    prolog_karakter(deskripsi_bruno)
    prolog_karakter(deskripsi_dewa)
    prolog_karakter(deskripsi_joy)
    prolog_karakter(deskripsi_mikasa)
    
def validasi_karakter():
    #aku mempelajari kalau variabel global harus di devenisikan dulu
    global karakter_1, karakter_2, karakter_3

    while True:
        try:
            tanya = input('apakah lanjut?...\ny/n >>> ')
    
            if tanya == 'y':
                print()
                karakter_1 = input('silahkan pilih karakter pertama:\n>>>  ')
                karakter_2 = input('karakter kedua:\n>>>  ')
                karakter_3 = input('karakter ketiga:\n>>>  ')

                #logika sebelum permainan benar-benar berjalan dan cek jika ada yang sama atau ada yang kosong
                #set = pengumpulan data yang harus beda
                #len = hitung isi dalam list
                isi_karakter = [karakter_1, karakter_2, karakter_3]
                if len(set(isi_karakter)) < 3 or "" in isi_karakter:
                    raise ValueError
                en.logika_pemilihan_karakter(karakter_1, karakter_2, karakter_3)
                break
            
            elif tanya == 'n':
                ut.bersihkan_terminal()
                return 'kembali...'
            
            else:
                print('pilih kembali ke menu dengan huruf "n", atau "y" untuk melanjutkan game.')
                continue
        
        except NameError:
            print('tidak boleh memilih nama karakter yang sama...')
        except ValueError:
            print('nama karakter tidak boleh sama atau nama tidak ada')
        except Exception as e:
            print(f'ada kesalahan yang tak terduga... \npesan buat developer\n{e}')
            break

def game_dimulai():
    ut.bersihkan_terminal()
    print('=== PEMILIHAN KARAKTER ===')
    print('silahkan pilih 3 dari teman kita untuk dibawa berpetualang...')
    print()
    cerita_karakter()
    validasi_karakter()