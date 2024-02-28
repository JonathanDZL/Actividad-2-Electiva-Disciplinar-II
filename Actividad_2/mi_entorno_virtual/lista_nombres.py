from flask import Flask, jsonify

# Crear una instancia de la aplicación Flask
app = Flask(__name__)

# Definir la ruta en este caso "/personas" que responde a solicitudes GET
@app.route('/personas', methods=['GET'])
def obtener_personas():

    #Esta función de vista se ejecuta cuando se realiza una solicitud GET a '/personas'. 
    # Codigo de lista estática de nombres de personas
    lista_personas = ["Jonathan", "Marta", "Jesus", "Juancho"]
    
     # Convierte la lista para retornarlo a formato JSON utilizando jsonify.
    return jsonify(personas=lista_personas)

# Verifica si el script es el principal.
if __name__ == '__main__':

    # Inicia el codigo en modo de depuración debug.
    app.run(debug=True)
