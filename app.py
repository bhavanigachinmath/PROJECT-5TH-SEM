from flask import Flask, render_template, request
import emoji
import nltk
from nltk.tokenize import word_tokenize

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    output = ""

    if request.method == "POST":
        emoji_input = request.form.get("emoji")

        if emoji_input:
            # Convert emoji to text
            demojized = emoji.demojize(emoji_input)

            # Clean text
            clean_text = demojized.replace(":", "").replace("_", " ")

            # NLP using NLTK
            tokens = word_tokenize(clean_text)

            # Join tokens
            output = " ".join(tokens)

    return render_template("index.html", result=output)

if __name__ == "__main__":
    app.run(debug=True)
