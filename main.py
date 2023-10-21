from flask import Flask

app=Flask(__name__)
#FLASK_APP: this is the variable meant to identify  the file where the application is located
# in the terminal just write export FLASK_APP=main.py on linux, set FLASK_APP=main.py on Windows and on powershell $env:FLASK_APP = ‘main.py’ 
#to check, just run echo $FLASK_APP, it should return main.py
#type "flask run"

#para los que trabajan con anaconda:

#--> Para crearlo

#conda create -n NombreEntorno python=3.9

#Eligen la versión de python que deseen.

#--> Para activarlo

#conda activate NombreEntorno

#--> Para desactivarlo:

#conda deactivate
#Cuando se utilize conda en lugar de pip este comando guarda los comandos de creacion del ambiente:

#conda env export --from-history --file environment.yml

@app.route('/')
def hello():
    return'Hello World Colombia'
