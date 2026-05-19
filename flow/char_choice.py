from flow import utils as ut
from flow import units as un

def pemilihan_karakter(k1, k2, k3):
    tim_pemain = {}
    for nama_input in [k1.lower(), k2.lower(), k3.lower()]:
        if nama_input in un.attribute_karakter:
            attribute_karakter = un.attribute_karakter[nama_input]

            tim_pemain[nama_input] = attribute_karakter

    return tim_pemain # <--- tim_pemain disini berbentuk dictionary
   
def validasi_karakter():
    while True:
        try:
            tanya = input('apakah tetap lanjut ke permainan?...\ny/n >>> ').strip().lower()
    
            if tanya == 'y':
                print()
                nama_input1 = input('silahkan pilih karakter pertama:\n>>>  ').strip()
                nama_input2 = input('karakter kedua:\n>>>  ').strip()
                nama_input3 = input('karakter ketiga:\n>>>  ').strip()
                
                tim_pemain = [nama_input1, nama_input2, nama_input3]

                # logika sebelum permainan benar-benar berjalan dan cek jika ada yang sama atau ada yang kosong
                # set = pengumpulan data yang harus beda
                # len = hitung isi dalam list
                if len(set(tim_pemain)) < 3 or "" in tim_pemain:
                    raise ValueError('nama kembar atau kosong')

                for nama in tim_pemain:
                    if nama not in KARAKTER_VALID:
                        raise ValueError('karakter tidak valid')

                # kembalikan list nama yang udah di validasikan    
                return tim_pemain
            
            elif tanya == 'n':
                ut.bersihkan_terminal()
                return None
            
            else:
                print('pilih kembali ke menu dengan huruf "n", atau "y" untuk melanjutkan game.')
                continue
        
        except ValueError:
            if str(e) == "nama_kembar_atau_kosong":
                print('\n[!] Nama karakter tidak boleh sama atau ada yang kosong! Silakan pilih ulang.')
            elif str(e) == "karakter_tidak_valid":
                print(f'\n[!] Ada nama karakter yang tidak terdaftar! Karakter yang tersedia: {", ".join(KARAKTER_VALID).upper()}')
        
        except Exception as e:
            print(f'ada kesalahan yang tak terduga... \npesan buat developer\n')
            traceback.print_exc() # ini bakal nampilin tulisan error traceback buat mempermudah debug


