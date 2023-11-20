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

app = Flask(**name**, template_folder='../templates', static_folder='../static')

el .. simplemente es para decirle que empieza en la carpeta donde esta, hacia atras

Bueno atualmente ya es soprtado Bootstrap4 solo que lo tienes que especificar a la hora de hacer pip install

pip install Flask-Bootstrap4

Para activar el development mode debes escribir lo siguiente en la consola:

export FLASK_ENV=development
echo $FLASK_ENV

SESSION: es un intercambio de información interactiva semipermanente, también conocido como diálogo, una conversación o un encuentro, entre dos o más dispositivos de comunicación, o entre un ordenador y usuario

en python existen varias formas de generar strings seguros.

Esta es una de ellas:

import os, binascii
binascii.b2a_hex(os.urandom(20))

Que como resultado daria algo así:

'b6026f861fd41a94c3389d54293de9d04bde6f7c'

Otra forma es usando el modulo secrets que segun su propia documentación indica que se utiliza para generar números aleatorios criptográficamente fuertes, adecuados para administrar datos como contraseñas, autenticación de usuarios, tokens de seguridad y secretos relacionados, el codigo seria este:

import secrets
secrets.token_hex(20)

Que como resultado daría algo así:

'ccaf5c9a22e854856d0c5b1b96c81e851bafb288'

Por ultimo se puede usar tambíen la función token_urlsafe con este codigo:

secrets.token_urlsafe(20)

Obteniendo como resultado algo así:

'dxM4-BL1CPeHYIMmXNQevdlsvhI'

app.config['']
puede tener los siguientes keys:

DEBUG
TESTING
PROPAGATE_EXCEPTIONS
SECRET_KEY
PERMANENT_SESSION_LIFETIME
USE_X_SENDFILE
SERVER_NAME
APPLICATION_ROOT
SESSION_COOKIE_NAME
SESSION_COOKIE_DOMAIN
SESSION_COOKIE_PATH
SESSION_COOKIE_HTTPONLY
SESSION_COOKIE_SECURE
SESSION_COOKIE_SAMESITE
SESSION_REFRESH_EACH_REQUEST
MAX_CONTENT_LENGTH
SEND_FILE_MAX_AGE_DEFAULT
TRAP_BAD_REQUEST_ERRORS
TRAP_HTTP_EXCEPTIONS
EXPLAIN_TEMPLATE_LOADING
PREFERRED_URL_SCHEME
TEMPLATES_AUTO_RELOAD
MAX_COOKIE_SIZE
BOOTSTRAP_USE_MINIFIED
BOOTSTRAP_CDN_FORCE_SSL
BOOTSTRAP_QUERYSTRING_REVVING
BOOTSTRAP_SERVE_LOCAL
BOOTSTRAP_LOCAL_SUBDOMAIN

Para los rebeldes (como yo) que no usamos boostrap, Y por ende, hicimos la plantilla así:

<div class="container-form">
        <form action="{{url_for('hello')}}" method="POST">
            {{login_form.username.label}}
            {{login_form.username}}
            {{login_form.password.label}}
            {{login_form.password}}
            {{login_form.submit}}
        </form>
    </div>

Esta es la configuración para que el resultado sea igual al de Bernardo.

app.config['WTF_CSRF_ENABLED']= False

Lo que pasa es que los formularios hay que cifrarlos para poder mandar la información más segura y ese proceso lo hace boostrap por defecto. Mientras que el método manual, toca tambien cifrarlo pero de forma manual.

e pasaba lo mismo. La respuesta es que se necesita enviar el token del formulario (CSRF). Faltaría añadir: {{ login_form.csrf_token }} Entonces ya puedes validar con la función "validate_on_submit". Espero que te sirva. Saludos.

  <form action="{{ url_for('hello') }}" method="POST">
                {{ login_form.csrf_token }}
                {{ login_form.username.label }}
                {{ login_form.username }}
                {{ login_form.password.label }}                
                {{ login_form.password }}                
                {{ login_form.submit }}                              
            </form>

Flask acepta peticiones GET por defecto y por ende no debemos declararla en nuestras rutas.

Pero cuando necesitamos hacer una petición POST al enviar un formulario debemos declararla de la siguiente manera, como en este ejemplo:

@app.route('/platzi-post', methods=['GET', 'POST'])

Debemos declararle además de la petición que queremos, GET, ya que le estamos pasando el parámetro methods para que acepte solo y únicamente las peticiones que estamos declarando.

De esta forma, al actualizar el navegador ya podremos hacer la petición POST a nuestra ruta deseada y obtener la respuesta requerida.

La etapa de pruebas se denomina testing y se trata de una investigación exhaustiva, no solo técnica sino también empírica, que busca reunir información objetiva sobre la calidad de un proyecto de software, por ejemplo, una aplicación móvil o un sitio web.

El objetivo del testing no solo es encontrar fallas sino también aumentar la confianza en la calidad del producto, facilitar información para la toma de decisiones y detectar oportunidades de mejora.

La función self.assertRedirects extrae el atributo location del primer parámetro (“response”) , y del segundo revisa el netloc, que seria para ambos parámetros
localhost
Para esto usa la función urlparse, pero no toma el netloc, solo el path ‘/’ en index y ‘/hello’ .
Como no encuentra el netloc en el segundo parametro, le añadi ‘localhost’, por lo que la comparación queda mal.
Posiblemente esto no ocurría en las versiones anteriores de Flask-Testing.
Así que modifique la función del modulo. Ya que en Visual Code se puede acceder a la función directamente ubicando el puntero en esta y presionando CTRL.
Aquí esta el código corregido. Sé que el código puede ser más prolijo pero priorice claridad de uso sobre limpieza.
Aquí esta el repositorio original:
jarus/ flask-testing

<h4>En el tercer test subraya **assertRedirects** con click derecho despliega las opciones, escoge la primera "Go to definition" y en la línea 304 en utils.py cambia el  — if parts.netloc — por — if parts.path --</h4>


    https://pythonise.com/series/learning-flask/flask-application-structure
    https://dev.to/aligoren/how-i-structure-my-flask-apps-3eh8
    https://flask.palletsprojects.com/en/1.1.x/tutorial/layout/
    https://flask.palletsprojects.com/en/1.1.x/tutorial/factory/
    https://bitybyte.github.io/Organzando-codigo-Python/

