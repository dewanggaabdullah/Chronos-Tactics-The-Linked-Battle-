function bukaMenuPertarungan(battle) {
    document.getElementById('prolog').classList.add('hidden');
    document.getElementById('menu-utama').classList.add('hidden');
    document.getElementById('menu-settings').classList.add('hidden');
    document.getElementById('judul-game').classList.add('hidden');

    document.getElementById('menu-game').classList.remove('hidden');

    document.getElementById('hp-monster').innerText =
        battle.hp_monster;

    tampilkanTim(battle.tim_pemain);
}


function tampilkanTim(tim) {
    const daftarTim =
        document.getElementById('daftar-tim');

    daftarTim.innerHTML = '';

    tim.forEach(namaKarakter => {

        const tombol = document.createElement('button');

        tombol.innerText =
            namaKarakter.charAt(0).toUpperCase()
            + namaKarakter.slice(1);

        tombol.onclick = function() {
            pilihKarakterAktif(namaKarakter);
        };

        daftarTim.appendChild(tombol);
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


function pilihKarakterAktif(namaKarakter) {
    fetch('/aksi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            aksi: 'atur_karakter_turn',
            karakter: namaKarakter
        })
    })
    .then(response => response.json())
    .then(data => {

        console.log(
            "KARAKTER AKTIF:",
            data
        );

        tampilkanPesan(data.log);

        if (!data.berhasil) {
            return;
        }

        document.getElementById(
            'karakter-aktif'
        ).innerText =
            data.karakter.charAt(0).toUpperCase()
            + data.karakter.slice(1);

    })
    .catch(error => {
        console.error("ERROR:", error);
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

        bukaMenuPertarungan(data.battle);
    })
    .catch(error => {
        console.error("ERROR:", error);
    });
}


function kirimAksi(aksi) {
    fetch('/aksi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            aksi: aksi
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log("DATA AKSI:", data);

        tampilkanPesan(data.log);

        if (!data.berhasil) {
            return;
        }

        if (aksi === 'kabur') {
            kembaliKeMenuUtama();
        }
    })
    .catch(error => {
        console.error("ERROR:", error);
    });
}
