from flask import Flask, request, make_response,redirect,render_template, session
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap=Bootstrap(app)
app.config['SECRET_KEY']='Super Secreto'



todos=['TODO 1','TODO 2', 'TODO 3']

@app.route('/')
def index():
    user_ip=request.remote_addr# provides the user ip
    response = make_response(redirect('/hello'))
    session['user_ip']=user_ip
    return response

@app.route('/hello')
def hello():
    user_ip=request.cookies.get('user_ip')
    context={'user_ip':user_ip,
             'todos':todos
             }
    return render_template('hello.html',**context)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

