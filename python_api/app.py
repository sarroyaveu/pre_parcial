from flask import Flask, jsonify

app= Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status" : "success"
        "message" : "API de python ejecutandose en el puerto interno  5006 y expuesta en el puerto 5007"
        "container_name" : "contenedor_python_parcial"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5006)    
