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