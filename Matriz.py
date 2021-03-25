from Nodos import nodo, nodo_encabezado
from ListasEncabezados import lista_encabezado

class matriz_ortogonal:

    def __init__(self):
        self.encabezado_fila = lista_encabezado()
        self.encabezado_columna = lista_encabezado()
    
    def insertar(self, fila, columna, contenido):
        nuevo_nodo = nodo(fila, columna, contenido)

        #Insertar encabezado fila
        enc_fila = self.encabezado_fila.devolver_encabezado(fila)
        if enc_fila == None:
            enc_fila = nodo_encabezado(fila)
            enc_fila.acceso = nuevo_nodo
            self.encabezado_fila.insertar(enc_fila)
        else:
            print()
