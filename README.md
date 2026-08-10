# ⚔️ Chronos-Tactics: The Linked-Battle

**Chronos-Tactics: The Linked-Battle** adalah *text-based Tactical RPG* berbasis Python yang dikembangkan sebagai game web dengan **Flask**.

Proyek ini menggabungkan konsep **Object-Oriented Programming (OOP)**, struktur data, state management, dan web application untuk membangun sistem pertempuran berbasis giliran yang memiliki mekanik *time rewind*.

Mekanik utama permainan menggunakan **Linked List** untuk menyimpan riwayat *state* pada setiap giliran. Dengan demikian, pemain dapat kembali ke kondisi permainan sebelumnya dan mengambil keputusan yang berbeda untuk mengubah jalannya pertempuran.

> **Status Proyek:** 🛠️ Active Development

---

## 🚀 Fitur Utama

### ⏳ Tactical Time Rewind

Setiap giliran pertempuran menghasilkan sebuah *game state* yang disimpan sebagai bagian dari riwayat pertempuran menggunakan struktur data **Linked List**.

Pemain dapat memilih untuk kembali ke giliran sebelumnya dan melanjutkan pertempuran dari kondisi tersebut.

Mekanik ini menjadi salah satu fitur utama yang membedakan Chronos-Tactics dari sistem turn-based RPG biasa.

### 🤝 Character Synergy

Setiap karakter memiliki kemampuan dan mekanik pasif yang dapat berinteraksi dengan karakter lain.

Contohnya, kemampuan **Mikasa** dipengaruhi oleh kondisi **Dewa**:

* Mendapatkan buff ketika berada dalam formasi bersama Dewa.
* Memasuki kondisi *rage* ketika HP Dewa berada dalam kondisi kritis.
* Mengalami kondisi *depression* ketika Dewa tumbang.

Dengan demikian, pemilihan formasi tidak hanya menentukan statistik tim, tetapi juga memengaruhi mekanik karakter selama pertempuran.

### ⏱️ Dynamic Cooldown System

Kemampuan aktif dan pasif memiliki aturan *cooldown* yang dikelola oleh *game engine*.

Setiap kemampuan hanya dapat digunakan ketika kondisi dan *cooldown*-nya terpenuhi, sehingga pemain harus mempertimbangkan timing ketika menggunakan kemampuan.

### 🌐 Web-Based Game Interface

Game yang sebelumnya berorientasi pada terminal dikembangkan menjadi **web-based game** menggunakan Flask.

Flask bertindak sebagai penghubung antara game engine Python dan antarmuka web, sehingga pemain dapat berinteraksi dengan permainan melalui browser tanpa harus menjalankan game secara langsung melalui terminal.

### ⌨️ Real-Time Keyboard Input

Game menggunakan library input untuk menangani interaksi keyboard tertentu secara *real-time*, seperti tombol yang digunakan untuk melewati dialog atau melakukan interaksi tertentu selama permainan.

### 🛡️ Input Validation & Exception Handling

Game memiliki validasi input dan *custom exception handling* untuk menangani kondisi yang tidak valid, seperti:

* Nama tim yang duplikat.
* Karakter yang tidak terdaftar.
* Input kosong.
* Kondisi permainan yang tidak memenuhi aturan.

Tujuannya adalah memastikan kesalahan input tidak menyebabkan game berhenti secara tiba-tiba.

---

## 🧰 Teknologi & Library

| Teknologi               | Penggunaan                                                                            |
| ----------------------- | ------------------------------------------------------------------------------------- |
| **Python 3.11+**        | Bahasa utama untuk game engine, game logic, OOP, dan state management.                |
| **Flask**               | Framework web yang digunakan untuk menyediakan interface game melalui browser.        |
| **pynput**              | Menangani input keyboard secara *real-time* untuk interaksi tertentu dalam permainan. |
| **evdev**               | Digunakan untuk berinteraksi dengan Linux input devices pada level rendah.            |
| **HTML/CSS/JavaScript** | Membentuk antarmuka web dan interaksi pemain dengan game.                             |

---

## 🧠 Konsep Software Engineering yang Dipelajari

Chronos-Tactics digunakan sebagai proyek untuk mempraktikkan berbagai konsep fundamental dalam pengembangan software.

### 1. Object-Oriented Programming

Game menggunakan prinsip OOP untuk memodelkan karakter dan perilaku mereka.

`Dasar_Karakter` digunakan sebagai class dasar yang kemudian diturunkan menjadi karakter seperti:

* `Dewa`
* `Bruno`
* `Joy`
* `Mikasa`
* `Elsa`

Konsep yang digunakan meliputi:

* Class dan object.
* Inheritance.
* Polymorphism.
* Method overriding.
* Encapsulation.
* `super()`.

Pendekatan ini memungkinkan setiap karakter memiliki perilaku dan kemampuan yang berbeda tanpa harus menempatkan seluruh logic dalam satu class.

### 2. Data Structure: Linked List

**Linked List** digunakan untuk menyimpan riwayat *game state* pada setiap giliran.

Setiap node merepresentasikan kondisi permainan pada suatu titik dalam pertempuran.

Struktur tersebut memungkinkan implementasi mekanik **time rewind**, karena game dapat berpindah kembali ke state sebelumnya dan melanjutkan permainan dari titik tersebut.

### 3. State Management

Pertempuran terdiri dari berbagai *state* yang berubah berdasarkan aksi pemain, damage, kemampuan karakter, cooldown, dan kondisi lainnya.

Game engine bertanggung jawab untuk menjaga agar perubahan state tetap mengikuti aturan permainan.

### 4. Exception Handling

*Exception handling* digunakan untuk menangani kondisi yang tidak valid tanpa menyebabkan seluruh aplikasi berhenti.

Proyek juga menggunakan *custom exceptions* untuk merepresentasikan kesalahan yang berkaitan secara langsung dengan aturan game.

### 5. Web Application Architecture

Dengan migrasi dari terminal menuju web, game dipisahkan menjadi beberapa bagian utama:

```text
Browser
   │
   ▼
Flask Web Application
   │
   ▼
Game Engine
   │
   ├── Character System
   ├── Battle System
   ├── Cooldown System
   └── Game State / Linked List
```

Flask berfungsi sebagai lapisan yang menerima interaksi dari browser dan meneruskannya ke game engine.

Game engine tetap bertanggung jawab terhadap aturan dan state permainan sehingga logic utama tidak bergantung langsung pada tampilan web.

---

## 🎮 Struktur Karakter Saat Ini

| Karakter   | Role             | Mekanik Unik                                                                                                                       |
| ---------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| **Elsa**   | Passive Healer   | Memberikan efek heal kepada tim setiap ronde.                                                                                      |
| **Dewa**   | Critical DPS     | Dapat memberikan serangan kritikal secara berkala berdasarkan sistem cooldown.                                                     |
| **Bruno**  | Tank             | Menggunakan *Guard Mode* untuk menepis damage monster.                                                                             |
| **Joy**    | Support / Healer | Memberikan tambahan HP kepada anggota tim, termasuk HP yang dapat melewati batas maksimum normal.                                  |
| **Mikasa** | Assasin        | Mendapatkan buff ketika bersama Dewa, memasuki kondisi *rage* ketika Dewa sekarat, dan mengalami *depression* ketika Dewa tumbang. |

---

## 🛠️ Cara Menjalankan

### 1. Clone Repository

```bash
git clone https://github.com/dewanggaabdullah/Chronos-Tactics-The-Linked-Battle-.git
cd Chronos-Tactics-The-Linked-Battle-
```

### 2. Buat Virtual Environment

**Linux/macOS:**

```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows Command Prompt:**

```cmd
python -m venv venv
venv\Scripts\activate
```

**Windows PowerShell:**

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

Setelah virtual environment aktif:

```bash
pip install -r requirements.txt
```

### 4. Jalankan Web Application

```bash
python main.py
```

Setelah Flask berhasil dijalankan, server akan tersedia pada alamat lokal yang ditampilkan di terminal.

Secara default, Flask biasanya menggunakan:

```text
http://127.0.0.1:5000
```

Buka alamat tersebut menggunakan browser untuk mulai memainkan game setelah proyek sudah lancar dan stabil buat dimainkan.

---

## ⚠️ Catatan

Karena game masih dalam tahap pengembangan, struktur aplikasi, sistem pertempuran, karakter, dan antarmuka web dapat mengalami perubahan.

Beberapa komponen seperti sistem input keyboard juga memiliki ketergantungan terhadap environment sistem operasi. Khususnya pada Linux, `evdev` berinteraksi langsung dengan perangkat input sehingga permission perangkat dapat memengaruhi kemampuan aplikasi untuk membaca input.

---

## 📌 Roadmap

Pengembangan Chronos-Tactics berfokus pada transisi dari game berbasis terminal menjadi **web-based Tactical RPG**.

Beberapa area yang sedang dikembangkan meliputi:

* [x] Core game engine
* [x] Character system
* [ ] Turn-based battle system
* [x] Cooldown system
* [x] Linked List untuk game state
* [ ] Web interface
* [ ] Integrasi game engine dengan Flask
* [ ] Interactive battle UI
* [ ] Improved visual presentation
* [ ] Persistent game state
* [ ] Deployment ke public web server
* [ ] playable

---

## 🎯 Tujuan Proyek

Chronos-Tactics bukan hanya dibuat sebagai game, tetapi juga sebagai sarana untuk mempraktikkan bagaimana sebuah **game engine Python dapat dihubungkan dengan aplikasi web**.

Melalui proyek ini, berbagai konsep software engineering diterapkan secara langsung dalam satu sistem, mulai dari OOP dan struktur data hingga state management, exception handling, dan web application development.
