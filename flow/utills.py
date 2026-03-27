import os
import time
from pynput import keyboard

def bersihkan_terminal():
    """Fungsi clear yang dioptimalkan untuk VS Code"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def print_story(text, speed='normal'):
    # variabel sama fungsi yang nanti bisa bikin story ke skip untuk mempercepat debugging
    # atau waktu user ke isi permainan
    skip = False

    def skip_story(key):
        nonlocal skip
        if skip == keyboard.Key.space:
            skip = True
            return False

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
    print()

