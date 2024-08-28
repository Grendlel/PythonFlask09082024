from flask import Flask, render_template, request, flash
app = Flask(__name__)
from database import db
from flask_migrate import Migrate
from models import Pedidos
app.config['SECRET_KEY'] ='13db70a7b93420a4df3c9688dafcd60bab89a54f00a8902f1b442e92562660de'

# drive://usuario:senha@servidor/banco_de_dados
conexao = "mysql+pymysql://alunos:cefetmg@127.0.0.1/PedidosGab"
app.config['SQLALCHEMY_DATABASE_URI'] = conexao
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)
migrate = Migrate(app, db)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/Deposito')
@app.route('/Deposito/<data_pedido>')
@app.route('/Deposito/<data_pedido>/<valor_total>')
@app.route('/Deposito/<data_pedido>/<valor_total>/<int:status>')
def Deposito(data_pedido = '2000/01/01', valor_total = 0, status = 'offline'):
    dados = {'data pedido':data_pedido,'valor total':valor_total, 'status':status}
    return render_template('aula.html', dados_curso=dados)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dados', methods=['POST'])
def dados():
    flash('dados enviados!!!')
    dados = request.form
    return render_template('dados.html', dados = dados)

@app.route('/Pedidos')
def Pedidos():
    u = Pedidos.query.all()
    return render_template('Pedidos.html', dados = u)


if __name__ == '__main__':
    app.run()