import tkinter
from tkinter import *
from tkinter import filedialog, ttk
import xml.etree.ElementTree as ET
from xml import etree
from Matriz import matriz_ortogonal
from ListaSimple import ListaSimple

matrices_ortogonales = ListaSimple()
contador_filas = 1
contador_columnas = 1

#Operaciones principales
def cargar_archivos():
    global contador_filas, contador_columnas
    try:
        ventana = tkinter.Tk()
        ruta = filedialog.askopenfilename(title="Seleccione un archivo", 
                filetypes = (("xml files","*.xml"),("all files","*.*")))
        ventana.destroy()

        tree = ET.parse(ruta)
        root = tree.getroot()

        for elemento in root:
            nombre = ''
            fila = 0
            columna = 0
            contador_elementos = 0
            matriz = matriz_ortogonal()
            for subelemento in elemento:
                
                if subelemento.tag == 'nombre':
                    nombre = subelemento.text
                elif subelemento.tag == 'filas':
                    fila = int(subelemento.text)
                elif subelemento.tag == 'columnas':
                    columna = int(subelemento.text)
                elif subelemento.tag == 'imagen':
                    lista = subelemento.text.split('\n')
                    
                    for x in lista:
                        for y in x:
                            if y == '*' or y == '-':
                                #print('Fila: ',str(contador_filas),'\tColumna: ',str(contador_columnas),'\tValor: ',y)
                                matriz.insertar(contador_filas,contador_columnas,y)
                                contador_columnas += 1
                                contador_elementos += 1
                            else:
                                continue
                        contador_columnas = 1
                        if x != '':
                            contador_filas += 1
                    contador_filas = 1

            if contador_elementos == fila*columna:
                if matrices_ortogonales.verificar_nombre(nombre):
                    print('Ya existe una matriz con este nombre')
                else:
                    print(fila, columna, contador_elementos, nombre)
                    matrices_ortogonales.insertar_simple(nombre,fila,columna,matriz)
            else:
                print('Los tamaños de la matriz no coinciden')  

    except IOError:
        print('Error al leer el archivo')

def operaciones():
    ventanaOperaciones = tkinter.Tk()
    ventanaOperaciones.title('Operaciones')
    ventanaOperaciones.resizable(1,1)
    ventanaOperaciones.geometry('880x500')

    '''frameOperaciones = tkinter.Frame(ventanaOperaciones,width='567',height='476',bg='green')
    frameOperaciones.pack()'''

    nb = ttk.Notebook(ventanaOperaciones)
    nb.pack(fill='both',expand='yes')

    p1 = ttk.Frame(nb)
    p2 = ttk.Frame(nb)
    p3 = ttk.Frame(nb)
    p4 = ttk.Frame(nb)
    p5 = ttk.Frame(nb)
    p6 = ttk.Frame(nb)
    p7 = ttk.Frame(nb)
    p8 = ttk.Frame(nb)

    #Agregrar todas las pestañas al frame
    nb.add(p1, text='Rotación horizontal')
    nb.add(p2, text='Rotación vertical')
    nb.add(p3, text='Transpuesta')
    nb.add(p4, text='Limpiar zona')
    nb.add(p5, text='Agregar linea horizontal')
    nb.add(p6, text='Agregar linea vertical')
    nb.add(p7, text='Agregar rectangulo')
    nb.add(p8, text='Agregar triangulo rectangulo')

    var1 = Entry(p1)
    var1.place(x=100,y=100)
    def obtener1():
        rotacionHorizontal(var1.get())

    var2 = Entry(p2)
    var2.place(x=100,y=100)
    def obtener2():
        rotacionVertical(var2.get())

    var3 = Entry(p3)
    var3.place(x=100,y=100)
    def obtener3():
        transpuesta(var3.get())

    Button(p1, text='Elegir matriz', command=obtener1).place(x=10,y=10)
    Button(p2, text='Elegir matriz', command=obtener2).place(x=10,y=10)
    Button(p3, text='Elegir matriz', command=obtener3).place(x=10,y=10)
    Button(p4, text='Elegir matriz', command=saludar).place(x=10,y=10)
    Button(p5, text='Elegir matriz', command=saludar).place(x=10,y=10)
    Button(p6, text='Elegir matriz', command=saludar).place(x=10,y=10)
    Button(p7, text='Elegir matriz', command=saludar).place(x=10,y=10)
    Button(p8, text='Elegir matriz', command=saludar).place(x=10,y=10)



    ventanaOperaciones.mainloop()

def reportes():
    matrices_ortogonales.mostrar_simple()


def ayuda():
    pass

#Operaciones --------------------------------------------------------------
def rotacionHorizontal(nombre_de_matriz):
    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)
    matrizAux = matriz_ortogonal()
    filas = matriz0.x
    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(filas,y+1,contenido)
        filas -= 1
    matrizAux.recorrerFilas()

def rotacionVertical(nombre_de_matriz):
    print(nombre_de_matriz)

def transpuesta(nombre_de_matriz):
    print(nombre_de_matriz)

def saludar():
    print('Hola')

#Fin operaciones ---------------------------------------------------------

root = tkinter.Tk()
root.title('Ventana Principal')
#root.geometry('1000x600')
root.resizable(0,0)

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