from flask import request, make_response, redirect, render_template, session, url_for, flash
import unittest

from app import create_app
from app.forms import LoginForm


app =create_app()   


todos = ['TODO 1', 'TODO 2', 'TODO 3']




@app.cli.command('test')
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)


@app.route('/')
def index():
    user_ip = request.remote_addr  # provides the user ip
    response = make_response(redirect('/hello'))
    session['user_ip'] = user_ip
    return response


@app.route('/hello', methods=['GET', 'POST'])
def hello():
    # user_ip=request.cookies.get('user_ip')
    user_ip = session.get('user_ip')
    username = session.get('username')
    login_form = LoginForm()
    context = {'user_ip': user_ip,
               'todos': todos,
               'login_form': login_form,
               'username': username
               }
    if login_form.validate_on_submit():
        username = login_form.username.data
        session['username'] = username
        flash('Nombre de usuario registrado con éxito')
        return redirect(url_for('hello'))

    return render_template('hello.html', **context)


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)
