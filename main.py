from pasajero import Pasajero
from mi_pila import MiPila
from mi_cola import MiCola
from herramientas import leer_entero, limpiar_pantalla, pedir_cedula_valida, pedir_fecha_valida , pausar, menu

pila = MiPila(10)
cola = MiCola(10)


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = pedir_cedula_valida()
    edad = leer_entero("  Edad: ")
    fecha = pedir_fecha_valida()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    """Los 5 pasajeros de prueba en ORDEN DE LLEGADA (Diana llega primero, Elena última)."""
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]

# ---------------------- MENÚ 1 · PILA ----------------------
def menu_pila():
    limpiar_pantalla()
    opciones_pila = [
        "0. Volver",
        "1. Apilar pasajero",
        "2. Listar pasajeros",
        "3. Desapilar pasajero",
        "4. Ver tope",
        "5. Buscar por número",
        "6. Modificar pasajero",
        "7. Eliminar por número",
        "8. Copiar pila",
        "9. Longitud / ¿vacía?",
        "10. Cargar datos de prueba"
    ]

    while True:
        op = menu("MENÚ 1 · PILA (LIFO)", opciones_pila)

        if op == 1:
            limpiar_pantalla()
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print(" Apilado: ahora es el tope")
            pausar()
        elif op == 2:
            limpiar_pantalla()
            pila.listar()
            pausar()
        elif op == 3:
            limpiar_pantalla()  
            removido = pila.desapilar()
            if removido:
                print(f"  Desapilado: {removido}")
            pausar()
        elif op == 4:
            limpiar_pantalla()
            tope = pila.ver_tope()
            if tope:
                print(f"  → Tope actual: {tope}")
            pausar()
        elif op == 5:
            limpiar_pantalla()
            num = leer_entero("  Ingrese N.º de pasajero a buscar: ")
            pos = pila.buscar(num)
            if pos != -1:
                print(f"  Pasajero encontrado en la posición [{pos}]: {pila.datos[pos]}")
            else:
                print(f"  El pasajero con número {num} no existe.")
            pausar()
        elif op == 6:
            limpiar_pantalla()
            num = leer_entero("  Ingrese N.º de pasajero a modificar: ")
            n_destino = input("  Nuevo destino: ").strip()
            n_asiento = input("  Nuevo asiento: ").strip().upper()
            if pila.modificar(num, n_destino, n_asiento):
                print("  Pasajero modificado con éxito")
            pausar()
        elif op == 7:
            limpiar_pantalla()
            num = leer_entero("  Ingrese N.º de pasajero a eliminar: ")
            if pila.eliminar_por_numero(num):
                print("  Pasajero eliminado exitosamente")
            pausar()
        elif op == 8:
            limpiar_pantalla()
            copia_pila = pila.copiar()
            print("  Pila copiada con éxito. Elementos en la copia:")
            copia_pila.listar()
            pausar()
        elif op == 9:
            limpiar_pantalla()
            print(f"  → Longitud de la pila: {pila.longitud()}")
            print(f"  → ¿La pila está vacía?: {'Sí' if pila.esta_vacia() else 'No'}")
            pausar()
        elif op == 10:
            limpiar_pantalla()
            for p in datos_prueba():
                pila.apilar(p)
            print("  Datos de prueba apilados")
            pausar()
        elif op == 0:
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ 2 · COLA ----------------------
def menu_cola():
    limpiar_pantalla()
    opciones_cola = [
        "0. Volver",
        "1. Encolar pasajero",
        "2. Listar pasajeros",
        "3. Desencolar pasajero",
        "4. Ver frente",
        "5. Buscar por número",
        "6. Modificar pasajero",
        "7. Eliminar por número",
        "8. Copiar cola",
        "9. Longitud / ¿vacía?",
        "10. Cargar datos de prueba"
    ]

    while True:
        op = menu("MENÚ 2 · COLA (FIFO)", opciones_cola)

        if op == 1:
            limpiar_pantalla()
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("  Encolado: está al final")
            pausar()
        elif op == 2:
            limpiar_pantalla()
            cola.listar()
            pausar()
        elif op == 3:
            limpiar_pantalla()
            removido = cola.desencolar()
            if removido:
                print(f"  Desencolado: {removido}")
            pausar()
        elif op == 4:
            limpiar_pantalla()
            frente = cola.ver_frente()
            if frente:
                print(f"  → Frente actual: {frente}")
            pausar()
        elif op == 5:
            limpiar_pantalla()
            num = leer_entero("  Ingrese N.º de pasajero a buscar: ")
            pos = cola.buscar(num)
            if pos != -1:
                print(f" Pasajero encontrado en la posición [{pos}]: {cola.datos[pos]}")
            else:
                print(f" El pasajero con número {num} no existe.")
            pausar()
        elif op == 6:
            limpiar_pantalla()
            num = leer_entero("  Ingrese N.º de pasajero a modificar: ")
            n_destino = input("  Nuevo destino: ").strip()
            n_asiento = input("  Nuevo asiento: ").strip().upper()
            if cola.modificar(num, n_destino, n_asiento):
                print("  Pasajero modificado con éxito")
            pausar()
        elif op == 7:
            limpiar_pantalla()
            num = leer_entero("  Ingrese N.º de pasajero a eliminar: ")
            if cola.eliminar_por_numero(num):
                print("  Pasajero eliminado exitosamente")
            pausar()
        elif op == 8:
            limpiar_pantalla()
            copia_cola = cola.copiar()
            print("  Cola copiada con éxito. Elementos en la copia:")
            copia_cola.listar()
            pausar()
        elif op == 9:
            limpiar_pantalla()
            print(f"  → Longitud de la cola: {cola.longitud()}")
            print(f"  → ¿La cola está vacía?: {'Sí' if cola.esta_vacia() else 'No'}")
            pausar()
        elif op == 10:
            limpiar_pantalla()
            for p in datos_prueba():
                cola.encolar(p)
            print("  Datos de prueba encolados")
            pausar()
        elif op == 0:
            break
        else:
            print("  Opción no válida")


# ---------------------- MENÚ PRINCIPAL ----------------------
def main():
    opciones_principales = [
        "0. Salir",
        "1. Menú 1 · Pila",
        "2. Menú 2 · Cola"
    ]
    
    while True:
        limpiar_pantalla()
        op = menu("TAREA PILAS Y COLAS · PASAJEROS ✈", opciones_principales)
        if op == 1:
            menu_pila()
        elif op == 2:
            menu_cola()
        elif op == 0:
            print("¡Hasta pronto!")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()