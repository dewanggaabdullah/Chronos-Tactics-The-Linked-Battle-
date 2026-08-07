from flask import Flask, render_template, request, jsonify
from flow import engine as en

app = Flask(__name__)

@app.route('/')
def index():
    en.inisialisasi_game()
    return render_template('index.html')


@app.route('/aksi', methods=['POST'])
def handle_aksi():
    data = request.json
    aksi_user = data.get('aksi', '').lower()
    
    hasil_log = en.proses_aksi(aksi_user)
    
    return jsonify({
        "log": hasil_log,
        "hp_monster": en.game_state["monster"].hp if en.game_state["monster"] else 0,
        "turn": en.game_state["nomor_turn"]
    })

if __name__ == '__main__':
    app.run(debug=True)