from flask import Flask, redirect, url_for, request

app = Flask(__name__)

@app.route('/exito/<nombre>')
def exito(nombre):
    return 'Bienvenido, %s' % nombre

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        usuario = request.form['nm']
        return redirect(url_for('exito', nombre=usuario))
    else:
        usuario = request.args.get('nm')
        return redirect(url_for('exito', nombre=usuario))

if __name__ == '__main__':
    app.run()


# from flask import Flask, redirect, url_for
# app = Flask(__name__)
#
# @app.route('/admin')
# def hola_admin():
#     return 'Xopa Admin'
#
# @app.route('/mortal/<mortal>')
# def hola_mortal(mortal):
#     return 'Larga de aqui mortal, %s' % mortal
#
# @app.route('/usuario/<nombre>')
# def hola_usuario(nombre):
#     if nombre == 'admin':
#         return redirect(url_for('hola_admin'))
#     else:
#         return redirect(url_for('hola_mortal', mortal=nombre))
#
# if __name__ == '__main__':
#     app.run()