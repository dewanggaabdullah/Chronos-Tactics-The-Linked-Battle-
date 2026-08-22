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
