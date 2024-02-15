


def contadorValles(cadena):
    altura = 0
    vallesCounter = 0
    bajo_nivel_mar = False
    for letra in cadena:
        if letra == 'U':
            altura += 1
        elif letra == 'D':
            altura -= 1
            if altura < 0:
                bajo_nivel_mar = True
        if altura >= 0 and bajo_nivel_mar:
            vallesCounter += 1
            bajo_nivel_mar = False
    return vallesCounter



class Nodo:
    def __init__(self, elem):
        self.elem = elem
        self.nodo_izq = None
        self.nodo_der = None

    def __str__(self):
        return str(self.elem)

    def pre_orden(self):
        result = [self.elem]
        if self.nodo_izq is not None:
            result.extend(self.nodo_izq.pre_orden())
        if self.nodo_der is not None:
            result.extend(self.nodo_der.pre_orden())
        return result

    def in_orden(self):
        result = []
        if self.nodo_izq is not None:
            result.extend(self.nodo_izq.in_orden())
        result.append(self.elem)
        if self.nodo_der is not None:
            result.extend(self.nodo_der.in_orden())
        return result

    def post_orden(self):
        result = []
        if self.nodo_izq is not None:
            result.extend(self.nodo_izq.post_orden())
        if self.nodo_der is not None:
            result.extend(self.nodo_der.post_orden())
        result.append(self.elem)
        return result


    def inserta(self, nodo):
        #el nodo insert es mayor al elem
        if self.elem < nodo.elem:
            #si el siguiente nodo derecho esta vacio, ahi lo insartamos
            if self.nodo_der is None:
                self.nodo_der = nodo
                return True
            #mandamos a llamar el nodo derecho para que haga recursion
            elif self.nodo_der is not None:
                self.nodo_der.inserta(nodo)
        elif self.elem > nodo.elem:
            if self.nodo_izq is None:
                self.nodo_izq = nodo
                return True
            elif self.nodo_izq is not None:
                self.nodo_izq.inserta(nodo)
        #Ya habia un nodo con el mismo valor
        else:
            return False

class Arbol:
    def __init__(self):
        self.raiz = None


    def inserta(self, nodo):
        if self.raiz is None:
            self.raiz = nodo
        else:
            self.raiz.inserta(nodo)

    def __str__(self):
        return str(self.raiz.pre_orden())

    def in_orden(self):
        if self.raiz is not None:
            return self.raiz.in_orden()
        else:
            return []


    def pre_orden(self):
        if self.raiz is not None:
            return self.raiz.pre_orden()
        else:
            return []

    def post_orden(self):
        if self.raiz is not None:
            return self.raiz.post_orden()
        else:
            return []




if __name__ == '__main__':

    #Pequeno Ejemplo de un arbol y sus 3 recorridos
    arbol = Arbol()
    arbol.inserta(Nodo(7))
    arbol.inserta(Nodo(5))
    arbol.inserta(Nodo(8))
    arbol.inserta(Nodo(3))
    arbol.inserta(Nodo(6))
    arbol.inserta(Nodo(9))



    print("Recorrido pre_orden:", arbol.pre_orden())
    print("Recorrido in_orden:",  arbol.in_orden())
    print("Recorrido post_orden:", arbol.post_orden())

    #Pequeno Ejemplo del problema de los valles
    print("El recorrido de valles para la entrada DDUUUUDDDUDUD es: ")
    print(contadorValles("DDUUUUDDDUDUD"))