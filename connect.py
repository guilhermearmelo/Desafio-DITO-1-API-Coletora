from flask import Flask, render_template, request
from flask_pymongo import PyMongo

app = Flask(__name__)

# Definição de conexões com o banco de dados
app.config['MONGO_DBNAME'] = 'desafioditoconnect'
app.config['MONGO_URI'] = 'mongodb://guilhermemelo:guidll2@ds029187.mlab.com:29187/desafioditoconnect'

mongo = PyMongo(app)

# Definição da página inicial
@app.route('/')
def index():
    return render_template('index.html')

# CREATE
@app.route('/add', methods=['POST'])
def adicionar():
    event = request.form['novoevent']
    timestamp = request.form['novotimestamp']
    dado = mongo.db.dados
    dado.insert({'event': event, 'timestamp': timestamp})
    return render_template('add.html', novoevento=event)

# READ
@app.route('/find')
def find():
    dado = mongo.db.dados
    x = dado.find_one({'event': 'Evento1'})
    return 'Evento Encontrado!'

# UPDATE
@app.route('/update')
def update():
    dado = mongo.db.dados
    x = dado.find_one({'event': 'Evento1'})
    x['timestamp'] = '1000'
    dado.save(x)
    return 'Evento Atualizado!'

# DELETE
@app.route('/delete')
def delete():
    dado = mongo.db.users
    x = dado.find_one({'event': 'Evento3'})
    dado.remove(x)
    return 'Evento Removido!'

if __name__ == '__main__':
    app.run(debug=True)
