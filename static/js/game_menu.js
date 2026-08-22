function bukaGameMenu() {
    document.getElementById('prolog').classList.add('hidden');
    document.getElementById('menu-game').classList.remove('hidden');
}


function pilihkarakter(namaKarakter) {
    fetch('/aksi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            aksi: 'pilih_karakter',
            karakter: namaKarakter
        })
    })
    .then(response => response.json())
    .then(data => {

        tampilkanPesan(data.log);

        const tombol = document.querySelector(
            `[data-karakter="${namaKarakter}"]`
        );

        if (!tombol) {
            return;
        }

        if (data.berhasil && data.dipilih) {
            tombol.classList.add('karakter-dipilih');
        }

        if (data.berhasil && !data.dipilih) {
            tombol.classList.remove('karakter-dipilih');
        }

    })
    .catch(error => {
        console.error("Error:", error);
    });
}


function siapBertarung() {
    fetch('/aksi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            aksi: 'siap'
        })
    })
    .then(response => response.json())
    .then(data => {
        tampilkanPesan(data.log);
    })
    .catch(error => {
        console.error("Error:", error);
    });
}