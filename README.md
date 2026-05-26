# ⚔️ Chronos-Tactics: The Linked-Battle

Proyek *text-based Tactical RPG* sederhana berbasis Python yang dibangun untuk mengeksplorasi konsep pemrograman berorientasi objek (OOP), manajemen data, dan visualisasi antarmuka terminal (*CLI*).

> **Status Proyek:** 🛠️ Dalam Tahap Pengembangan (*Active Development*)

---

## 🚀 Fitur Utama Game

* **Mekanik Mengulang Putaran yang Taktis:** Menggunakan implementasi struktur data *Linked List*, pemain dapat memutar balik waktu, memilih di babak (*turn*) manakah dia akan kembali, dan memperbaiki strategi pertempurannya.
* **Sistem Formasi Sinergis:** Karakter memiliki mekanik pasif yang saling memengaruhi satu sama lain (Contoh: Pasif *Ngamuk/Depresi* Mikasa yang bergantung pada kondisi HP Dewa).
* **Sistem Cooldown Dinamis:** Pengelolaan giliran kemampuan aktif (*Active Skills*) dan pasif yang diatur secara adil oleh *core game engine*.
* **Antarmuka Terminal Responsif:** Cetak status unit (*HP & Status*) menggunakan kalkulasi spasi manual dan kode warna ANSI agar tampilan tabel tetap simetris di terminal.
* **Validasi Input Anti-Crash:** Dilengkapi dengan *custom exception handling* untuk mencegah nama tim kembar, karakter tidak terdaftar, atau input kosong yang dapat merusak jalannya game.

---

## 🧰 Teknologi & Library yang Digunakan

Proyek ini dibangun murni menggunakan ekosistem **Python 3** dengan memanfaatkan beberapa library pihak ketiga untuk menangani interaksi *hardware stream*:

* **Python 3.11+** - Bahasa pemrograman utama untuk seluruh logika backend dan game engine.
* **pynput** - Digunakan untuk mendengarkan (*listen*) input keyboard secara *real-time* (seperti mendeteksi tombol Spasi untuk melewati dialog cerita).
* **evdev** - Digunakan sebagai interaksi tingkat rendah (*low-level*) dengan input device pada sistem Linux/Docker agar pembacaan tombol menjadi lebih responsif dan *headless-friendly*.

---

## 🧠 Konsep & Teknik Backend yang Dipelajari

Melalui proyek ini, saya mendalami beberapa konsep penting dalam pengembangan perangkat lunak dan DevOps:
1. **Virtual Environment (venv):** Isolasi dependensi proyek agar berjalan konsisten di lingkungan pengembangan lokal.
2. **Struktur Data Lanjutan:** Eksplorasi *Linked List* untuk mencatat riwayat setiap babak (*state per turn*) demi mendukung mekanik pembalikan waktu.
3. **Prinsip OOP (Inheritance & Polymorphism):** Menggunakan `Dasar_Karakter` sebagai kelas induk (*parent*), lalu diturunkan ke kelas spesifik seperti `Dewa`, `Bruno`, `Joy`, dan `Mikasa` dengan memanfaatkan fungsi `super()`.
4. **Kontainerisasi (Docker):** Membungkus seluruh aplikasi ke dalam Docker Image agar game dapat dimainkan di sistem operasi mana pun tanpa perlu melakukan instalasi Python atau library secara manual di komputer *host*.

---

## 🎮 Struktur Karakter Saat Ini

| Karakter | Tipe/Role | Mekanik Unik |
| **elsa** | pasif healer | punya kemampuan memberikan heal pada tim tiap ronde. |
| **Dewa** | Critical DPS | Memberikan serangan kritikal instan setiap beberapa babak. |
| **Bruno** | Tanker | Menggunakan barbel untuk menepis 100% damage monster (*Guard Mode*). |
| **Joy** | Support/Healer | Menyuntikkan HP tambahan ke seluruh rekan tim melewati batas HP maksimal. |
| **Mikasa** | Berserker | Mendapat buff jika bersama Dewa, mengamuk saat Dewa sekarat, dan depresi jika Dewa tumbang. |

---

## 🛠️ Cara Menjalankan (Bagi Pengguna/Pemain)

Anda bisa memilih salah satu dari dua cara di bawah ini untuk memainkan game:

### Opsi A: Menggunakan Docker (Sangat Direkomendasikan & Instan)

## clone repositori dan masuk ke folder proyek:
git clone [https://github.com/username/Chronos-Tactics-The-Linked-Battle.git](https://github.com/username/Chronos-Tactics-The-Linked-Battle.git)
cd Chronos-Tactics-The-Linked-Battle

## berikan izin eksekusi pada file script (.sh):
chmod +x edit-game-chronos.sh jalankan-game-cronos.sh

## Rakit Kontainer Game Anda (Hanya untuk Pertama Kali):
./edit-game-chronos.sh

## Mainkan Game Langsung dari Kontainer:
./jalankan-game-cronos.sh

### Opsi B: Menggunakan Environment Python Lokal
Jika Anda ingin menjalankannya secara manual tanpa Docker, ikuti langkah berikut:

## Clone Repositori:

git clone [https://github.com/username/Chronos-Tactics-The-Linked-Battle.git](https://github.com/username/Chronos-Tactics-The-Linked-Battle.git)
cd Chronos-Tactics-The-Linked-Battle

## Buat dan Aktifkan Virtual Environment (venv):

# Linux/macOS:

Bash
python3 -m venv venv
source venv/bin/activate

# Windows (Command Prompt):

DOS
python -m venv venv
venv\Scripts\activate

# Windows (PowerShell):

PowerShell
python -m venv venv
.\venv\Scripts\Activate.ps1

## Instal Dependensi:

Bash
pip install -r requirements.txt

## Jalankan Game:

Bash
python main.py

## ⚠️ Catatan Khusus Pengguna Linux (Non-Docker): Jika mengalami kendala izin akses terkait pembacaan input oleh evdev, jalankan script menggunakan perintah sudo atau masukkan user Anda ke dalam grup input.