from flow import utils as ut
from flow import units as un

def pemilihan_karakter(k1, k2, k3):
    tim_pemain = {}
    for nama_input in [k1.lower(), k2.lower(), k3.lower()]:
        if nama_input in un.attribute_karakter:
            attribute_karakter = un.attribute_karakter[nama_input]

            tim_pemain[nama_input] = attribute_karakter

    return tim_pemain

def validasi_karakter():
    #aku mempelajari kalau variabel global harus di devenisikan dulu
    global nama_input1, nama_input2, nama_input3

    while True:
        try:
            tanya = input('apakah tetap lanjut ke permainan?...\ny/n >>> ').strip().lower()
    
            if tanya == 'y':
                print()
                nama_input1 = 'dewa' #input('silahkan pilih karakter pertama:\n>>>  ').strip()
                nama_input2 = 'joy' #input('karakter kedua:\n>>>  ').strip()
                nama_input3 = 'mikasa' #input('karakter ketiga:\n>>>  ').strip()

                #logika sebelum permainan benar-benar berjalan dan cek jika ada yang sama atau ada yang kosong
                #set = pengumpulan data yang harus beda
                #len = hitung isi dalam list
                tim_pemain = [nama_input1, nama_input2, nama_input3]
                if len(set(tim_pemain)) < 3 or "" in tim_pemain:
                    raise ValueError
                return tim_pemain
                break
            
            elif tanya == 'n':
                ut.bersihkan_terminal()
                return 'kembali...'
            
            else:
                print('pilih kembali ke menu dengan huruf "n", atau "y" untuk melanjutkan game.')
                continue
        
        except ValueError:
            print('nama karakter tidak boleh sama atau nama karakter tidak ada')
        """except NameError:
            print('tidak boleh memilih nama karakter yang sama...')"""
        """except Exception as e:
            print(f'ada kesalahan yang tak terduga... \npesan buat developer\n{e}')
            break"""

