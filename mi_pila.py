from pasajero import Pasajero


class MiPila:
    """Pila (LIFO) hecha a mano sobre un arreglo de tamaño fijo.
    datos -> [fondo, ..., TOPE, None, None]
    TOPE  -> datos[cantidad - 1]  (el último que entró: el único que se ve y el único que sale)
    ⛔ Mismas prohibiciones que MiLista: sin append, pop, insert, remove, index,
       sort, reverse, copy, len(), in, slicing ni comprensiones.
    """

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def apilar(self, pasajero):                      # ✅ resuelto (= añadir de MiLista)
        if self.cantidad == self.capacidad:
            print("  ⚠ La pila está llena")
            return False
        self.datos[self.cantidad] = pasajero          # el nuevo queda encima: es el TOPE
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):                                 # ✅ EJEMPLO: del TOPE al FONDO
        if self.cantidad == 0:
            print("  (pila vacía)")
            return
        for i in range(self.cantidad - 1, -1, -1):    # cantidad-1, ..., 1, 0  (hacia atrás)
            if i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  ← TOPE")
            elif i == 0:
                print(f"  [{i}] {self.datos[i]}  ← FONDO")
            else:
                print(f"  [{i}] {self.datos[i]}")

    # ------- ✍ IMPLEMENTA (tabla 3) · recorre SIEMPRE del tope al fondo -------
    def desapilar(self):
        if self.cantidad == 0:
            print("La pila está vacía")    
            return None
        valor = self.datos[self.cantidad - 1]        # guardo el que voy a quitar
        self.datos[self.cantidad - 1] = None    # el último cajón queda vacío
        self.cantidad -= 1
        return valor

    def ver_tope(self):
        if self.cantidad == 0:
            print("La pila está vacía")
            return None
        return self.datos[self.cantidad - 1]

    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            print(numero, "no existe")
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        pila_auxiliar = MiPila(self.capacidad)
        hallado = False
        # 1. Desapilar hacia la auxiliar hasta encontrar el elemento
        while self.cantidad > 0:
            val = self.desapilar()
            if val.numero == numero:
                hallado = True  # Encontrado: se descarta (no se apila en la auxiliar)
                break
            pila_auxiliar.apilar(val)
        # 2. Restaurar los elementos desde la auxiliar a la pila original
        while pila_auxiliar.cantidad > 0:
            self.apilar(pila_auxiliar.desapilar())
        # 3. Si no se encontró, se informa
        if not hallado:
            print(numero, "no existe")
            return False
        return True

    def copiar(self):
        nueva = MiPila(self.capacidad)
        for i in range(self.cantidad):
            nueva.apilar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0