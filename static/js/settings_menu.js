function bukaSettings() {
    document.getElementById('menu-utama').classList.add('hidden');
    document.getElementById('menu-settings').classList.remove('hidden');

    tampilkanPesan("Silakan pilih pengaturan.");
}


function pilihSubSettings(namaFitur) {
    tampilkanPesan(
        `Pengaturan ${namaFitur} masih dalam tahap pengembangan.`
    );
}


function kembaliKeMenuUtama() {
    // Sembunyikan Settings
    document.getElementById('menu-settings').classList.add('hidden');

    // Sembunyikan menu game
    document.getElementById('menu-game').classList.add('hidden');

    // Sembunyikan prolog
    document.getElementById('prolog').classList.add('hidden');

    // Tampilkan menu utama
    document.getElementById('menu-utama').classList.remove('hidden');

    // Bersihkan pesan
    tampilkanPesan("");
}
