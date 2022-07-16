from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/hola/<nombre>')
def hola_nombre():
   return 'Hola %s!' % nombre

if __name__ == '__main__':
   app.run()