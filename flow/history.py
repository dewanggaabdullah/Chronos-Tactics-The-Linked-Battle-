import time
import os

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_story(text, speed='normal'):
    """Print teks dengan kecepatan berbeda"""
    
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
        time.sleep(delay)
    print()

# Contoh story telling
def intro_cerita():
    clear_screen()
    
    print_story("DIAM...", 'lambat')
    time.sleep(1)
    print_story("Sunyi sekali...", 'lambat')
    time.sleep(1)
    print_story("\nTiba-tiba...", 'dramatis')
    time.sleep(1.5)
    print_story("BRAAAK!!!", 'cepat')
    time.sleep(0.5)
    print_story("Pintu terbuka dengan kerasnya!", 'normal')

intro_cerita()