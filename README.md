# ⚔️ Chronos-Tactics: The Linked-Battle

Proyek *text-based Tactical RPG* sederhana berbasis Python yang dibangun untuk mengeksplorasi konsep pemrograman berorientasi objek (OOP), manajemen data, dan visualisasi antarmuka terminal (*CLI*).

> **Status Proyek:** 🛠️ Dalam Tahap Pengembangan (*Active Development*)

---

## 🚀 Fitur Utama Game

* **mekanik mengulang putaran yang seru dan taktis** dengan menggunakan teknologi python3 linked list, pemain dapat mengulang dan memilih di putaran manakah dia akan kembali dan memperbaiki rencananya.
* **Sistem Formasi Sinergis:** Karakter memiliki mekanik yang saling memengaruhi satu sama lain (Contoh: Pasif *Ngamuk/Depresi* Mikasa yang bergantung pada kondisi HP Dewa).
* **sistem Cooldown Dinamis:** Pengelolaan giliran kemampuan aktif (*Active Skills*) dan pasif yang diatur secara adil oleh *core game engine*.
* **Antarmuka Terminal Responsif:** Cetak status unit (*HP & Status*) menggunakan kalkulasi spasi manual dan kode warna ANSI agar tampilan tabel tetap simetris.
* **Validasi Input Anti-Crash:** Dilengkapi dengan *custom exception handling* untuk mencegah nama tim kembar, karakter tidak terdaftar, atau input kosong.

---

## 🧠 Konsep & Teknik yang Dipelajari

Melalui proyek ini, saya mendalami beberapa konsep penting dalam pengembangan perangkat lunak:
1. **Virtual Environment (venv):** Isolasi dependensi proyek agar berjalan konsisten di lingkungan mana pun.
2. **Struktur Data:** Penerapan logika *Arrays* dan eksplorasi *Linked List* untuk alur jalannya babak pertempuran.
3. **Prinsip OOP (Inheritance & Polymorphism):** Menggunakan `Dasar_Karakter` sebagai induk, lalu diturunkan ke kelas spesifik seperti `Dewa`, `Bruno`, `Joy`, dan `Mikasa` dengan memanfaatkan `super()`.

---

## 🎮 Struktur Karakter Saat Ini

| Karakter | Tipe/Role | Mekanik Unik |
| :--- | :--- | :--- |
| **Dewa** | Critical DPS | Memberikan serangan kritikal instan setiap beberapa babak. |
| **Bruno** | Tanker | Menggunakan barbel untuk menepis 100% damage monster (*Guard Mode*). |
| **Joy** | Support/Healer | Menyuntikkan HP tambahan ke seluruh rekan tim melewati batas HP maksimal. |
| **Mikasa** | Berserker | Mendapat buff jika bersama Dewa, mengamuk saat Dewa sekarat, dan depresi jika Dewa tumbang. |

---

## 🛠️ Cara Menjalankan

Ikuti langkah-langkah berikut untuk memasang dependensi dan menjalankan game di komputer Anda:

### 1. Clone Repositori
   ~ git clone [https://github.com/username/Chronos-Tactics-The-Linked-Battle.git](https://github.com/username/Chronos-Tactics-The-Linked-Battle.git)
   
   ~cd Chronos-Tactics-The-Linked-Battle

### 2. buat dan aktifkan virtual environment (venv)

   ~ di linux/macOS:
         python3 -m venv venv
         source venv/bin/activate

   ~ Windows (Command Prompt):
         python -m venv venv
         venv\Scripts\activate

   ~ Windows (PowerShell):
         python -m venv venv
         .\venv\Scripts\Activate.ps1

### 3. Instal Dependensi / Library Resmi
      Pastikan virtual environment Anda sudah aktif (ditandai dengan munculnya teks (venv) di ujung kiri terminal), lalu pasang library yang dibutuhkan:

      pip install -r requirements.txt
      

### jalankan game
      Setelah semua library (pynput, evdev, dll.) berhasil terpasang, mainkan game dengan perintah:

      - python main.py

      ⚠️ **Catatan Khusus Pengguna Linux:** Jika mengalami kendala izin akses terkait pembacaan input oleh `evdev`, jalankan script menggunakan perintah `sudo` atau masukkan *user* Anda ke dalam grup `input`.
