from flow import utils as ut
from flow import units as un
import traceback

def pemilihan_karakter(k1, k2, k3):
    tim_pemain = {}
    for nama_input in [k1.lower(), k2.lower(), k3.lower()]:
        if nama_input in un.attribute_karakter:
            karakter_class = un.attribute_karakter[nama_input]

            tim_pemain[nama_input] = attribute_karakter

    return tim_pemain
   
   
def validasi_karakter():
    while True:
        try:
            tanya = 'y' 
    
            if tanya == 'y':
                print()
                nama_input1 = 'elsa' 
                nama_input2 = 'bruno' 
                nama_input3 = 'joy' 
                
                tim_pemain = [nama_input1, nama_input2, nama_input3]

                if len(set(tim_pemain)) < 3 or "" in tim_pemain:
                    raise ValueError('nama kembar atau kosong')

                KARAKTER_VALID = ['elsa', 'bruno', 'dewa', 'joy', 'mikasa']

                for nama in tim_pemain:
                    if nama not in KARAKTER_VALID:
                        raise ValueError('karakter tidak valid')
    
                return tim_pemain
            
            elif tanya == 'n':
                ut.bersihkan_terminal()
                return None
            
            else:
                print('pilih kembali ke menu dengan huruf "n", atau "y" untuk melanjutkan game.')
                continue
        
        except ValueError as e:
            if str(e) == "nama kembar atau kosong":
                print('\n[!] Nama karakter tidak boleh sama atau ada yang kosong! Silakan pilih ulang.')
            elif str(e) == "karakter_tidak_valid":
                print(f'\n[!] Ada nama karakter yang tidak terdaftar! Karakter yang tersedia: {", ".join(KARAKTER_VALID).upper()}')
        
        except Exception as e:
            print(f'ada kesalahan yang tak terduga... \npesan buat developer\n')
            traceback.print_exc() 
