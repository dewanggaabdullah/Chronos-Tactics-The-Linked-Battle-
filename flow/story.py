# ============================================================
# DATA CERITA KARAKTER
# ============================================================

cerita_karakter = {
    "elsa": (
        "-- Elsa --\n"
        "Elsa merupakan seorang gadis manis yang suka membantu "
        "teman-temannya dan bercita-cita menjadi dokter.\n\n"
        "STATISTIK:\n"
        "HP: 75\n"
        "ATK: 5\n"
        "Kemampuan: dapat menambah HP rekan tiap ronde sebanyak 7."
    ),

    "bruno": (
        "-- Bruno --\n"
        "Dia seorang anak kuat yang hobi nge-gym dan suka melakukan "
        "aktivitas fisik berat.\n\n"
        "STATISTIK:\n"
        "HP: 150\n"
        "ATK: 9\n"
        "Kemampuan: punya barbel raksasa yang dapat menangkis "
        "serangan monster dengan tidak melakukan penyerangan "
        "saat ronde berlangsung."
    ),

    "dewa": (
        "-- Dewa --\n"
        "Seorang anak yang suka mengotak-atik barang dan belajar "
        "teknologi. Dia pernah merakit drone kamikaze berbasis AGI "
        "untuk menghancurkan rumah tetangganya karena mengira "
        "tetangganya menciptakan nuklir. Namun ternyata tidak ada "
        "apapun setelah diperiksa di sana.\n\n"
        "STATISTIK:\n"
        "HP: 85\n"
        "ATK: 30\n"
        "Kemampuan: damage dasar tertinggi dalam tim dan setiap "
        "3 babak dapat memberikan critical damage sebesar 40."
    ),

    "joy": (
        "-- Joy --\n"
        "Ayah Joy seorang ilmuwan gila yang tergila-gila pada "
        "kekebalan dan daya tahan tubuh. Sejak ibu Joy meninggal "
        "karena terpeleset di kamar mandi, Joy mengambil suntikan "
        "eksperimen ayahnya secara diam-diam untuk dibawa dalam "
        "petualangan.\n\n"
        "STATISTIK:\n"
        "HP: 90\n"
        "ATK: 10\n"
        "Kemampuan: menyuntikkan zat yang membuat semua teman "
        "dalam petualangan mendapatkan tambahan HP sebanyak 20. "
        "(Waktu tunggu: 3 babak)"
    ),

    "mikasa": (
        "-- Mikasa --\n"
        "Mikasa seorang anak yatim piatu yang dulunya terlantar "
        "di alun-alun kota. Keluarga Dewa mengadopsinya dan "
        "menganggapnya sebagai anak sendiri.\n\n"
        "Dia sangat kuat dan lincah. Saat bersama Dewa, dia "
        "bahkan pernah hampir mengalahkan Bruno.\n\n"
        "STATISTIK:\n"
        "HP: 90\n"
        "ATK: 10\n"
        "Kemampuan: saat bersama Dewa, serangan Mikasa bertambah "
        "10 poin. Saat HP Dewa berada di bawah 30, seluruh "
        "serangan Mikasa meningkat 100 persen."
    ),
}


# ============================================================
# PESAN OFENSIF
# ============================================================

tim_menyerang = (
    "\n[x] {nama} menyerang! Memberikan damage sebesar {damage}."
)

monster_menyerang = (
    "\n[x] {monster} mulai menyerang! Serangannya menghasilkan "
    "kerusakan sebesar {damage} untuk {target}."
)


# ============================================================
# PESAN DEFENSIF
# ============================================================

karakter_diserang = (
    "[-] {nama} menerima serangan! HP tersisa: {hp}"
)

kabur = (
    "\nKalian melarikan diri! Monster itu terlalu kuat dan "
    "kalian ternyata hanya seekor anak ayam di mata monster "
    "perkasa tersebut.\n\n"
    "<<< GAME OVER >>>"
)


# ============================================================
# PESAN MENANG / KALAH
# ============================================================

pilihan_char_kalah = (
    "\n[!] {nama} sudah tidak berdaya. Pilih teman yang lain!"
)

karakter_kalah = (
    "\n[!] {nama} tidak sanggup melanjutkan pertempuran. "
    "Terus berjuang!"
)

game_kalah = (
    "\n[!] GAME OVER. Tidak ada lagi anggota dalam tim yang "
    "sanggup melanjutkan pertarungan.\n\n"
    "CRONOS SPARKLE DIAKTIFKAN...\n"
    "KEMBALI KE MASA LALU!"
)

monster_kalah = (
    "\n[!] Berhasil! {monster} telah dikalahkan!"
)


# ============================================================
# PESAN LAIN-LAIN
# ============================================================

kedatangan_monster = (
    "\n[!] Sebuah {monster} muncul di perjalanan!"
)

nama_char_tidak_ada = (
    "\n[?] Nama tersebut tidak ada di dalam tim atau salah ketik."
)

skill_cooldown = (
    "\n[!] Skill {nama} sedang cooldown. Skill akan terbuka "
    "{cooldown} ronde lagi."
)


# ============================================================
# PROLOG
# ============================================================

def ambil_prolog():
    return {
        "judul": "CRONOS TACTICS: The Linked Battle",
        "pembuka": [
            "Game dimulai...",
            "Enjoy!",
        ],
        "instruksi": (
            "Silakan pilih 3 dari teman kita "
            "untuk dibawa berpetualang."
        ),
        "karakter": list(cerita_karakter.values())
    }