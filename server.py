from flask import Flask, request, jsonify
from tamil.txt2unicode import auto2unicode

app = Flask(__name__)

@app.route('/')
def home():
    # Example TSCII string
    tscii_text = "இங்கே இரவு வெகுநேரம் ஆச்சு."  # If this is Unicode already, no need to convert
    # You should test with actual TSCII text like: "§Áø ÀÌ¾¢¨Â ºÚì¸¢ §Á¨ºÂ¢ø ¨Åì¸×õ."
    unicode_text = auto2unicode(tscii_text)
    return unicode_text

@app.route('/convert', methods=['POST'])
def convert_text():
    data = request.get_json()
    tscii_text = data.get("text", "")
    unicode_text = auto2unicode(tscii_text)
    return jsonify({"unicode_text": unicode_text})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
