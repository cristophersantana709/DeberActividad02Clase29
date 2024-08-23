
saldo = 1000.0  
historial = [] 
pin = "1234"

def consultar_saldo():
    """Esta función muestra el saldo actual en la cuenta."""
    global saldo  
    print(f"Tu saldo actual es: ${saldo:.2f}")
    
def depositar_dinero():
    """Esta función permite al usuario depositar dinero en su cuenta."""
    global saldo  
    cantidad = float(input("Ingresa la cantidad a depositar: $"))
    if cantidad > 0:
        saldo += cantidad
        historial.append(f"Depósito: +${cantidad:.2f}")
        print(f"Has depositado: ${cantidad:.2f}")
    else:
        print("La cantidad a depositar debe ser positiva.")
        
def retirar_dinero():
    """Esta función permite al usuario retirar dinero de su cuenta."""
    global saldo  
    cantidad = float(input("Ingresa la cantidad a retirar: $"))
    if 0 < cantidad <= saldo:
        saldo -= cantidad
        historial.append(f"Retiro: -${cantidad:.2f}")
        print(f"Has retirado: ${cantidad:.2f}")
    elif cantidad > saldo:
        print("No tienes suficiente saldo para retirar esa cantidad.")
    else:
        print("La cantidad a retirar debe ser positiva.")
        
def ver_historial():
    """Esta función muestra el historial de transacciones realizadas."""
    if historial:
        print("Historial de transacciones:")
        for transaccion in historial:
            print(transaccion)
    else:
        print("No hay transacciones realizadas.")

def cambiar_pin():
    """Esta función permite al usuario cambiar el PIN de la cuenta."""
    global pin
    pin_ingresado = input("Ingresa tu PIN actual: ")
    if pin_ingresado == pin:
        nuevo_pin = input("Ingresa el nuevo PIN: ")
        confirmacion_pin = input("Confirma el nuevo PIN: ")
        if nuevo_pin == confirmacion_pin:
            pin = nuevo_pin
            print("El PIN ha sido cambiado exitosamente.")
        else:
            print("Los PINs no coinciden. Intenta nuevamente.")
    else:
        print("El PIN actual ingresado es incorrecto.")

        
def menu():
    """Esta función muestra el menú principal y maneja las opciones del usuario."""
    while True:  
        print("\nBienvenido al Cajero Automático")
        print("1. Consultar Saldo")
        print("2. Depositar Dinero")
        print("3. Retirar Dinero")
        print("4. Ver Historial de Transacciones")
        print("5. Cambiar de pin")
        print("6. Salir")
        
        opcion = input("Elige una opción: ")
        if opcion == "1":
            consultar_saldo()
        elif opcion == "2":
            depositar_dinero()
        elif opcion == "3":
            retirar_dinero()
        elif opcion == "4":
            ver_historial()
        elif opcion == "5":
            cambiar_pin()
        elif opcion == "6":
            print("Gracias por usar el Cajero Automático. ¡Hasta luego!")
            break  
        else:
            print("Opción inválida, por favor elige nuevamente.")
            
menu() 