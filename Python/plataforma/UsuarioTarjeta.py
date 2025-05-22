# miguel cabezas
class TarjetaCredito:
    def __init__(self):
        self.saldo_pagar = 0

    def compra(self, monto):
        self.saldo_pagar += monto

    def pagar(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0
            

class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjeta = TarjetaCredito()

    def hacer_compra(self, monto):
        self.tarjeta.compra(monto)
        return self

    def pagar_tarjeta(self, monto):
        self.tarjeta.pagar(monto)
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre}, Saldo a pagar: {self.tarjeta.saldo_pagar}")

# BONUS: Usuario con múltiples tarjetas
class UsuarioMultipleTarjetas:
    def __init__(self, nombre):
        self.nombre = nombre
        self.tarjetas = {}

    def agregar_tarjeta(self, nombre_tarjeta):
        self.tarjetas[nombre_tarjeta] = TarjetaCredito()

    def hacer_compra(self, monto, nombre_tarjeta):
        if nombre_tarjeta in self.tarjetas:
            self.tarjetas[nombre_tarjeta].compra(monto)
        else:
            print("Tarjeta no encontrada.")
        return self

    def pagar_tarjeta(self, monto, nombre_tarjeta):
        if nombre_tarjeta in self.tarjetas:
            self.tarjetas[nombre_tarjeta].pagar(monto)
        else:
            print("Tarjeta no encontrada.")
        return self

    def mostrar_saldo_usuario(self):
        print(f"Usuario: {self.nombre}")
        for nombre, tarjeta in self.tarjetas.items():
            print(f"  Tarjeta {nombre}: Saldo a pagar: {tarjeta.saldo_pagar}")

if __name__ == "__main__":
    print("Seleccione el tipo de usuario:")
    print("1. Usuario con una tarjeta")
    print("2. Usuario con múltiples tarjetas")
    tipo = input("Opción (1/2): ")

    if tipo == "1":
        nombre = input("Ingrese el nombre del usuario: ")
        usuario = Usuario(nombre)
        while True:
            print("\nOpciones:")
            print("1. Hacer compra")
            print("2. Pagar tarjeta")
            print("3. Mostrar saldo")
            print("4. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                monto = float(input("Ingrese el monto de la compra: "))
                usuario.hacer_compra(monto)
            elif opcion == "2":
                monto = float(input("Ingrese el monto a pagar: "))
                usuario.pagar_tarjeta(monto)
            elif opcion == "3":
                usuario.mostrar_saldo_usuario()
            elif opcion == "4":
                break
            else:
                print("Opción no válida.")
    elif tipo == "2":
        nombre = input("Ingrese el nombre del usuario: ")
        usuario = UsuarioMultipleTarjetas(nombre)
        while True:
            print("\nOpciones:")
            print("1. Agregar tarjeta")
            print("2. Hacer compra")
            print("3. Pagar tarjeta")
            print("4. Mostrar saldos")
            print("5. Salir")
            opcion = input("Seleccione una opción: ")
            if opcion == "1":
                nombre_tarjeta = input("Nombre de la nueva tarjeta: ")
                usuario.agregar_tarjeta(nombre_tarjeta)
            elif opcion == "2":
                nombre_tarjeta = input("Nombre de la tarjeta: ")
                monto = float(input("Ingrese el monto de la compra: "))
                usuario.hacer_compra(monto, nombre_tarjeta)
            elif opcion == "3":
                nombre_tarjeta = input("Nombre de la tarjeta: ")
                monto = float(input("Ingrese el monto a pagar: "))
                usuario.pagar_tarjeta(monto, nombre_tarjeta)
            elif opcion == "4":
                usuario.mostrar_saldo_usuario()
            elif opcion == "5":
                break
            else:
                print("Opción no válida.")
    else:
        print("Tipo de usuario no válido.")

