#Freddy Galvez      28-442-93
#Francisco Rios     AQ-1537-25
#Jose Garcia        8-8559-2208
from flask import*
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///paciente.sqlite3'
app.config['SECRET_KEY'] = 'uippc3'
db = SQLAlchemy(app)

class pacientes(db.Model):
    """
    Esta es la clase para la informacion del paciente
    """
    id = db.Column('id', db.Integer, primary_key=True)
    nombre = db.Column(db.String(50))
    edad = db.Column(db.String(3))
    direccion = db.Column(db.String(30))
    cedula = db.Column(db.String(9))
    def __init__(self,nombre, edad, direccion, cedula, celular):
        """
        Este es el metodo constructor de la clase
        :param nombre: nombre del paciente
        :param edad: edad del paciente
        :param direccion: direccion del paciente
        :param cedula: cedula del paciente
        :param celular: celular del paciente
        """
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        self.cedula = cedula
        self.celular = celular

@app.route('/')
def inicio():
    return render_template('inicio.html')
"""
Este metodo hace llamado al inicio 
"""

@app.route('/datos', methods=['GET', 'POST'])
def datos():
    if request.method == 'POST':
        if not request.form['nombre'] or not request.form['edad'] or not request.form['direccion'] or not request.form['cedula']:
            flash('Por favor introduzca todos los campos', 'error')
        else:
            paciente = pacientes(request.form['nombre'],
                                        request.form['edad'],
                                        request.form['direccion'],
                                        request.form['cedula'],
                                        request.form['celular'])
            db.session.add(paciente)
            db.session.commit()
            flash('Registro guardado con exito!')
            return redirect(url_for('sintomas'))
    return render_template('datos.html')
"""
Base de datos de los usuarios que buscan en la pagina.
"""

@app.route('/sintomas', methods=['GET', 'POST'])
def sintomas():
    if request.method == 'POST':
        if 'comunes' in request.form.values():
            return render_template('comunes.html')
        elif 'cabeza' in request.form.values():
            return render_template('cabeza.html')
        elif 'torso' in request.form.values():
            return render_template('torso.html')
        else:
            flash('por favor seleccionar algo','error')
    return render_template('sintomas.html')
"""
Lee la opcion elegida por el usuario y redirecciona a la siguiente opcion.
"""

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None

    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'FarmaciaHormigos':
            error = 'Invalid username or password. Please try again!'
        else:
            flash('Te has logueado correctamente.')
            return redirect(url_for('registros'))

    return render_template('login.html', error=error)
"""
Login para ver la base de datos de clientes que han hecho consultas
"""

@app.route('/registros')
def registros():
    return render_template('registros.html', pacientes=pacientes.query.all())
"""
Base de datos de los usuarios que han hecho busquedas en la pagina.
"""

@app.route('/dudas')
def dudas():
    return render_template('dudas.html')
"""
Terminos y condiciones de la pagina con dudas generales.
"""

@app.route('/comunes', methods=['GET', 'POST'])
def comunes():
    if request.method == 'POST':
        if 'dolor_cabeza' in request.form.values():
            return dolor_cabeza()
        elif 'dolor_muscular' in request.form.values():
            return dolor_muscular()
        elif 'dolor_garganta' in request.form.values():
            return dolor_garganta()
        elif 'sequedad_ojos' in request.form.values():
            return sequedad_ojos()
        elif 'fiebre' in request.form.values():
            return fiebre()
        elif 'gripe' in request.form.values():
            return gripe()
        elif 'diarrea_vomito' in request.form.values():
            return diarrea_vomito()
        else:
            flash('holi', error='error')

    return render_template('comunes.html')
"""
Esta metodo lee el dato que el usuario pide y lo redirecciona a otra pagina segun lo seleccionado.
"""

@app.route('/dolor_cabeza')
def dolor_cabeza():
    return render_template('dolor_cabeza.html')

@app.route('/dolor_muscular')
def dolor_muscular():
    return render_template('dolor_muscular.html')

@app.route('/dolor_garganta')
def dolor_garganta():
    return render_template('dolor_garganta.html')

@app.route('/fiebre')
def fiebre():
    return render_template('fiebre.html')

@app.route('/gripe')
def gripe():
    return render_template('gripe.html')

@app.route('/sequedad_ojos')
def sequedad_ojos():
    return render_template('sequedad_ojos.html')

@app.route('/diarrea_vomito')
def diarrea_vomito():
    return render_template('diarrea_vomito.html')
"""
Todas estan son la rutas con los metodos de las enfermadades comunes.
"""

@app.route('/cabeza',  methods=['GET', 'POST'])
def cabeza():
    if request.method == 'POST':
        if 'oidos_tapados' in request.form.values():
            return oidos_tapados()
        elif 'infeccion' in request.form.values():
            return infeccion()
        elif 'herpes' in request.form.values():
            return herpes()
        elif 'conjutivitis' in request.form.values():
            return conjutivitis()
    return render_template('cabeza.html')
"""
Esta metodo lee el dato que el usuario pide y lo redirecciona a otra pagina segun lo seleccionado.
"""

@app.route('/oidos_tapados')
def oidos_tapados():
    return render_template('oidos_tapados.html')
@app.route('/infeccion')
def infeccion():
    return render_template('infeccion.html')
@app.route('/herpes')
def herpes():
    return render_template('herpes.html')
@app.route('/conjutivitis')
def conjutivitis():
    return render_template('conjutivitis.html')
"""
Todas estan son la rutas con los metodos de las enfermadades de la opcion cabeza.
"""

@app.route('/torso', methods=['GET', 'POST'])
def torso():
    if request.method == 'POST':
        if 'acaros' in request.form.values():
            return acaros()
        elif 'cicatrices' in request.form.values():
            return cicatrices()
        elif 'quemaduras' in request.form.values():
            return quemaduras()
        elif 'mucosidad' in request.form.values():
            return mucosidad()
    return render_template('torso.html')
"""
Esta metodo lee el dato que el usuario pide y lo redirecciona a otra pagina segun lo seleccionado.
"""

@app.route('/acaros')
def acaros():
    return render_template('acaros.html')

@app.route('/cicatrices')
def cicatrices():
    return render_template('cicatrices.html')

@app.route('/quemaduras')
def quemaduras():
    return render_template('quemaduras.html')

@app.route('/mucosidad')
def mucosidad():
    return render_template('mucosidad.html')
"""
Todas estan son la rutas con los metodos de las enfermadades de la opcion torso.
"""

if __name__ == '__main__':
    db.create_all()
    app.run()