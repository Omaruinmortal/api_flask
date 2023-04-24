from flask import Flask, jsonify
from flask_mysqldb import MySQL
from config import config

app = Flask(__name__)

conexion = MySQL(app)

#Ruta
@app.route('/personal', methods=['GET'])

#funcion
def listar_personal():
    try:
        cursor=conexion.connection.cursor()
        sql = 'SELECT id_evaluado,num_empleado,nombre_completo FROM cat_eva_evaluacion_desempeno'
        cursor.execute(sql)
        datos=cursor.fetchall()
        personal=[]
        for fila in datos:
            persona={'id_evaluado':fila[0], 'num_empleado':fila[1], 'nombre_completo':fila[2]}
            personal.append(persona)
        return jsonify({'personal':personal,'mensaje':'Personal listado.'})
    except Exception as ex:
        return jsonify({'mensaje':'Error de listado.'})

@app.route('/personal/<codigo>', methods=['GET'])
def leer_persona(codigo):
    try:
        cursor=conexion.connection.cursor()
        sql = "SELECT id_evaluado,num_empleado,nombre_completo FROM cat_eva_evaluacion_desempeno where num_empleado = '{0}'".format(codigo)
        cursor.execute(sql)
        datos=cursor.fetchone()
        if datos != None:
            persona={'id_evaluado':datos[0], 'num_empleado':datos[1], 'nombre_completo':datos[2]}
            return jsonify({'personal':persona,'mensaje':'Personal encontrado.'})
        else:
            return jsonify({'mensaje':'Persona no encontrada.'})
    except Exception as ex:
        return jsonify({'mensaje':'Error de busqueda.'})
def pagina_no_encontrada(error):
    return '<h1>Pagina no encontrada</h1>'

if __name__ == '__main__':
    app.config.from_object(config['development'])
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()


#instalar entorno virtual 
#virtualenv -p python3 env
#activar entorno activo env/Scripts/activate
#intalar py install flask flask_mysqldb