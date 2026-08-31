function kembaliKeMenuUtama() {
    // Sembunyikan semua menu
    document.getElementById('menu-settings').classList.add('hidden');
    document.getElementById('menu-game').classList.add('hidden');
    document.getElementById('prolog').classList.add('hidden');

    // Tampilkan kembali judul game
    document.getElementById('judul-game').classList.remove('hidden');

    // Tampilkan menu utama
    document.getElementById('menu-utama').classList.remove('hidden');

    // Bersihkan pesan
    tampilkanPesan("");
}


function tampilkanPesan(teks) {
    const pesanPemain =
        document.getElementById('pesan-pemain');

    if (!pesanPemain) {
        console.error(
            "Elemen #pesan-pemain tidak ditemukan."
        );
        return;
    }

    pesanPemain.innerText = teks;
}
