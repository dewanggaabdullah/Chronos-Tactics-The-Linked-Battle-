function bukaGameMenu() {
    document.getElementById('prolog').classList.add('hidden');
    document.getElementById('menu-game').classList.remove('hidden');
}


function tampilkanMenuKarakter(tim) {
    const aksiKarakter = document.getElementById('aksi-karakter');

    aksiKarakter.innerHTML = '';

    tim.forEach(nama => {
        const button = document.createElement('button');

        button.innerText = `Serang dengan ${nama}`;

        button.onclick = function () {
            kirimAksi(nama);
        };

        aksiKarakter.appendChild(button);
    });
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
        console.log(data);

        const pesanPemain =
            document.getElementById('pesan-pemain');

        if (pesanPemain) {
            pesanPemain.innerText = data.log;
        }
    })
    .catch(error => {
        console.error('Error:', error);
    });
}