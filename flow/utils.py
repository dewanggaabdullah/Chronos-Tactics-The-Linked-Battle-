import os

def bersihkan_terminal():
    """
    Fungsi clear yang dioptimalkan untuk VS Code, 'nt' buat os windows, dan else buat sistem terminal linux yang
    gunain perintah clear sebagai prompt nya.
    """
    if os.name == 'nt':
        os.system('cls') 
    else:
        os.system('clear')

# Kode Warna ANSI
merah  = "\033[91m"
hijau  = "\033[92m"
kuning = "\033[93m"
biru   = "\033[94m"
RESET  = "\033[0m" # <--- reset buat balikin warna ke semula dan biar tulisan bawahnya gak ikutan berwarna

# variabel sama fungsi yang nanti bisa bikin story ke skip untuk mempercepat debugging
# atau waktu user ke isi permainan
# nanti si 'skip' ini yang jadi sakelar buat delay outputnya
