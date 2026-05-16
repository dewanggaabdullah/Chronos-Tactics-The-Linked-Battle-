# module built-in
import time
import textwrap
import sys

# module library
from pynput import keyboard

# module bikin
from flow import utils as ut

# story setiap karakter
cerita_karakter = {
    'elsa': "-- elsa --\n    elsa merupakan seorang gadis manis yang suka membantu teman-temannya dan bercita cita menjadi dokter yang manis pula.\nSTATISTIK:\nhp: 75\natk: 5\nkemampuan:  dapat menambah hp rekan tiap ronde sebanyak 7",
    'bruno': "-- bruno --\n    dia seorang anak kuat yang hobi nge-gym dan suka melakukan aktifitas fisik berat.\nSTATISTIK:\nhp: 150\natk: 12\nkemampuan:  punya barbel raksasa yang dapat menangkis serangan monster apapun dengan tidak melakukan penyerangan saat ronde berlangsung",
    'dewa': "-- dewa --\n    seorang anak yang suka mengotak atik barang dan belajar teknologi,dia pernah merakit drone kamikaze berbasis AGI untuk menghancurkan rumah tetangganya karna dia mengira tetangganya menciptakan nuklir,namun ternyata tidak ada apapun setelah diperiksa disana...\nSTATISTIK:\nhp: 85\natk: 30\nkemampuan:  karna mikasa menyuruhnya membawa peralatan siaga untuk jaga-jaga (marsya suka dengan dewa jir...hahaha),dewa membawa banyak drone kamikaze dan sedikit persediaan operasi militer khusus untuk berpetualang ke antah-brantah yang jauh disana.\nkemampuan: damage dasar tertinggi dalam tim, dan setiap 3 babak bisa memberikan damage critical(40 damage)",
    'joy':  "-- joy --\n    ayah joy seorang ilmuan gila yang tergila gila pada kekebalan dan daya tahan tubuh. semenjak ibu joy meninggal dunia karna terpeleset dari lantai kamar mandi. joy mengambil suntikan eksperimen ayah nya secara diam-diam untuk dibawa (ku harap joy masih hidup setelah kembali dari petualangan dan menjelaskan pada ayahnya apa yang terjadi agar ayahnya tidak semakin gila...).\nSTATISTIK:\nhp: 90\natk: 10\nkemampuan:  joy menyuntikan zat yang membuat semua temannya di dalam petualangan mendapatkan hp tambahan sebanyak 20. (waktu tunggu 3 babak)",
    'mikasa': "-- mikasa --\n    mikasa seorang anak yatim piatu yang dulunya terlantar di alun-alun kota. keluarga dewa mengadopsinya dan menganggapnya sebagai anak sendiri dan jadi saudara angkat bagi dewa. tidak tau kenapa, tapi mikasa sangat kuat dan lincah saat bertengkar dengan bruno dan hampir mengalahkannya demi dewa saat dewa berselisih dengan bruno dulu, padahal dia tidak pernah latihan fisik sangat keras seperti bruno.\nSTATISTIK:\nhp: 90\natk: 10\nkemampuan:  saat bersama dewa, poin serangan mikasa bertambah sebanyak 10 poin dan saat hp dewa berada di bawah 30, seluruh poin serangan mikasa meningkat sebanyak 100 persen"
} 

# wadah pemberitahuan umum in-game, aku pakai sistem format biar clean
# ofensif
tim_menyerang = "\n[x] {nama} menyerang! memberikan damage sebesar {damage}."
monster_menyerang = '\n[x] {monster} mulai menyerang...!, kali ini serangannya menghasilkan kerusakan setara {damage} untuk {target}'

# defensif
karakter_diserang = '[-] {nama} menerima serangan...! Hp tersisa: {hp}'
kabur = '\n[lol] kalian melarikan diri...!, monster itu terlalu kuat dan kalian ternyata hanya seekor anak ayam di mata seorang monster perkasa...(wkwk)\n<<< GAME OVER >>>'

# menang/kalah
pilihan_char_kalah = '\n[!] {nama} sudah tidak berdaya, pilih teman yang lain!'
karakter_kalah = '\n[!] {nama} tidak sanggup melanjutkan pertempuran... terus berjuang..!!!'
game_kalah = '\n[!] GAME OVER.. tidak ada lagi anggota dalam tim yang sanggup melanjutkan pertarungan\nCRONOS SPARKLE DIAKTIFKAN... KEMBALI KE MASA LALU!!!'
monster_kalah = '\n[!] berhasil...!!!, {monster} telah dikalahkan...'

# pesan lain-lain
kedatangan_monster = '\n[!] sebuah {monster} muncul di perjalanan...!'
nama_char_tidak_ada = '\n[?] nama tersebut tidak ada di dalam tim atau salah ketik'

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

    # ini akan merapikan text yang bikin rusak visual di layar, ini dari module textwrap

    wrapper = textwrap.TextWrapper(width=50, replace_whitespace=False) # 50 bisa di edit sesuai lebar layar
    text = wrapper.fill(text=text)
    
    for char in text:
        print(char, end='', flush=True)
        if skip == False:
            time.sleep(delay)

    # print di pakai untuk bikin spasi setelah for di laksanakan.

    print()

    # kalau gunanya .stop() buat berhentiin listener mantau input sesudah loop selesai kasih output
    if listener.running:
        listener.stop()

def prolog(durasi = 0.5):
    ut.bersihkan_terminal()
    prolog1 = 'game_dimulai...'
    prolog2 = 'enjoy!'
    print_story(prolog1)
    print_story(prolog2) 
    time.sleep(1.5)

    ut.bersihkan_terminal()
    print('=== PEMILIHAN KARAKTER ===')
    print('silahkan pilih 3 dari teman kita untuk dibawa berpetualang...')
    print()
    print()
    print('<< tekan spasi untuk skip keluarnya text >>')
    print('\n' + '='*55 + '\n') # biar rapi

    # ambil isi dictionary cerita_karakter buat di tampilkan ke layar
    for text in cerita_karakter.values():
        print_story(text)
        print('\n' + '='*55 + '\n') # biar rapi
        time.sleep(durasi)

