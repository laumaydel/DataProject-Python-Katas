# 36. Crea la clase UsuarioBanco ,representa a un usuario de un banco con su nombre, saldo y si tiene o no cuenta
# corriente. Proporciona métodos para realizar operaciones como retirar dinero, transferir dinero desde otro usuario 
# y agregar dinero al saldo.

class UsuarioBanco:
    def __init__(self, nombre, saldo, cuenta_corriente=True):
        self.nombre = nombre
        self.saldo = saldo
        self.cuenta_corriente = cuenta_corriente

    def agregar_dinero(self, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad a agregar debe ser mayor a cero.")
        self.saldo += cantidad
        print(f"{self.nombre} ha ingresado {cantidad} €. Saldo actual: {self.saldo} €")

    def retirar_dinero(self, cantidad):
        if cantidad > self.saldo:
            raise ValueError(f" Operación cancelada: {self.nombre} saldo insuficiente ({self.saldo}€) para retirar {cantidad}€.")
        self.saldo -= cantidad
        print(f"{self.nombre} ha retirado {cantidad}€. Saldo restante: {self.saldo}€")

    def transferir_dinero(self, destino, cantidad):
        # Transfiere dinero DESDE 'destino' HACIA el usuario actual ('self')
        if cantidad > destino.saldo:
            raise ValueError(f"Transferencia fallida: {destino.nombre} no tiene saldo suficiente para transferir {cantidad}€.")
        destino.saldo -= cantidad
        self.saldo += cantidad
        print(f"Transferencia de {cantidad}€ realizada de {destino.nombre} a {self.nombre}.")


#EJEMPLOS
# 1.Crear dos usuarios: "Alicia" con saldo inicial de 100 y "Bob" con saldo inicial de 50, ambos con cuenta corriente.
alicia = UsuarioBanco("Alicia", 100, True)
bob = UsuarioBanco("Bob", 50, True)

# 2. Agregar 20 unidades de saldo de "Bob".
bob.agregar_dinero(20)  # Saldo de Bob pasa a 70

# 3.  Hacer una transferencia de 80 unidades desde "Bob" a "Alicia".
try:
    alicia.transferir_dinero(bob, 80) #Sobre Alicia para seguir la lógica
except ValueError as e:
    print(f"Error detectado: {e}")

# 4. Retirar 50 unidades de saldo a "Alicia".
alicia.retirar_dinero(50)  # Saldo de Alicia pasa de 100 a 50