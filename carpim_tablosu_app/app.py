from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return '''
    <h1>Çarpım Tablosu</h1>
    <form action="/result" method="GET">
        <label for="sayi">Bir sayı girin (1-10 arası):</label>
        <input type="number" id="sayi" name="sayi" min="1" max="10" required>
        <input type="submit" value="Gönder">
    </form>
    '''

@app.route('/result')
def result():
    sayi = int(request.args.get('sayi'))
    results = []
    for num in range(1, 10):
        results.append(f'{sayi} x {num} = {sayi * num}')
    return '<br>'.join(results)

if __name__ == '__main__':
    app.run()