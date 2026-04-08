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

# variabel sama fungsi yang nanti bisa bikin story ke skip untuk mempercepat debugging
# atau waktu user ke isi permainan
# nanti si 'skip' ini yang jadi sakelar buat delay outputnya
