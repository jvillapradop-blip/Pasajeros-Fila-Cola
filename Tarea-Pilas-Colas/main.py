from pasajero import Pasajero
from pila import MiPila
from cola import MiCola

pila = MiPila(10)
cola = MiCola(10)


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print("  Debe ser un número entero.")


def leer_pasajero():
    numero = leer_entero("  N.º de pasajero: ")
    nombre = input("  Nombre: ").strip()
    cedula = input("  Cédula: ").strip()
    edad = leer_entero("  Edad: ")
    fecha = input("  Fecha de vuelo (AAAA-MM-DD): ").strip()
    destino = input("  Destino: ").strip()
    asiento = input("  Asiento: ").strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def datos_prueba():
    return [
        Pasajero(1005, "Diana", "0923456789", 22, "2026-11-15", "Quito",  "12A"),
        Pasajero(1002, "Ana",   "0912345678", 28, "2026-11-15", "Lima",   "03C"),
        Pasajero(1009, "Luis",  "0987654321", 35, "2026-11-20", "Bogotá", "18F"),
        Pasajero(1004, "Beto",  "0934567890", 16, "2026-11-20", "Quito",  "07B"),
        Pasajero(1001, "Elena", "0901234567", 41, "2026-11-22", "Lima",   "01A"),
    ]


def mostrar_opciones(titulo, entrar, salir, ver):
    print(f"\n========== {titulo} ==========")
    print(f" 1. {entrar:<12}  2. Listar          3. {salir}")
    print(f" 4. {ver:<12}  5. Buscar          6. Modificar")
    print(" 7. Eliminar por número         8. Copiar")
    print(" 9. Longitud / ¿vacía?")
    print(" C. Cargar datos de prueba      0. Volver")


def menu_pila():
    while True:
        mostrar_opciones("MENÚ 1 · PILA (LIFO)", "Apilar", "Desapilar", "Ver tope")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if pila.apilar(pasajero):
                print("  Apilado: ahora es el tope")
        elif op == "2":
            pila.listar()
        elif op == "3":
            eliminado = pila.desapilar()
            if eliminado == None:
                print("  La pila está vacía")
            else:
                print(f"  Salió: {eliminado}")
                tope = pila.ver_tope()
                if tope == None:
                    print("  Nuevo tope: (pila vacía)")
                else:
                    print(f"  Nuevo tope: {tope}")
        elif op == "4":
            tope = pila.ver_tope()
            if tope == None:
                print("  (pila vacía)")
            else:
                print(f"  Tope: {tope}")
        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            pos = pila.buscar(numero)
            if pos == -1:
                print("  No existe un pasajero con ese número")
            else:
                print(f"  Encontrado en [{pos}]: {pila.datos[pos]}")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            nuevo_destino = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if pila.modificar(numero, nuevo_destino, nuevo_asiento):
                print("  Pasajero modificado correctamente")
            else:
                print("  No existe un pasajero con ese número")
        elif op == "7":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if pila.eliminar_por_numero(numero):
                print("  Pasajero eliminado")
            else:
                print("  No existe un pasajero con ese número")
        elif op == "8":
            copia = pila.copiar()
            print("  Copia de la pila:")
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {pila.longitud()}")
            if pila.esta_vacia():
                print("  Estado: está vacía")
            else:
                print("  Estado: no está vacía")
        elif op == "C":
            pruebas = datos_prueba()
            for i in range(5):
                pila.apilar(pruebas[i])
            print("  Datos de prueba apilados")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


def menu_cola():
    while True:
        mostrar_opciones("MENÚ 2 · COLA (FIFO)", "Encolar", "Desencolar", "Ver frente")
        op = input("Opción: ").strip().upper()

        if op == "1":
            pasajero = leer_pasajero()
            if cola.encolar(pasajero):
                print("  Encolado: está al final")
        elif op == "2":
            cola.listar()
        elif op == "3":
            eliminado = cola.desencolar()
            if eliminado == None:
                print("  La cola está vacía")
            else:
                print(f"  Salió: {eliminado}")
                frente = cola.ver_frente()
                if frente == None:
                    print("  Nuevo frente: (cola vacía)")
                else:
                    print(f"  Nuevo frente: {frente}")
        elif op == "4":
            frente = cola.ver_frente()
            if frente == None:
                print("  (cola vacía)")
            else:
                print(f"  Frente: {frente}")
        elif op == "5":
            numero = leer_entero("  N.º de pasajero a buscar: ")
            pos = cola.buscar(numero)
            if pos == -1:
                print("  No existe un pasajero con ese número")
            else:
                print(f"  Encontrado en [{pos}]: {cola.datos[pos]}")
        elif op == "6":
            numero = leer_entero("  N.º de pasajero a modificar: ")
            nuevo_destino = input("  Nuevo destino: ").strip()
            nuevo_asiento = input("  Nuevo asiento: ").strip().upper()
            if cola.modificar(numero, nuevo_destino, nuevo_asiento):
                print("  Pasajero modificado correctamente")
            else:
                print("  No existe un pasajero con ese número")
        elif op == "7":
            numero = leer_entero("  N.º de pasajero a eliminar: ")
            if cola.eliminar_por_numero(numero):
                print("  Pasajero eliminado")
            else:
                print("  No existe un pasajero con ese número")
        elif op == "8":
            copia = cola.copiar()
            print("  Copia de la cola:")
            copia.listar()
        elif op == "9":
            print(f"  Longitud: {cola.longitud()}")
            if cola.esta_vacia():
                print("  Estado: está vacía")
            else:
                print("  Estado: no está vacía")
        elif op == "C":
            pruebas = datos_prueba()
            for i in range(5):
                cola.encolar(pruebas[i])
            print("  Datos de prueba encolados")
        elif op == "0":
            break
        else:
            print("  Opción no válida")


def main():
    while True:
        print("\n===== Pilas y Colas · Pasajeros =====")
        print("1. Menú 1 · Pila")
        print("2. Menú 2 · Cola")
        print("3. Salir")
        op = input("Opción: ").strip()
        if op == "1":
            menu_pila()
        elif op == "2":
            menu_cola()
        elif op == "3":
            print("Hasta pronto.")
            break
        else:
            print("Opción no válida")


if __name__ == "__main__":
    main()