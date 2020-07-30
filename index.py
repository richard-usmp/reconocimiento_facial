from flask import Flask, render_template, request
import capturandoRostros as CP
import getNombresyFotos as getNF
import shutil
import os
import entrenamientoRF
app = Flask (__name__, static_url_path='/data')

@app.route('/')
def home():
    ##import reconocimientofacial as R
    return render_template('home.html')

@app.route('/perdido_alguien')
def perdido_alguien():
    return render_template('perdido_alguien.html')

@app.route('/personas_desaparecidas')
def personas_desaparecidas():
    arrayNom =[]
    fotox = []
    for i in range(len(getNF.getNombres())):
        arrayNom.append(getNF.getNombres()[i])
    
    for i in range(len(getNF.getImage())):
        fotox.append(getNF.getImage()[i])
        print(fotox)
    return render_template('personas_desaparecidas.html', arrayNom_e = arrayNom, foto = fotox)

@app.route('/tests')
def pruebas():
    return render_template('tests.html')

@app.route('/formulario',methods=['POST'])
def formulario():
    
    
    
   
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    edad = request.form['edad']
    video = request.form['files']   
    print(nombre,apellido,edad,video)
    
    
    shutil.move(video, 'C:/Users/USUARIO/Desktop/PIA/reconocimiento_facial/'+video)
    
    CP.capturandoRostros(nombre,apellido,edad,video)
    CP.construir(nombre,apellido,edad,video)
    
    print('received-------------------------------------------------------------------') 
    return render_template('perdido_alguien.html')
    

if __name__ == '__main__':
        app.run(debug=True)