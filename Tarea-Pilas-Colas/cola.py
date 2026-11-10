from pasajero import Pasajero


class MiCola:

    def __init__(self, capacidad=10):
        self.datos = [None] * capacidad
        self.capacidad = capacidad
        self.cantidad = 0

    def encolar(self, pasajero):
        if self.cantidad == self.capacidad:
            print("  La cola está llena")
            return False
        if self.buscar(pasajero.numero) != -1:
            print("  Ya existe un pasajero con ese número")
            return False
        self.datos[self.cantidad] = pasajero
        self.cantidad = self.cantidad + 1
        return True

    def listar(self):
        if self.cantidad == 0:
            print("  (cola vacía)")
            return
        for i in range(self.cantidad):
            if i == 0:
                print(f"  [{i}] {self.datos[i]}  FRENTE")
            elif i == self.cantidad - 1:
                print(f"  [{i}] {self.datos[i]}  FINAL")
            else:
                print(f"  [{i}] {self.datos[i]}")

    def desencolar(self):
        if self.cantidad == 0:
            return None
        aux = self.datos[0]
        for i in range(self.cantidad):
            if i < self.cantidad - 1:
                self.datos[i] = self.datos[i + 1]
            else:
                self.datos[i] = None
        self.cantidad = self.cantidad - 1
        return aux

    def ver_frente(self):
        if self.cantidad == 0:
            return None
        return self.datos[0]

    def buscar(self, numero):
        for i in range(self.cantidad):
            if self.datos[i].numero == numero:
                return i
        return -1

    def modificar(self, numero, nuevo_destino, nuevo_asiento):
        pos = self.buscar(numero)
        if pos == -1:
            return False
        self.datos[pos].destino = nuevo_destino
        self.datos[pos].asiento = nuevo_asiento
        return True

    def eliminar_por_numero(self, numero):
        encontrado = False
        for i in range(self.cantidad):
            p = self.desencolar()
            if p.numero == numero and encontrado == False:
                encontrado = True
            else:
                self.encolar(p)
        return encontrado

    def copiar(self):
        nueva = MiCola(self.capacidad)
        for i in range(self.cantidad):
            nueva.encolar(self.datos[i])
        return nueva

    def longitud(self):
        return self.cantidad

    def esta_vacia(self):
        return self.cantidad == 0