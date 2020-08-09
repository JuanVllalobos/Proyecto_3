from reconociento import reconocer_caras
import cv2 
from tkinter import *
from tkinter import ttk
from datetime import datetime
from PIL import ImageTk
from PIL import Image  
from reconociento import reconocer_caras
import json
import tkinter as tk  
import jsonpickle
import os, io
from google.cloud import vision
from google.cloud.vision import types
from tkinter import filedialog

#Esta va a ser la lista donde se almacenarán los registros
asistencias = []

#Esto crea la ventana "top"
top = Tk()

#Esta definición cumple la función de abrir la ventana donde uno debe seleccionar los archivos deseados
def cargar_imagen():
    top.filename =  filedialog.askopenfile(initialdir = "/",title = "Select file",filetypes = (("jpeg files",".jpg"),("all files",".*")))


def capturar_Qr():
    """En resumidas cuentas, esta definición cumple la función de realizar la lectura del código Qr y lo muestra en los Entry.
    """
    cap = cv2.VideoCapture(0)
    leido, frame = cap.read()
    if leido == True:
        cv2.imwrite("cedula.png", frame)
        print("Foto tomada correctamente")
    else:
        print("Error al acceder a la cámara")
    cap.release()
    img=cv2.imread(r'cedula.png')
    detector=cv2.QRCodeDetector()
    data, points, stight_code = detector.detectAndDecode(img)
    global part_ced
    global part_cod
    part_ced = data[0:8]
    part_cod = data[9:]
    
#Esta definición cumple con la función de capturar la fotografía en ese mismo momento, y la envía al API de Google para extraer su reconocimiento de emociones.
def capturar_imagen():
    cap = cv2.VideoCapture(0)
    leido, frame = cap.read()
    if leido == True:
        cv2.imwrite("jiji.png", frame)
        print("Foto tomada correctamente")
    else:
        print("Error al acceder a la cámara")
    cap.release()
    
    suma1=0
    suma2=0
    suma3=0
    suma4=0
    suma5=0
    suma6=0
    suma7=0
    datos = reconocer_caras("jiji.png")
    posicion = datos[0]["face_expressions"]["joy_likelihood"]
    if posicion == "VERY_LIKELY":
        suma1+=5
    elif posicion == "LIKELY":
        suma1+=4
    elif posicion == "POSSIBLE":
        suma1+=3
    elif posicion == "UNLIKELY":
        suma1+=2
    elif posicion == "VERY_UNLIKELY":
        suma1+=0    
    suma1= (suma1/1)*20
    
    posicion = (datos[0]["face_expressions"]["sorrow_likelihood"])
    if posicion == "VERY_LIKELY":
        suma2+=5
    elif posicion == "LIKELY":
        suma2+=4
    elif posicion == "POSSIBLE":
        suma2+=3
    elif posicion == "UNLIKELY":
        suma2+=2
    elif posicion == "VERY_UNLIKELY":
        suma2+=0
    suma2= (suma2/1)*20
    
    posicion = (datos[0]["face_expressions"]["anger_likelihood"])
    if posicion == "VERY_LIKELY":
        suma3+=5
    elif posicion == "LIKELY":
        suma3+=4
    elif posicion == "POSSIBLE":
        suma3+=3
    elif posicion == "UNLIKELY":
        suma3+=2
    elif posicion == "VERY_UNLIKELY":
        suma3+=0
    suma3= (suma3/1)*20
    
    posicion = (datos[0]["face_expressions"]["surprise_likelihood"])
    if posicion == "VERY_LIKELY":
        suma4=5
    elif posicion == "LIKELY":
        suma4+=4
    elif posicion == "POSSIBLE":
        suma4+=3
    elif posicion == "UNLIKELY":
        suma4+=2
    elif posicion == "VERY_UNLIKELY":
        suma4+=0    
    suma4= (suma4/1)*20
    
    posicion = (datos[0]["face_expressions"]["under_exposed_likelihood"])
    if posicion == "VERY_LIKELY":
        suma5+=5
    elif posicion == "LIKELY":
        suma5+=4
    elif posicion == "POSSIBLE":
        suma5+=3
    elif posicion == "UNLIKELY":
        suma5+=2
    elif posicion == "VERY_UNLIKELY":
        suma5+=0    
    suma5= (suma5/1)*20
    
    posicion = (datos[0]["face_expressions"]["blurred_likelihood"])
    if posicion == "VERY_LIKELY":
        suma6+=5
    elif posicion == "LIKELY":
        suma6+=4
    elif posicion == "POSSIBLE":
        suma6+=3
    elif posicion == "UNLIKELY":
        suma6+=2
    elif posicion == "VERY_UNLIKELY":
        suma6+=0    
    suma6= (suma6/1)*20
    
    posicion = (datos[0]["face_expressions"]["headwear_likelihood"])
    if posicion == "VERY_LIKELY":
        suma7+=5
    elif posicion == "LIKELY":
        suma7+=4
    elif posicion == "POSSIBLE":
        suma7+=3
    elif posicion == "UNLIKELY":
        suma7+=2
    elif posicion == "VERY_UNLIKELY":
        suma7+=0
        suma7= (suma7/1)*20

    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7

    s1 = str(suma1)
    s2 = str(suma2)
    s3 = str(suma3)
    s4 = str(suma4)
    s5 = str(suma5)
    s6 = str(suma6)
    s7 = str(suma7)
   
def extraer_reconocimiento():
    """Esta definición tiene como propósito, enviar una imagen al API de Google, la cual va a ser seleccionada desde el explorador de archivos, para extraer su debido reconocimiento de emociones
    """
    suma1=0
    suma2=0
    suma3=0
    suma4=0
    suma5=0
    suma6=0
    suma7=0
    cargar_imagen()
    datos = reconocer_caras(top.filename.name)
    posicion = datos[0]["face_expressions"]["joy_likelihood"]
    if posicion == "VERY_LIKELY":
        suma1+=5
    elif posicion == "LIKELY":
        suma1+=4
    elif posicion == "POSSIBLE":
        suma1+=3
    elif posicion == "UNLIKELY":
        suma1+=2
    elif posicion == "VERY_UNLIKELY":
        suma1+=0    
    suma1= (suma1/1)*20
    
    posicion = (datos[0]["face_expressions"]["sorrow_likelihood"])
    if posicion == "VERY_LIKELY":
        suma2+=5
    elif posicion == "LIKELY":
        suma2+=4
    elif posicion == "POSSIBLE":
        suma2+=3
    elif posicion == "UNLIKELY":
        suma2+=2
    elif posicion == "VERY_UNLIKELY":
        suma2+=0
    suma2= (suma2/1)*20
    
    posicion = (datos[0]["face_expressions"]["anger_likelihood"])
    if posicion == "VERY_LIKELY":
        suma3+=5
    elif posicion == "LIKELY":
        suma3+=4
    elif posicion == "POSSIBLE":
        suma3+=3
    elif posicion == "UNLIKELY":
        suma3+=2
    elif posicion == "VERY_UNLIKELY":
        suma3+=0
    suma3= (suma3/1)*20
    
    posicion = (datos[0]["face_expressions"]["surprise_likelihood"])
    if posicion == "VERY_LIKELY":
        suma4=5
    elif posicion == "LIKELY":
        suma4+=4
    elif posicion == "POSSIBLE":
        suma4+=3
    elif posicion == "UNLIKELY":
        suma4+=2
    elif posicion == "VERY_UNLIKELY":
        suma4+=0   
    suma4= (suma4/1)*20
    
    posicion = (datos[0]["face_expressions"]["under_exposed_likelihood"])
    if posicion == "VERY_LIKELY":
        suma5+=5
    elif posicion == "LIKELY":
        suma5+=4
    elif posicion == "POSSIBLE":
        suma5+=3
    elif posicion == "UNLIKELY":
        suma5+=2
    elif posicion == "VERY_UNLIKELY":
        suma5+=0   
    suma5 = (suma5/1)*20
    
    posicion = (datos[0]["face_expressions"]["blurred_likelihood"])
    if posicion == "VERY_LIKELY":
        suma6+=5
    elif posicion == "LIKELY":
        suma6+=4
    elif posicion == "POSSIBLE":
        suma6+=3
    elif posicion == "UNLIKELY":
        suma6+=2
    elif posicion == "VERY_UNLIKELY":
        suma6+=0    
    suma6 = (suma6/1)*20
    
    posicion = (datos[0]["face_expressions"]["headwear_likelihood"])
    if posicion == "VERY_LIKELY":
        suma7+=5
    elif posicion == "LIKELY":
        suma7+=4
    elif posicion == "POSSIBLE":
        suma7+=3
    elif posicion == "UNLIKELY":
        suma7+=2
    elif posicion == "VERY_UNLIKELY":
        suma7+=0
        suma7 = (suma7/1)*20
    
    global s1
    global s2
    global s3
    global s4
    global s5
    global s6
    global s7

    s1 = str(suma1)
    s2 = str(suma2)
    s3 = str(suma3)
    s4 = str(suma4)
    s5 = str(suma5)
    s6 = str(suma6)
    s7 = str(suma7)

def abrir_registrar_asistencias():
    """Esta definición cumple la función de desplegar una ventana con multiples botones funcionales,
     los cuales cumplen la función de realizar diversas tareas definidas a continuación.
    """
    #Acá se crea dicha ventana
    root = Tk()

    #Este label indica la posición en la cual se desplegaran los datos que corresponden a la cédula.
    label = Label(root, text="Cédula Registrada")
    label.grid(row=0, column=0, padx=5, pady=5)

    #Este es un entry vacío, en el cual se mostrarán los datos correspondientes a la cédula.
    entry = Entry(root)
    entry.grid(row=0, column=1, padx=5, pady=5)

    #Este label indica la posición en la cual se desplegaran los datos que corresponden al código del curso.
    label2 = Label(root, text="Código Registrado")
    label2.grid(row=1, column=0, padx=5, pady=5)

    #Este es un entry vacío, en el cual se mostrarán los datos correspondientes al código del curso.
    entry2 = Entry(root)
    entry2.grid(row=1, column=1, padx=5, pady=5)


    class asistencia():
        """En esta parte se crea la clase asistencia, la cual dispone de multiples valores como lo son la cédula, el codigo, la hora de registro, etc.
        """
        def __init__(self, cedula, codigo, hora_registro, expresion_1, expresion_2, expresion_3, expresion_4, expresion_5, expresion_6, expresion_7):
            self.cedula=cedula
            self.codigo=codigo
            self.hora_registro=hora_registro
            self.expresion_1=expresion_1
            self.expresion_2=expresion_2
            self.expresion_3=expresion_3
            self.expresion_4=expresion_4
            self.expresion_5=expresion_5
            self.expresion_6=expresion_6
            self.expresion_7=expresion_7
        #Esta definición cumple la función de mostrar los datos que contiene "asistencia" en forma str.    
        def __str__(self):
                string = u"[<asistencia> cedula:%s codigo:%s  Fecha:%s Felicidad:%s Dolor:%s Disgusto:%s Sorpresa:%s Subexpuesta:%s borrosa:%s Gorro:%s]" %(self.cedula, self.codigo, self.hora_registro, self.expresion_1, self.expresion_2, self.expresion_3, self.expresion_4, self.expresion_5, self.expresion_6, self.expresion_7)
                return string

    #Esta definición cumple la función de insertarle los valores que corresponden a la cédula y al código, a los dos entry que antes se definieron.
    def llamar_inserts():
        capturar_Qr()
        entry.insert(0, part_ced)
        entry2.insert(0, part_cod)

    #Esta función lo que hace es otorgarle lo que corresponde a cada valor a la asistencia
    def formar_asistencia():
        hora_exacta = datetime.now()
        cedula_entry = entry.get()
        codigo_entry2 = entry2.get()
        asistencias.append(asistencia(cedula_entry, codigo_entry2, hora_exacta, s1, s2, s3, s4, s5, s6, s7))
        for cd in asistencias:
            print(cd)

    #Esta definición cumple la función de finalizar o cerrar la ventana.
    def cerrar_ventana():
        root.quit()
    
    #Este botón cumple la función de realizar la acción que tiene la definición formar_asistencia
    bot1 = Button(root, text="Guardar Registro", command = formar_asistencia)
    bot1.grid(row=0, column=2, padx=5, pady=5)

    #Este botón cumple la función de realizar la acción que tiene la definición cerrar_ventana
    bot2 = Button(root, text="Cerrar", command = cerrar_ventana)
    bot2.grid(row=5, column=1, padx=5, pady=5)

    #Este botón cumple la función de realizar la acción que tiene la definición llamar_inserts
    bot3 = Button(root, text="Capturar Qr", command = llamar_inserts)
    bot3.grid(row=4, column=1, padx=5, pady=5)

    #Este botón cumple la función de realizar la acción que tiene la definición capturar_imagen
    bot4 = Button(root, text="Capturar Foto", command = capturar_imagen)
    bot4.grid(row=3, column=1, padx=5, pady=5)

    #Este botón cumple la función de realizar la acción que tiene la definición extraer reconocimiento
    bot5 = Button(root, text="Cargar Foto", command = extraer_reconocimiento)
    bot5.grid(row=2, column=1, padx=5, pady=5)

    #Esto detiene
    root.mainloop()


#Este es el menu de acciones
menubar = Menu(top)
menuaccion = Menu(menubar, tearoff=0) 
menuaccion.add_command(label="Registrar Asistencia", command=abrir_registrar_asistencias)

#Esto es para crear un separador entre las dos opciones
menuaccion.add_separator()

#Esta opción cumple con la función de detener la aplicación.
menuaccion.add_command(label="Salir!", command=top.quit)
menubar.add_cascade(label="Accion", menu=menuaccion) 
top.config(menu=menubar)

top.mainloop()