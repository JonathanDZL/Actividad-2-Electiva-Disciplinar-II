from flask import Flask,app,request,jsonify
# Importamos la librería pymysql y su módulo cursors
import pymysql.cursors

# Definimos una función para conectar a la base de datos MySQL
def connection_mysql():
    # Establecemos la conexión con los detalles de la base de datos
    connection = pymysql.connect(host='localhost',  # El host de la base de datos, generalmente es 'localhost' o la IP del servidor
                                 user='root',       # El usuario de la base de datos
                                 password='',       # La contraseña del usuario
                                 database='crud_python', # El nombre de la base de datos a conectar
                                 cursorclass=pymysql.cursors.DictCursor)  # Especificamos que queremos usar un cursor DictCursor para recuperar resultados como diccionarios
    
    return connection  # Retornamos el objeto conexión para ser usado fuera de esta función.

app = Flask(__name__)
@app.route('/usuarios', methods=["POST"])
def create():
    
    data = request.get_json()
    connection = connection_mysql()

    with connection:
        with connection.cursor() as cursor:
            sql = "INSERT INTO users (email, password) VALUES (%s, %s)"
            cursor.execute(sql, (data['email'], data['password']))

        connection.commit()

    return jsonify({
        'message': 'Creacion exitosa'
    }), 201 #:return: Un mensaje de éxito y el código de estado HTTP 201 si la creación es exitosa.

@app.route('/usuarios', methods=['GET'])
def list():
    # Establecer una conexión con la base de datos MySQL
    connection = connection_mysql()

    # Crear un cursor para ejecutar consultas SQL
    with connection.cursor() as cursor:
        # Consulta SQL para seleccionar los campos id, email y password de la tabla "users"
        sql = 'SELECT id, email, password FROM users'
        cursor.execute(sql)
        result = cursor.fetchall()

    # Devolver los resultados como JSON con un estado HTTP 200 (OK)
    return jsonify({
        'data': result
    }), 200

# Ruta para actualizar un usuario existente
@app.route('/usuarios/<int:id>', methods=['PUT'])
def update(id):
    # Obtenemos los nuevos datos del usuario desde el cuerpo de la solicitud
    data = request.get_json()
    # Establecemos la conexión con la base de datos
    connection = connection_mysql()

    with connection:
        # Creamos un cursor para ejecutar consultas SQL
        with connection.cursor() as cursor:
            # Consulta SQL para actualizar un usuario existente en la tabla "users"
            sql = "UPDATE users SET email = %s, password = %s WHERE id = %s"
            cursor.execute(sql, (data['email'], data['password'], id))
        # Hacemos commit de la transacción
        connection.commit()

    # Devolvemos un mensaje de éxito y un código de estado HTTP 200 (OK)
    return jsonify({
        'message': 'Actualizacion exitosa'
    }), 200

# Ruta para eliminar un usuario existente
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def delete(id):
    # Establecemos la conexión con la base de datos
    connection = connection_mysql()

    with connection:
        # Creamos un cursor para ejecutar consultas SQL
        with connection.cursor() as cursor:
            # Consulta SQL para eliminar un usuario existente de la tabla "users"
            sql = "DELETE FROM users WHERE id = %s"
            cursor.execute(sql, (id,))
        # Hacemos commit de la transacción
        connection.commit()

    # Devolvemos un mensaje de éxito y un código de estado HTTP 200 (OK)
    return jsonify({
        'message': 'Eliminacion exitosa'
    }), 200


# Verifica si el script es el principal.
if __name__ == '__main__':

    # Inicia el codigo en modo de depuración debug.
    app.run(debug=True)

