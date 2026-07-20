from flask import Flask, render_template, request, jsonify
from flow import engine as en

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/jalankan_game', methods=['POST'])
def jalankan_game():
    pilihan = request.form.get('menu_option')
    
    if pilihan == '1':
        en.inisialisasi_karakter()
        return jsonify({"status": "Game Dimulai", "message": "Fungsi inisialisasi karakter telah berjalan."})
    
    elif pilihan == '2':
        return jsonify({"status": "Settings", "message": "Fitur settings akan datang segera."})
    
    return jsonify({"status": "Error", "message": "Pilihan tidak valid"})

if __name__ == '__main__':
    app.run(debug=True)