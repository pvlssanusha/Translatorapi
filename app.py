from flask import Flask, request, jsonify
from googletrans import Translator

app = Flask(__name__)

@app.route('/', methods=['POST'])
def translate_text():
    try:
        source_lang = request.get_json().get('source_lang')
        target_lang = request.get_json().get('target_lang')
        source_text = request.get_json().get('source_text')
        
        # Perform translation using googletrans
        translator = Translator()
        
        translated_text = translator.translate(source_text, dest=target_lang).text
        result = {
            'original_text': source_text,
            'translated_text': translated_text,
            'target_language':target_lang
        }

        return jsonify(result), 200

    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
