# Miguel Cabezas
class TarjetaCredito:
    instancias = []

    def __init__(self, saldo_pagar=0, limite_credito=1000, intereses=0.05):
        self.saldo_pagar = saldo_pagar
        self.limite_credito = limite_credito
        self.intereses = intereses
        TarjetaCredito.instancias.append(self)

    def compra(self, monto):
        if self.saldo_pagar + monto > self.limite_credito:
            print("Tarjeta Rechazada, has alcanzado tu límite de crédito")
        else:
            self.saldo_pagar += monto
        return self

    def pago(self, monto):
        self.saldo_pagar -= monto
        if self.saldo_pagar < 0:
            self.saldo_pagar = 0
        return self

    def mostrar_info_tarjeta(self):
        print(f"Saldo a Pagar: ${self.saldo_pagar}")
        return self

    def cobrar_interes(self):
        self.saldo_pagar += self.saldo_pagar * self.intereses
        return self

    @classmethod
    def mostrar_todas_tarjetas(cls):
        for i, tarjeta in enumerate(cls.instancias, 1):
            print(f"Tarjeta {i}:")
            tarjeta.mostrar_info_tarjeta()

# Crear 3 tarjetas
t1 = TarjetaCredito(saldo_pagar=0, limite_credito=500, intereses=0.1)
t2 = TarjetaCredito(saldo_pagar=50, limite_credito=1000, intereses=0.05)
t3 = TarjetaCredito(saldo_pagar=0, limite_credito=200, intereses=0.2)

# Primera tarjeta: 2 compras, 1 pago, cobra intereses y muestra info (encadenado)
t1.compra(100).compra(200).pago(50).cobrar_interes().mostrar_info_tarjeta()

# Segunda tarjeta: 3 compras, 2 pagos, cobra intereses y muestra info (encadenado)
t2.compra(100).compra(200).compra(300).pago(100).pago(50).cobrar_interes().mostrar_info_tarjeta()

# Tercera tarjeta: 5 compras, excede límite, muestra info (encadenado)
t3.compra(50).compra(50).compra(50).compra(50).compra(50).mostrar_info_tarjeta()

# BONUS: Mostrar todas las tarjetas
TarjetaCredito.mostrar_todas_tarjetas()