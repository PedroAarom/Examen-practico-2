from flask import Flask, render_template, request
import pymysql

# Set the database credentials
host = 'database-1.coi9j6tpwblj.us-east-1.rds.amazonaws.com'
port = 3306
user = 'admin'
password = 'yuiop789'
database = 'datos'

# Connect to the database
connection = pymysql.connect(
    host=host,
    port=port,
    user=user,
    password=password,
    database=database
)

# Create a cursor object
cursor = connection.cursor()

app = Flask(__name__)
 
# Ruta para el formulario de entrada de datos
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para procesar los datos del formulario
@app.route('/calcular', methods=['POST'])
def calcular():
    nombre = request.form['nombre']
    edad = int(request.form['edad'])
    genero = request.form['genero']
    cursor.execute("INSERT INTO datos (nombre, edad, genero) values (%s,%s,%s)",(nombre,edad,genero))
    connection.commit()
    cursor.close()
    return render_template('resultado.html', nombre=nombre, edad=edad, genero=genero)
 
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

