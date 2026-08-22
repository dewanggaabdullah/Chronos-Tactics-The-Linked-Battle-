function mulaiGame() {
    fetch('/aksi', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({
            aksi: 'mulai'
        })
    })
    .then(response => response.json())
    .then(data => {
        console.log(data);

        const prolog =
            document.getElementById('prolog');

        const teksProlog =
            document.getElementById('teks-prolog');

        const menuUtama =
            document.getElementById('menu-utama');

        if (!prolog || !teksProlog || !menuUtama) {
            console.error(
                'Elemen HTML tidak ditemukan.'
            );
            return;
        }

        teksProlog.innerHTML = `
            <h2>${data.prolog.judul}</h2>

            ${data.prolog.pembuka
                .map(teks => `<p>${teks}</p>`)
                .join('')}

            <p>${data.prolog.instruksi}</p>

            ${data.prolog.karakter
                .map(karakter => `
                    <div class="karakter">
                        <p>
                            ${karakter.replace(/\n/g, '<br>')}
                        </p>
                    </div>
                `)
                .join('')}
        `;

        menuUtama.classList.add('hidden');
        prolog.classList.remove('hidden');

        tampilkanPesan(
            'Pilih 3 karakter untuk membentuk tim.'
        );
    })
    .catch(error => {
        console.error('Error:', error);
    });
}
