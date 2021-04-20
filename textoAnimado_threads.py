
#|------------------------------------------------------------|
#| ACLARACION: Es el mismo codigo de textoAnimado, pero hago  |
#| la implementacion de los THREADS aca, de forma separada.   |
#|------------------------------------------------------------|

#Importa módulos para Interfaz Gráfica de usuario (tkinter)
import tkinter as tk
from tkinter import ttk
import time
import threading

#Crea la ventana principal
main_window = tk.Tk()
main_window.title("Ejemplo")
main_window.configure(width=350, height=200)

#Función que crea y posiciona el botón "Salir"
def opcionFinalizar():
    boton = ttk.Button(main_window, text="Salir", command=main_window.destroy)
    boton.place(x=170, y=170)

#Función que crea una etiqueta (label) de texto en la posición (x,y) de la pantalla.
def createLabel(a,b):
    label = ttk.Label(text="")
    label.place(x=a,y=b)
    return label

#Función que crea una etiqueta (llamando a createLabel()) y luego anima texto dentro de la misma.
def crearAnimacion(a, b, char,retardo=0.25):
    mylabel = createLabel(a,b)
    texto=""
    #retardo: float=0.25  //variable movida a parametros de la funcion.
    for i in range(0,35):
        time.sleep(retardo)
        texto += char
        mylabel.config(text = texto)
        main_window.update_idletasks()
        main_window.update()


#Creamos los procesos:
thread_H = threading.Thread(target=crearAnimacion,args=(10,10,'H',0.10),)
thread_O = threading.Thread(target=crearAnimacion,args=(10,30,'O',0.20),)
thread_L = threading.Thread(target=crearAnimacion,args=(10,50,'L',0.40),)
thread_A = threading.Thread(target=crearAnimacion,args=(10,70,'A',0.80),)

#Los ejecutamos:
thread_H.start()
thread_O.start()
thread_L.start()
thread_A.start()

# Mantener las siguientes líneas siempre al final del script y en el mismo orden.
#Coloca la opcion "Salir"
opcionFinalizar()

#Bucle principal de la ventana
main_window.mainloop()


