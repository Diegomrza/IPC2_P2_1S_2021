import tkinter
#from tkinter import *
from tkinter import filedialog
import xml.etree.ElementTree as ET
from xml import etree
from Matriz import matriz_ortogonal
from ListaSimple import ListaSimple

matrices_ortogonales = ListaSimple()
contador_filas = 1
contador_columnas = 1

#Operaciones principales
def cargar_archivos():

    try:
        ventana = tkinter.Tk()
        ruta = filedialog.askopenfilename(title="Seleccione un archivo", 
                filetypes = (("xml files","*.xml"),("all files","*.*")))
        ventana.destroy()

        tree = ET.parse(ruta)
        root = tree.getroot()

        for elemento in root:


            for subelemento in elemento:


                nombre = ''

                if subelemento.tag == 'nombre':

                    nombre = subelemento.text
                    print(nombre)

                if subelemento.tag == 'imagen':

                    lista = subelemento.text.split('\n')

                    for x in lista:
                        separar_elementos(x)

                    global contador_filas
                    contador_filas = 1
    except IOError:
        print('Error al leer el archivo')

                
def separar_elementos(cadena):

    global contador_filas, contador_columnas
    print('Cadena: ',cadena)

    matriz = matriz_ortogonal()

    for x in cadena:
        if x == '*' or x == '-':
            print('Fila: ',str(contador_filas),'\tColumna: ',str(contador_columnas),'\tValor: ',x)
            matriz.insertar(contador_filas,contador_columnas, x)
            contador_columnas += 1
            
        else:
            continue

    contador_columnas = 1
    if cadena != '':
        contador_filas += 1

    matriz.recorrerFilas()

def operaciones():
    pass

def reportes():
    pass

def ayuda():
    pass


root = tkinter.Tk()
root.title('Ventana Principal')
#root.geometry('1000x600')
root.resizable(1,1)

frame_principal = tkinter.Frame(root,width='567',height='476',bg='green')
frame_principal.pack()

#SubFrames
frame0 = tkinter.Frame(frame_principal,width='250',height='330',bg='red')
frame1 = tkinter.Frame(frame_principal,width='250',height='330',bg='blue')
frame0.place(x=25,y=100)
frame1.place(x=290,y=100)

tkinter.Button(frame_principal,text='Cargar Archivo', command=cargar_archivos, bg='gray',font=('Comic Sans MS',18)).place(x=0,y=0)
tkinter.Button(frame_principal,text='Operaciones', command=operaciones, bg='gray',font=('Comic Sans MS',18)).place(x=190,y=0)
tkinter.Button(frame_principal,text='Reportes', command=reportes, bg='gray',font=('Comic Sans MS',18)).place(x=352,y=0)
tkinter.Button(frame_principal,text='Ayuda', command=ayuda, bg='gray',font=('Comic Sans MS',18)).place(x=476,y=0)












root.mainloop()

'''raiz = Tk() #Creacion de la ventana
raiz.title('Principal') #Titulo de la ventana
raiz.iconbitmap('Prueba.ico') #Icono de la ventana

#raiz.geometry('650x350') #Dimensiones de la ventana
raiz.config(bg='red') #Color de fondo de la ventana


frame = Frame() #Creacion de nuevo Frame
frame.pack() #Empaquetado junta la ventana con el frame
frame.config(bg='yellow') #Color del frame
frame.config(width='800', height='800') #dimensiones del frame

#frame.pack(side='top', anchor='e') #Posicion del frame
#frame.pack(fill='y', expand='True') #Expandir verticalmente
#frame.pack(fill='both',expand='True') #Expandir alto y ancho

raiz.resizable(1,1) #Redimensionar la ventana, recibe dos parametros booleanos'''

#Pestañas
'''#Creacion de las pestañas

nb = ttk.Notebook(root)
nb.pack(fill='both',expand='yes')

p1 = ttk.Frame(nb)
p2 = ttk.Frame(nb)
p3 = ttk.Frame(nb)
p4 = ttk.Frame(nb)

#Agregrar todas las pestañas al frame
nb.add(p1, text='Cargar Archivo')
nb.add(p2, text='Operaciones')
nb.add(p3, text='Reportes')
nb.add(p4, text='Ayuda')'''