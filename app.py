from flask import Flask, render_template

# Crear aplicación Flask
app = Flask(__name__)

# Ruta principal
@app.route('/')
def inicio():
    return render_template('index.html')

# Ejecutar aplicación
if __name__ == '__main__':
    app.run(debug=True)