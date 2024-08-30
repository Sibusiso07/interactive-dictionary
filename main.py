from flask import Flask, render_template, request
import requests

app = Flask(__name__)


# Home route
@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        word = request.form['word']
        response = requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{word}')

        if response.status_code == 200:
            data = response.json()[0]  # Extract the first result
            return render_template('index.html', word=word, data=data)
        else:
            error = "Word not found! Please try another word."
            return render_template('index.html', error=error)

    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
