from flask import Flask, render_template, request, jsonify
from flow import engine as en

app = Flask(__name__)

@app.route('/')
def index():
    # Inisialisasi awal saat halaman utama dibuka
    en.inisialisasi_game()
    return render_template('index.html')

@app.route('/aksi', methods=['POST'])
def handle_aksi():
    data = request.json
    aksi_user = str(data.get('aksi', '')).lower()
    
    # Proses aksi lewat engine
    hasil_log = en.proses_aksi(aksi_user)
    
    # Ambil data monster dan turn dengan aman
    monster = en.game_state.get("monster")
    hp_monster_val = monster.hp if monster else 0
    
    return jsonify({
        "log": hasil_log,
        "hp_monster": hp_monster_val,
        "turn": en.game_state.get("nomor_turn", 1)
    })

if __name__ == '__main__':
    app.run(debug=True)