from flask import Flask, render_template, request
from flaskext.mysql import MySQL

app=Flask(__name__)

#conexion base de datos
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'Jesus-Restrepo.2003'
app.config['MYSQL_DB'] = 'registro'
mysql=MySQL(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/habitaciones')
def habitaciones():
    return render_template('habitaciones.html')

@app.route('/contactenos')
def contactenos():
    return render_template('contactenos.html')

@app.route('/sobre-nosotros')
def nosotros():
    return render_template('nosotros.html')

@app.route('/trabaja-con-nosotros')
def trabaja():
    return render_template('trabajo.html')

@app.route('/reserva')
def reserva():
    return render_template('reserva.html')

@app.route('/habitacion/doble-estandar')
def doble():
    return render_template('doble.html')

@app.route('/habitacion/sencilla')
def sencilla():
    return render_template('sencilla.html')

@app.route('/habitacion/suite-especial/5-estrellas')
def suite():
    return render_template('suite.html')

@app.route('/habitacion/doble-cama')
def double():
    return render_template('doblecama.html')

@app.route('/comprobar', methods=['POST'])
def comprobar():
    if request.method == 'POST':
        identificacion = request.form['identificacion']
        nombre = request.form['nombre']
        telefono = request.form['telefono']
        email = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO informacion (identificacion, nombre, telefono, email) VALUES(%s, %s, %s, %s)', 
        (identificacion, nombre, telefono, email))
        mysql.connection.commit()
        return render_template('comprobar.html')

    if __name__ == '__main__':
        app.run(debug=True)
