class Cuenta:
    def __init__(self, numero_cuenta, pin, saldo=0):
        self.__numero_cuenta = numero_cuenta
        self.__pin = pin
        self.__saldo = saldo

    def autenticar_pin(self, pin):
        return self.__pin == pin

    def depositar(self, cantidad):
        self.__saldo += cantidad

    def retirar(self, cantidad):
        if self.__saldo >= cantidad:
            self.__saldo -= cantidad
            return True
        else:
            return False

    def mostrar_saldo(self):
        return self.__saldo

    def transferir(self, cuenta_destino, cantidad):
        if self.retirar(cantidad):
            cuenta_destino.depositar(cantidad)
            return True
        else:
            return False

    def obtener_numero_cuenta(self):
        return self.__numero_cuenta


class Banco:
    def __init__(self):
        self.__cuentas = {}

    def agregar_cuenta(self, cuenta):
        self.__cuentas[cuenta.obtener_numero_cuenta()] = cuenta

    def obtener_cuenta(self, numero_cuenta):
        return self.__cuentas.get(numero_cuenta)

    def obtener_cuentas(self):
        return self.__cuentas


class Cajeroautomatico:
    def __init__(self, banco):
        self.__banco = banco
        self.__cuenta_actual = None
        # Inicializamos el inventario con un total de 100 millones
        self.__inventario = {
            100000: 999,  # 10 billetes de $100,000
            50000: 200,   # 20 billetes de $50,000
            20000: 500,   # 50 billetes de $20,000
            10000: 100   # 100 billetes de $10,000
        }

    def autenticar_usuario(self, numero_cuenta, pin):
        cuenta = self.__banco.obtener_cuenta(numero_cuenta)
        if cuenta and cuenta.autenticar_pin(pin):
            self.__cuenta_actual = cuenta
            return True
        else:
            return False

    def mostrar_menu(self):
        if self.__cuenta_actual:
            print("1. Consultar Saldo")
            print("2. Depositar")
            print("3. Retirar")
            print("4. Transferir")
            print("5. Salir")
            opcion = input("Elija una opcion: ")
            return opcion
        else:
            print("No hay usuario autenticado")
            return None

    def depositar(self, cantidad):
        if self.__cuenta_actual:
            self.__cuenta_actual.depositar(cantidad)
            print(f"Se han depositado ${cantidad}.")

    def retirar(self, cantidad):
        if self.__cuenta_actual:
            if self.__cuenta_actual.retirar(cantidad):
                print(f"Se han retirado ${cantidad}.")
            else:
                print("Fondos insuficientes.")

    def consultar_saldo(self):
        if self.__cuenta_actual:
            saldo = self.__cuenta_actual.mostrar_saldo()
            print(f"Su saldo es ${saldo}.")

    def transferir(self, numero_cuenta_destino, cantidad):
        if self.__cuenta_actual:
            cuenta_destino = self.__banco.obtener_cuenta(numero_cuenta_destino)
            if cuenta_destino:
                if self.__cuenta_actual.transferir(cuenta_destino, cantidad):
                    print(f"Se han transferido ${cantidad}.")
                else:
                    print("Fondos insuficientes.")
            else:
                print("Cuenta destino no encontrada.")

    def mostrar_inventario(self):
        print("Inventario del cajero:")
        for billete, cantidad in sorted(self.__inventario.items(), reverse=True):
            print(f"${billete}: {cantidad} billetes")
        total = sum(b * c for b, c in self.__inventario.items())
        print(f"\nTotal disponible en el cajero: ${total}")

    def realizar_retiro_admin(self, monto):
        billetes_entregados = {}
        monto_original = monto
        for billete in sorted(self.__inventario.keys(), reverse=True):
            if monto <= 0:
                break
            cantidad_disponible = self.__inventario[billete]
            cantidad_necesaria = monto // billete
            cantidad_a_dar = min(cantidad_disponible, cantidad_necesaria)
            if cantidad_a_dar > 0:
                billetes_entregados[billete] = cantidad_a_dar
                monto -= billete * cantidad_a_dar

        if monto == 0:
            for b, cantidad in billetes_entregados.items():
                self.__inventario[b] -= cantidad
            print(f"Se entregó: {billetes_entregados}")
        else:
            print(f"No se puede entregar ${monto_original} con los billetes disponibles.")

    def realizar_retiro_usuario(self, monto):
        billetes_entregados = {}
        monto_original = monto
        for billete in sorted(self.__inventario.keys(), reverse=True):
            if monto <= 0:
                break
            cantidad_disponible = self.__inventario[billete]
            cantidad_necesaria = monto // billete
            cantidad_a_dar = min(cantidad_disponible, cantidad_necesaria)
            if cantidad_a_dar > 0:
                billetes_entregados[billete] = cantidad_a_dar
                monto -= billete * cantidad_a_dar

        if monto == 0:
            for b, cantidad in billetes_entregados.items():
                self.__inventario[b] -= cantidad
            print(f"Se entregó: {billetes_entregados}")
            return True
        else:
            print(f"No se puede entregar ${monto_original} con los billetes disponibles.")
            return False


# Función para gestionar el login
def login(cajero):
    while True:
        print("\n=== Bienvenido al Cajero Automático ===")
        print("1. Ingresar como Usuario")
        print("2. Ingresar como Administrador")
        print("3. Salir")
        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            numero_cuenta = int(input("Ingrese el número de cuenta: "))
            pin = int(input("Ingrese el PIN: "))
            if cajero.autenticar_usuario(numero_cuenta, pin):
                while True:
                    opcion_usuario = cajero.mostrar_menu()
                    if opcion_usuario == "1":
                        cajero.consultar_saldo()
                    elif opcion_usuario == "2":
                        cantidad = float(input("Ingrese la cantidad a depositar: "))
                        cajero.depositar(cantidad)
                    elif opcion_usuario == "3":
                        cantidad = float(input("Ingrese la cantidad a retirar: "))
                        if not cajero.realizar_retiro_usuario(cantidad):
                            print("No se pudo realizar el retiro.")
                    elif opcion_usuario == "4":
                        numero_cuenta_destino = int(input("Ingrese el numero de cuenta destino: "))
                        cantidad = float(input("Ingrese la cantidad a transferir: "))
                        cajero.transferir(numero_cuenta_destino, cantidad)
                    elif opcion_usuario == "5":
                        print("Sesión cerrada.")
                        break
                    else:
                        print("Opción no válida. Intente de nuevo.")
            else:
                print("Autenticación fallida.")
        elif opcion == "2":
            contrasena_admin = input("Ingrese la contraseña de administrador: ")
            if contrasena_admin == "admin123":
                while True:
                    print("\n--- Panel de Administrador ---")
                    print("1. Ver inventario completo")
                    print("2. Realizar un retiro de dinero")
                    print("3. Salir")
                    opcion_admin = input("Seleccione una opción: ")
                    if opcion_admin == "1":
                        cajero.mostrar_inventario()
                    elif opcion_admin == "2":
                        monto = float(input("Ingrese el monto a retirar: "))
                        cajero.realizar_retiro_admin(monto)
                    elif opcion_admin == "3":
                        print("Saliendo del panel de administrador.")
                        break
                    else:
                        print("Opción inválida.")
            else:
                print("Contraseña incorrecta.")
        elif opcion == "3":
            print("Gracias por usar el sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intente nuevamente.")


# Crear un banco y agregar cuentas
banco = Banco()
banco.agregar_cuenta(Cuenta(numero_cuenta=1234, pin=5678, saldo=500000))
banco.agregar_cuenta(Cuenta(numero_cuenta=5678, pin=1234, saldo=300000))
banco.agregar_cuenta(Cuenta(numero_cuenta=1111, pin=0000, saldo=700000))
banco.agregar_cuenta(Cuenta(numero_cuenta=3334, pin=2222, saldo=1000000))

# Crear un cajero automático
cajero = Cajeroautomatico(banco)

# Iniciar sesión
login(cajero)
