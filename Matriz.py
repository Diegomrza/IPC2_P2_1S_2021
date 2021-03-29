from Nodos import nodo, nodo_encabezado
from ListasEncabezados import lista_encabezado

class matriz_ortogonal:
    def __init__(self):
        self.encabezado_filas = lista_encabezado()
        self.encabezado_columnas = lista_encabezado()
    
    def insertar(self, fila, columna, contenido):
        nuevo_nodo = nodo(fila, columna, contenido)
        #Insertar encabezado fila
        efila = self.encabezado_filas.devolver_encabezado(fila)
        if efila == None:
            efila = nodo_encabezado(fila)
            efila.acceso = nuevo_nodo
            self.encabezado_filas.insertar(efila)
        else:
            if nuevo_nodo.columna < efila.acceso.columna:
                nuevo_nodo.derecha = efila.acceso
                efila.acceso.izquierda = nuevo_nodo
                efila.acceso = nuevo_nodo
            else:
                aux = efila.acceso
                while aux.derecha != None:
                    if nuevo_nodo.columna < aux.derecha.columna:
                        nuevo_nodo.derecha = aux.derecha
                        aux.derecha.izquierda = nuevo_nodo
                        nuevo_nodo.izquierda = aux
                        aux.derecha = nuevo_nodo
                        break
                    aux = aux.derecha
                if aux.derecha == None:
                    aux.derecha = nuevo_nodo
                    nuevo_nodo.izquierda = aux

        #Insertar encabezado columna
        ecolumna = self.encabezado_columnas.devolver_encabezado(columna)
        if ecolumna == None:
            ecolumna = nodo_encabezado(columna)
            ecolumna.acceso = nuevo_nodo
            self.encabezado_columnas.insertar(ecolumna)
        else:
            if nuevo_nodo.fila < ecolumna.acceso.fila:
                nuevo_nodo.abajo = ecolumna.acceso
                ecolumna.acceso.arriba = nuevo_nodo
                ecolumna.acceso = nuevo_nodo
            else:
                aux = ecolumna.acceso
                while aux.derecha != None:
                    if nuevo_nodo.fila < aux.abajo.fila:
                        nuevo_nodo.abajo = aux.abajo
                        aux.abajo.arriba = nuevo_nodo
                        nuevo_nodo.arriba = aux
                        aux.abajo = nuevo_nodo
                        break
                    aux = aux.abajo
                if aux.abajo == None:
                    aux.abajo = nuevo_nodo
                    nuevo_nodo.arriba = aux


    def mostrar_ortogonal(self):
        efilas = self.encabezado_filas.primero
        while efilas != None:
            actual = efilas.acceso
            while actual != None:
                print(str(actual.columna),actual.contenido)
                actual.actual.derecha
            efilas = efilas.siguiente
