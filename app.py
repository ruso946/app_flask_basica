from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/hola/<nombre>')
def hola_nombre(nombre):
   return 'Hola %s!' % nombre

if __name__ == '__main__':
   app.run()