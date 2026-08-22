from flask import Flask, render_template, request, jsonify

from menu import main_menu
from menu import game_menu
from menu import settings_menu

from flow import engine as en
from flow import characters as ch


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aksi', methods=['POST'])
def handle_aksi():
    data = request.json
    aksi_user = str(data.get('aksi', '')).lower()

    # =========================
    # MENU UTAMA
    # =========================

    if aksi_user == 'mulai':
        return jsonify(
            main_menu.mulai_game()
        )


    # =========================
    # SETUP PERTARUNGAN
    # =========================

    if aksi_user == 'pilih_karakter':
        nama_karakter = str(
            data.get('karakter', '')
        ).lower()

        return jsonify(
            en.pilih_karakter(nama_karakter)
        )


    if aksi_user == 'tambah_anggota':
        nama_karakter = str(
            data.get('karakter', '')
        ).lower()

        hasil = ch.tambah_karakter_ke_tim(
            nama_karakter,
            en.game_state["tim_pemain"]
        )

        return jsonify(hasil)


    if aksi_user == 'siap':
        return jsonify(
            en.siap_bertarung()
        )


    # =========================
    # TURN KARAKTER
    # =========================

    if aksi_user == 'atur_karakter_turn':
        nama_karakter = str(
            data.get('karakter', '')
        ).lower()

        hasil = ch.atur_karakter_turn(
            nama_karakter,
            en.game_state
        )

        return jsonify(hasil)


    # =========================
    # AKSI PERTARUNGAN
    # =========================

    if aksi_user == 'serang':
        nama_karakter = str(
            data.get('karakter', '')
        ).lower()

        return jsonify(
            game_menu.proses_aksi(
                aksi_user,
                nama_karakter
            )
        )


    if aksi_user == 'skill':
        nama_karakter = str(
            data.get('karakter', '')
        ).lower()

        nama_skill = str(
            data.get('skill', '')
        ).lower()

        return jsonify(
            game_menu.proses_aksi(
                aksi_user,
                nama_karakter,
                nama_skill
            )
        )


    if aksi_user == 'kabur':
        return jsonify(
            game_menu.proses_aksi(
                aksi_user
            )
        )


    # =========================
    # PILIHAN KARAKTER / AKSI KHUSUS
    # =========================

    if aksi_user in ('elsa', 'bruno'):
        return jsonify(
            game_menu.proses_aksi(
                aksi_user
            )
        )


    # =========================
    # SETTINGS
    # =========================

    if aksi_user in ('audio', 'grafis'):
        return jsonify(
            settings_menu.proses_aksi(
                aksi_user
            )
        )


    # =========================
    # AKSI TIDAK DIKENAL/ERROR HANDLING
    # =========================

    return jsonify({
        "error": "Aksi tidak dikenal"
    }), 400


if __name__ == '__main__':
    app.run(debug=True)