function bukaMenuPertarungan(data.battle) {
    document.getElementById('prolog').classList.add('hidden');
    document.getElementById('menu-utama').classList.add('hidden');
    document.getElementById('menu-settings').classList.add('hidden');
    document.getElementById('judul-game').classList.add('hidden');

    document.getElementById('menu-game').classList.remove('hidden');

    document.getElementById('hp-monster').innerText =
        battle.hp_monster;

    tampilkanTim(battle.tim_pemain);
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
        console.log("DATA DARI SERVER:", data);

        tampilkanPesan(data.log);

        if (!data.berhasil) {
            console.log("Battle tidak dibuka:", data.log);
            return;
        }

        console.log("Battle dibuka!");

        bukaMenuPertarungan();
    })
    .catch(error => {
        console.error("ERROR:", error);
    });
}