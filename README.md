# flask-app-Platzi-course

# flask-app-Platzi-course

#FLASK_APP: this is the variable meant to identify the file where the application is located

# in the terminal just write export FLASK_APP=main.py on linux, set FLASK_APP=main.py on Windows and on powershell $env:FLASK_APP = ‘main.py’

#to check, just run echo $FLASK_APP, it should return main.py
#type "flask run"

#para los que trabajan con anaconda:

Macro: son un conjunto de comandos que se invocan con una palabra clave, opcionalmente seguidas de parámetros que se utilizan como código literal. Los Macros son manejados por el compilador y no por el ejecutable compilado.

Los macros facilitan la actualización y mantenimiento de las aplicaciones debido a que su re-utilización minimiza la cantidad de código escrito necesario para escribir un programa.

En este ejemplo nuestra macro se vería de la siguiente manera:

{% macro nav_link(endpoint, text) %}
{% if request.endpoint.endswith(endpoint) %}
<li class="active"><a href="{{ url_for(endpoint) }}">{{text}}a>li>
{% else %}
<li><a href="{{ url_for(endpoint) }}">{{text}}a>li>
{% endif %}
{% endmacro %}

Un ejemplo de uso de macros en Flask:

{% from "macros.html" import nav_link with context %}

<html lang="en">
    <head>
    {% block head %}
        <title>My applicationtitle>
    {% endblock %}
    head>
    <body>
        <ul class="nav-list">
            {{ nav_link('home', 'Home') }}
            {{ nav_link('about', 'About') }}
            {{ nav_link('contact', 'Get in touch') }}
        ul>
    {% block body %}
    {% endblock %}
    body>
html>

Como podemos observar en la primera línea estamos llamando a macros.html que contiene todos nuestros macros, pero queremos uno en específico así que escribimos import nav_link para traer el macro deseado y lo renderizamos de esta manera en nuestro menú {{ nav_link('home', 'Home') }}.
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
if **name** == '**main**':
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

return render_template('hello.htmrno. l', \*\*locals())```

Dato bastante útil, En caso que las variables estén definidas como globales (fuera de las funciones) se puede usar el equivalente \*\*globals()

Macro: son un conjunto de comandos que se invocan con una palabra clave, opcionalmente seguidas de parámetros que se utilizan como código literal. Los Macros son manejados por el compilador y no por el ejecutable compilado.

Los macros facilitan la actualización y mantenimiento de las aplicaciones debido a que su re-utilización minimiza la cantidad de código escrito necesario para escribir un programa.

En este ejemplo nuestra macro se vería de la siguiente manera:

{% macro nav_link(endpoint, text) %}
{% if request.endpoint.endswith(endpoint) %}
<li class="active"><a href="{{ url_for(endpoint) }}">{{text}}a>li>
{% else %}
<li><a href="{{ url_for(endpoint) }}">{{text}}a>li>
{% endif %}
{% endmacro %}

Un ejemplo de uso de macros en Flask:

{% from "macros.html" import nav_link with context %}

<html lang="en">
    <head>
    {% block head %}
        <title>My applicationtitle>
    {% endblock %}
    head>
    <body>
        <ul class="nav-list">
            {{ nav_link('home', 'Home') }}
            {{ nav_link('about', 'About') }}
            {{ nav_link('contact', 'Get in touch') }}
        ul>
    {% block body %}
    {% endblock %}
    body>
html>

Como podemos observar en la primera línea estamos llamando a macros.html que contiene todos nuestros macros, pero queremos uno en específico así que escribimos import nav_link para traer el macro deseado y lo renderizamos de esta manera en nuestro menú {{ nav_link('home', 'Home') }}.


Después de media hora sin poder poner la imagen y con el error de image not found, encontré que es bastante útil darle los path a Flask desde el principio

app = Flask(__name__, template_folder='../templates', static_folder='../static')

el .. simplemente es para decirle que empieza en la carpeta donde esta, hacia atras