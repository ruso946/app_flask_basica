from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/hola/')
def hola_mundo():
   return 'Hola Mundo'

if __name__ == '__main__':
   app.run()