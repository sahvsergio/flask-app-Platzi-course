from flask import Flask, request


app = Flask(__name__)


@app.route('/')
def hello():
    user_ip=request.remote_addr# provides the user ip
    
    return 'Hello World Colombia your ip is {}'.format(user_ip)
