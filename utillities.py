import os
import time

def clear_vscode_terminal():
    """Fungsi clear yang dioptimalkan untuk VS Code"""
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

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