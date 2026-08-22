
function tampilkanPesan(teks) {
    const pesanPemain =
        document.getElementById('pesan-pemain');

    if (!pesanPemain) {
        console.error("Elemen #pesan-pemain tidak ditemukan.");
        return;
    }

    pesanPemain.innerText = teks;
}