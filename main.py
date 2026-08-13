from flask import Flask, render_template, request, jsonify

from menu import main_menu
from menu import game_menu
from menu import settings_menu


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aksi', methods=['POST'])
def handle_aksi():
    data = request.json
    aksi_user = str(data.get('aksi', '')).lower()

    if aksi_user == 'mulai':
        return jsonify(
            main_menu.mulai_game()
        )

    if aksi_user in ('elsa', 'bruno', 'kabur'):
        return jsonify(
            game_menu.proses_aksi(aksi_user)
        )

    if aksi_user in ('audio', 'grafis'):
        return jsonify(
            settings_menu.proses_aksi(aksi_user)
        )

    return jsonify({
        "error": "Aksi tidak dikenal"
    }), 400


if __name__ == '__main__':
    app.run(debug=True)