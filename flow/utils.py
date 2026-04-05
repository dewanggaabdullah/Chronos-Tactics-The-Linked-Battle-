import os
import time
from pynput import keyboard

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
def print_story(text, speed='normal'):
    skip = False
    """
    nonlocal dipakai buat ambil variabel dari fungsi induk,
    jadi konsepnya mirip sama inheritance(pewarisan) class
    """
    def skip_story(Key):
        nonlocal skip
        if Key == keyboard.Key.space:
            skip = True
            return False

    
    # listener di pakai buat jalanin fungsi skip story di latar belakang
    # fungsi dari .start() itu gunanya biar variabel listener jalan di latar belakang
    # saat program utama di jalankan 
    
    listener = keyboard.Listener(on_press = skip_story)
    listener.start()

    # Print teks dengan kecepatan berbeda
    # Set kecepatan

    speeds = {
        'lambat': 0.1,
        'normal': 0.05,
        'cepat': 0.02,
        'dramatis': 0.08
    }
    
    delay = speeds.get(speed, 0.05)
    
    for char in text:
        print(char, end='', flush=True)
        if skip == False:
            time.sleep(delay)

    # print di pakai untuk bikin spasi setelah for di laksanakan.

    print()

    # kalau gunanya .stop() buat berhentiin listener mantau input sesudah loop selesai kasih output
    if listener.running:
        listener.stop()
