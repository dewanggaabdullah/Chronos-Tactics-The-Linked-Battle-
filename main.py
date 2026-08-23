from flask import Flask, render_template, request, jsonify
from flow import engine as en

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/aksi', methods=['POST'])
def handle_aksi():
    data = request.json or {}

    aksi_user = str(
        data.get('aksi', '')
    ).lower()

    return jsonify(
        en.proses_aksi(
            aksi_user,
            data
        )
    )


if __name__ == '__main__':
    app.run(debug=True)
