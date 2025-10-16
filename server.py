from flask import Flask, request, jsonify
from open_tamil import utf8

app = Flask(__name__)

@app.route('/')
def home():
    return "Tamil Server is Running!"

@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.get_json()
    text = data.get("text", "")
    tscii = utf8.get_letters(text)
    return jsonify({"letters": tscii})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
