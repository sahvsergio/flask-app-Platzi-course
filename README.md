# flask-app-Platzi-course

# flask-app-Platzi-course

#FLASK_APP: this is the variable meant to identify the file where the application is located

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

#conda env export --from-history --file environment.yml.
export FLASK_DEBUG=1
echo $FLASK_DEBUG
if __name__ == '__main__':
    app.run(debug=True)


    El codigo es vulnerable a XSS. Una ves que la cookie user_ip es guardada en el browser, el usuario es capaz de modificarla y ejecutar lo que guste.

Para evitar esto, recomendaria importar escape de flask, y hacer lo siguiente:

@app.route("/hello")
def ip():
	user_ip = request.cookies.get('user_ip')
	user_ip = escape(user_ip)
	return "Tu ip es {}".format(user_ip)

Si no saben que es XSS, les dejo algunos recursos:

En español: https://www.youtube.com/watch?v=inCS6PQYu34

En ingles: https://www.youtube.com/watch?v=EoaDgUgS6QA

Puedes optimizar el código escapando el dato de entrada en la misma línea de código de la variable user_ip:

user_ip = escape(request.remote_addr)

{% for key, segment in segment_details.items() %}
        <tr>
                <td>{{ key }}td>
                <td>{{ segment }}td>
        tr>
{% endfor %}  


os asteriscos se deben a que locals() nos regresa un dict con las variables del contexto, pero render_template solo resive un argumento, asi que pasamos el diccionario con key y values en forma de argumentos opcionales. 

Esto es util cuando empezamos a tener muchos datos en el entorno.

return render_template('hello.htmrno. l', **locals())```

Dato bastante útil, En caso que las variables estén definidas como globales (fuera de las funciones) se puede usar el equivalente **globals()