from flask import Flask, render_template, request, flash
app = Flask(__name__)
app.config['SECRET_KEY'] ='13db70a7b93420a4df3c9688dafcd60bab89a54f00a8902f1b442e92562660de'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/aula')
@app.route('/aula/<nome>')
@app.route('/aula/<nome>/<curso>')
@app.route('/aula/<nome>/<curso>/<int:ano>')
def aula(nome = 'Gabriel', curso = 'Informática', ano = 1):
    dados = {'nome':nome,'curso':curso, 'ano':ano}
    return render_template('aula.html', dados_curso=dados)

@app.route('/form')
def form():
    return render_template('form.html')

@app.route('/dados', methods=['POST'])
def dados():
    flash('dados enviados!!!')
    dados = request.form
    return render_template('dados.html', dados = dados)

if __name__ == '__main__':
    app.run()