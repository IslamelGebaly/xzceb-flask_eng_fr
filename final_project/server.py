from flask import Flask, render_template, request
from machinetranslation import translator
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    french_text = translator.englishToFrench(textToTranslate)[0]
    return french_text

@app.route("/frenchToEnglish")
def frenchToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    english_text = translator.frenchToEnglish(textToTranslate)[0]
    return english_text

@app.route("/")
def renderIndexPage():
    # Write the code to render template
    return render_template(r"index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
