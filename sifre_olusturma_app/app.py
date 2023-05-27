from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    length = int(request.form['length'])
    sifre = generate_password(length)
    return render_template('result.html', sifre=sifre)

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    sifre = ''.join(random.choice(characters) for _ in range(length))
    return sifre

if __name__ == '__main__':
    app.run()

