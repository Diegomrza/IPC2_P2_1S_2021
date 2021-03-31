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

    #Rotacion Horizontal -------------------
    var1 = Entry(p1)
    var1.place(x=100,y=15)
    def obtener1():
        rotacionHorizontal(var1.get())

    #Rotacion Vertical ---------------------
    var2 = Entry(p2)
    var2.place(x=100,y=15)
    def obtener2():
        rotacionVertical(var2.get())

    #Transpuesta ---------------------------
    var3 = Entry(p3)
    var3.place(x=100,y=15)
    def obtener3():
        transpuesta(var3.get())

    #Limpiar Zona --------------------------
    var4 = Entry(p4)
    var4.place(x=100,y=15)

    Label(p4, text='Fila inicio').place(x=400,y=15)
    varLimp0 = Entry(p4)
    varLimp0.place(x=250,y=15)

    Label(p4, text='Columna inicio').place(x=400,y=45)
    varLimp1 = Entry(p4)
    varLimp1.place(x=250,y=45)

    Label(p4, text='Fila final').place(x=400,y=75)
    varLimp2 = Entry(p4)
    varLimp2.place(x=250,y=75)

    Label(p4, text='Columna final').place(x=400,y=105)
    varLimp3 = Entry(p4)
    varLimp3.place(x=250,y=105)


    def obtener4():
        limpiar_zona(var4.get(), varLimp0.get(), varLimp1.get(), varLimp2.get(), varLimp3.get())

    #Agregar linea horizontal --------------
    var5 = Entry(p5)
    var5.place(x=100,y=15)

    Label(p5,text='x').place(x=375,y=14)
    varLH0 = Entry(p5)
    varLH0.place(x=250,y=15)

    Label(p5, text='y').place(x=375,y=39)
    varLH1 = Entry(p5)
    varLH1.place(x=250,y=40)

    Label(p5, text='Elementos').place(x=375,y=64)
    varLH2 = Entry(p5)
    varLH2.place(x=250,y=65)

    def obtener5():
        agregar_linea_horizontal(var5.get(), varLH0.get(), varLH1.get(), varLH2.get())

    #Agregar linea vertical ----------------
    var6 = Entry(p6)
    var6.place(x=100,y=15)

    Label(p6,text='x').place(x=375,y=14)
    varLV0 = Entry(p6)
    varLV0.place(x=250,y=15)

    Label(p6, text='y').place(x=375,y=39)
    varLV1 = Entry(p6)
    varLV1.place(x=250,y=40)

    Label(p6, text='Elementos').place(x=375,y=64)
    varLV2 = Entry(p6)
    varLV2.place(x=250,y=65)

    def obtener6():
        agregar_linea_vertical(var6.get(), varLV0.get(), varLV1.get(), varLV2.get())

    #Agregar Rectangulo ---------------------
    var7 = Entry(p7)
    var7.place(x=100,y=15)

    Label(p7, text='x').place(x=400,y=15)
    varRec0 = Entry(p7)
    varRec0.place(x=250,y=15)

    Label(p7, text='y').place(x=400,y=45)
    varRec1 = Entry(p7)
    varRec1.place(x=250,y=45)

    Label(p7, text='Filas').place(x=400,y=75)
    varRec2 = Entry(p7)
    varRec2.place(x=250,y=75)

    Label(p7, text='Columnas').place(x=400,y=105)
    varRec3 = Entry(p7)
    varRec3.place(x=250,y=105)

    def obtener7():
        agregar_rectangulo(var7.get(),varRec0.get(), varRec1.get(),varRec2.get(),varRec3.get())

    #Agregar triangulo rectangulo ----------
    var8 = Entry(p8)
    var8.place(x=100,y=15)

    Label(p8, text='x').place(x=400,y=15)
    varT0 = Entry(p8)
    varT0.place(x=250,y=15)

    Label(p8, text='y').place(x=400,y=45)
    varT1 = Entry(p8)
    varT1.place(x=250,y=45)

    Label(p8, text='Filas').place(x=400,y=75)
    varT2 = Entry(p8)
    varT2.place(x=250,y=75)

    Label(p8, text='Columnas').place(x=400,y=105)
    varT3 = Entry(p8)
    varT3.place(x=250,y=105)

    def obtener8():
        agregar_triangulo_rectangulo(var8.get(), varT0.get(), varT1.get(), varT2.get(), varT3.get())


    Button(p1, text='Elegir matriz', command=obtener1).place(x=10,y=10)
    Button(p2, text='Elegir matriz', command=obtener2).place(x=10,y=10)
    Button(p3, text='Elegir matriz', command=obtener3).place(x=10,y=10)
    Button(p4, text='Elegir matriz', command=obtener4).place(x=10,y=10)
    Button(p5, text='Elegir matriz', command=obtener5).place(x=10,y=10)
    Button(p6, text='Elegir matriz', command=obtener6).place(x=10,y=10)
    Button(p7, text='Elegir matriz', command=obtener7).place(x=10,y=10)
    Button(p8, text='Elegir matriz', command=obtener8).place(x=10,y=10)

    ventanaOperaciones.mainloop()

def reportes():
    matrices_ortogonales.mostrar_simple()

def ayuda():
    pass

#Operaciones --------------------------------------------------------------

def rotacionHorizontal(nombre_de_matriz):
    print('Rotacion Horizontal')
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
    print('Rotacion Vertical')
    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)
    matrizAux = matriz_ortogonal()

    columnas = matriz0.y
    print('Las filas de la matriz0 son: ', columnas)
    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar(x+1,columnas,contenido)
            columnas -= 1
        columnas = matriz0.y

    matrizAux.recorrerFilas()

def transpuesta(nombre_de_matriz):
    print('Transpuesta')
    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar(y+1,x+1,contenido)

    matrizAux.recorrerFilas()

def limpiar_zona(nombre_de_matriz, filaA, columnaA, filaB, columnaB):
    
    fila0 = int(filaA)
    columna0 = int(columnaA)
    fila1 = int(filaB)
    columna1 = int(columnaB)

    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(x+1,y+1,contenido)

    for x in range(fila0,fila1+1):
        print('X: ',x)
        for y in range(columna0,columna1+1):
            print('Y: ',y)
            matrizAux.reemplazar_valor(x,y,'-')

    matrizAux.recorrerFilas()

def agregar_linea_horizontal(nombre_de_matriz, x, y, elemento):

    fila = int(x)
    columna = int(y)
    columna1 = columna + int(elemento)-1
    

    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(x+1,y+1,contenido)

    for x in range(0,1):
        print('X: ',x)
        for y in range(columna,columna1+1):
            print('Y: ',y)
            matrizAux.reemplazar_valor(fila,y,'*')

    matrizAux.recorrerFilas()

def agregar_linea_vertical(nombre_de_matriz, x, y, elemento):

    fila = int(x)
    columna = int(y)
    columna1 = columna + int(elemento)-1
    
    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(x+1,y+1,contenido)

    for x in range(fila,columna1):
        print('X: ',x)
        for y in range(0,1):
            print('Y: ',y)
            matrizAux.reemplazar_valor(x,columna,'*')

    matrizAux.recorrerFilas()

def agregar_rectangulo(nombre_de_matriz, x, y, fila, columna):
    fila0 = int(x)
    columna0 = int(y)

    fila1 = fila0+(int(fila)-1)
    columna1 = columna0+(int(columna)-1)

    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(x+1,y+1,contenido)

    for x in range(fila0,fila1+1):
        #print('X: ',x)
        for y in range(columna0,columna1+1):
            #print('Y: ',y)
            matrizAux.reemplazar_valor(x,y,'*')

    matrizAux.recorrerFilas()

def agregar_triangulo_rectangulo(nombre_de_matriz, x, y, fila, columna):

    Finicio = int(x) 
    Cinicio = int(y)

    filas = Finicio + int(fila)-1
    columnas = Cinicio + int(columna)-1

    matriz0 = matrices_ortogonales.mostrar_elemento(nombre_de_matriz)
    print(matriz0.nombre)

    matrizAux = matriz_ortogonal()

    for x in range(0,matriz0.x):
        for y in range(0,matriz0.y):
            contenido = matriz0.matriz.mostrar_uni(x+1,y+1)
            matrizAux.insertar_como_vengan(x+1,y+1,contenido)
    pos = 1
    for x in range(Finicio, filas+1):
        print('X: ',x)
        for y in range(Cinicio,Cinicio+pos):
            print('Y: ',y)
            matrizAux.reemplazar_valor(x, y, '*')
        pos += 1
        
    matrizAux.recorrerFilas()
            
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