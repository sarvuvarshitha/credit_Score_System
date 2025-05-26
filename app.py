from flask import Flask, request, jsonify
from flask_cors import CORS
from feistel_cipher import feistel_encrypt, feistel_decrypt

app = Flask(__name__)
CORS(app)

def compute_score(income, debts, history):
    base_score = 300 + (int(income) - int(debts)) // 10 + int(history) * 20
    return min(max(base_score, 300), 850)

@app.route('/score', methods=['POST'])
def calculate_score():
    data = request.json
    key = "k3y12345"

    enc_income = feistel_encrypt(data['income'], key)
    enc_debts = feistel_encrypt(data['debts'], key)
    enc_history = feistel_encrypt(data['history'], key)

    income = feistel_decrypt(enc_income, key).strip()
    debts = feistel_decrypt(enc_debts, key).strip()
    history = feistel_decrypt(enc_history, key).strip()

    score = compute_score(income, debts, history)
    return jsonify({
        'credit_score': score,
        'encrypted': {
            'income': enc_income,
            'debts': enc_debts,
            'history': enc_history
        }
    })

if __name__ == '__main__':
    app.run(debug=True)
