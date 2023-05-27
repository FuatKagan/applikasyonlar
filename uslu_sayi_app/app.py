from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/power', methods=['POST'])
def power():
    taban = int(request.form['taban'])
    us = int(request.form['us'])
    sonuc = taban ** us
    return render_template('result.html', taban=taban, us=us, sonuc=sonuc)

if __name__ == '__main__':
    app.run()
