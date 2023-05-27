from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/calculate', methods=['POST'])
def calculate():
    sayi1 = int(request.form['sayi1'])
    sayi2 = int(request.form['sayi2'])
    islem = request.form['islem']
    
    if islem == '+':
        sonuc = sayi1 + sayi2
    elif islem == '-':
        sonuc = sayi1 - sayi2
    elif islem == '/':
        sonuc = sayi1 / sayi2
    elif islem == '*':
        sonuc = sayi1 * sayi2
    else:
        sonuc = None
    
    return render_template('result.html', sayi1=sayi1, sayi2=sayi2, islem=islem, sonuc=sonuc)

if __name__ == '__main__':
    app.run()