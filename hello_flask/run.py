from flask import Flask
app = Flask(__name__)

@app.route('/<numero>', methods= ['GET', 'POST'])
def hello(numero):
    return 'Hello World!!! {}'.format(numero)

if __name__ == '__main__':
    app.run(debug=True)
