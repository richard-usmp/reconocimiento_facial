from flask import Flask, render_template
import capturandoRostros as CP
from pip._vendor.urllib3 import request

app = Flask (__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/perdido_alguien')
def perdido_alguien():
    return render_template('perdido_alguien.html')

@app.route('/personas_desaparecidas')
def personas_desaparecidas():
    return render_template('personas_desaparecidas.html')

@app.route('/pruebas')
def pruebas():
    return render_template('pruebas.html')

@app.route('/formulario',methods=['POST'])
def formulario():
    print('ENTRA')  
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        edad = request.form['edad']
        video = request.form['video']
        print(nombre,apellido,edad)
        CP.capturandoRostros(nombre,apellido,edad,video)
        print('received')    

    if __name__ == '__main__':
        app.run(debug=True)