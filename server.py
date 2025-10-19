from flask import Flask, request, jsonify
from tamil.txt2unicode import auto2unicode

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, World!"

@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.get_json()
    tscii_text = data.get("text", "")
    unicode_text = auto2unicode(tscii_text)
    return jsonify({"unicode_text": unicode_text})
@app.route('/to_tscii', methods=['POST'])
def to_tscii():
    if unicode_to_tscii is None:
        return jsonify({
            "error": "unicode->TSCII converter not available in installed 'tamil' package.",
            "fix": "Install a tamil package/version that provides 'unicode2tscii' (or add your own converter)."
        }), 501
    data = request.get_json()
    unicode_text = data.get("text", "")
    tscii_text = unicode_to_tscii(unicode_text)
    return jsonify({"tscii_text": tscii_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
