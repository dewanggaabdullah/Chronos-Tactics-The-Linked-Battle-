from flow import utills as ut

def cerita_karakter():
    deskripsi_elsa = "-- elsa --\nelsa merupakan seorang gadis manis yang suka membantu teman-temannya dan bercita cita menjadi dokter yang manis pula.\nstatistik:\nhp: 75\natk: 5\nkemampuan:  dapat menambah hp rekan tiap ronde sebanyak 7"

    deskripsi_bruno ="-- bruno --\ndia seorang anak kuat yang hobi nge-gym dan suka melakukan aktifitas fisik berat.\nstatistik:\nhp: 150\natk: 12\nkemampuan:  punya barbel raksasa yang dapat menangkis serangan monster apapun dengan tidak melakukan penyerangan saat ronde berlangsung"

    deskripsi_dewa = "-- dewa --\nseorang anak yang suka mengotak atik barang dan belajar teknologi,dia pernah merakit drone kamikaze berbasis AGI untuk menghancurkan rumah tetangganya karna dia mengira tetangganya menciptakan nuklir,namun ternyata tidak ada apapun setelah diperiksa disana...\nstatistik:\nhp: 85\natk: 30\nkemampuan:  karna marsya menyuruhnya membawa peralatan siaga untukjaga-jaga (marsya suka dengan dewa jir...hahaha),dewa membawa banyak drone kamikaze untuk berpetualang ke antah-brantah yang jauh disana.\n pasif: damage dasar tertinggi dalam tim"

    deskripsi_joy =  "-- joy --\nayah joy seorang ilmuan gila yang tergila gila pada kekebalan dan daya tahan tubuh. semenjak ibu joy meninggal dunia karna terpeleset dari lantai kamar mandi. joy mengambil suntikan eksperimen ayah nya secara diam-diam untuk dibawa (ku harap joy masih hidup setelah kembali dari petualangan dan menjelaskan pada ayahnya apa yang terjadi agar ayahnya tidak semakin gila...).\nstatistik:\nhp: 90\natk: 10\nkemampuan:  joy menyuntikan zat yang membuat semua temannya di dalam petualangan mendapatkan hp tambahan sebanyak 20. (waktu tunggu 3 babak)"

    deskripsi_mikasa ="-- mikasa --\nmikasa seorang anak yatim piatu yang dulunya terlantar di alun-alun kota. keluarga dewa mengadopsinya dan menganggapnya sebagai anak sendiri dan jadi saudara angkat bagi dewa. tidak tau kenapa, tapi mikasa sangat kuat dan lincah saat bertengkar dengan bruno dan hampir mengalahkannya demi dewa saat dewa berselisih dengan bruno dulu, padahal dia tidak pernah latihan fisik sangat keras seperti bruno.\nstatistik:\nhp: 90\natk: 10\nkemampuan:  saat bersama dewa, poin serangan mikasa bertambah sebanyak 10 poin dan saat hp dewa berada di bawah 30, seluruh poin serangan marsya meningkat sebanyak 100 persen"

    def prolog_karakter(karakter, durasi = 0.5):
        ut.print_story(karakter)
        print()
        ut.time.sleep(durasi)

    prolog_karakter(deskripsi_elsa)
    prolog_karakter(deskripsi_bruno)
    prolog_karakter(deskripsi_dewa)
    prolog_karakter(deskripsi_joy)
    prolog_karakter(deskripsi_mikasa)
    
def pemilihan_karakter(k1, k2, k3):
    karakter_valid = ['elsa', 'bruno', 'dewa', 'joy', 'mikasa']
    tim_pemain = []
    for karakter in [k1.lower(), k2.lower(), k3.lower()]:
        if karakter in karakter_valid:
            data = attribute_karakter[karakter]
            objek_karakter = Karakter(nama = karakter, hp = data['hp'], attack=data['atk'])
            tim_pemain.append(objek_karakter)
    return tim_pemain

def validasi_karakter():
    #aku mempelajari kalau variabel global harus di devenisikan dulu
    global karakter_1, karakter_2, karakter_3

    while True:
        try:
            tanya = input('apakah lanjut?...(jangan ada spasi didalam input)\ny/n >>> ')
    
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
                karakter_aktif = pemilihan_karakter(karakter_1, karakter_2, karakter_3)
                return karakter_aktif
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
        """except Exception as e:
            print(f'ada kesalahan yang tak terduga... \npesan buat developer\n{e}')
            break"""

