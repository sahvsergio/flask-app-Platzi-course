from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired
import unittest


app = Flask(__name__)
bootstrap = Bootstrap(app)
app.config['SECRET_KEY'] = 'Super Secreto'


todos = ['TODO 1', 'TODO 2', 'TODO 3']


class LoginForm(FlaskForm):
    username = StringField('Nombre de usuario', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Enviar')


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
