from flask import Flask, render_template, request, jsonify
from translate import Translator
import googletrans
import pandas as pd

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate_sentence', methods=['POST'])
def translate_sentence():
    sentence = request.form['sentence']
    translator = Translator(to_lang='or')
    translated_sentence = translator.translate(sentence)
    return jsonify({"translated_sentence": translated_sentence})

@app.route('/translate_languages')
def translate_languages():
    languages = googletrans.LANGUAGES
    return jsonify(languages)

@app.route('/translate_dataframe')
def translate_dataframe():
    my_data = pd.DataFrame({"EnglishText": ["my name is Amirul", "Good boy", "Data Science Good Future"]})
    translator = Translator(to_lang="ta")
    my_data["TamilText"] = my_data["EnglishText"].apply(lambda x: translator.translate(x))
    return jsonify(my_data.to_dict(orient='records'))

if __name__ == '__main__':
    app.run(debug=True)
