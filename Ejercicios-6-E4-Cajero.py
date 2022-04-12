#cajero automatico con menu interactivo

from random import randrange

saldo = randrage(0,5000000)

print("***** Bienvenidos al cajero automatico *****")


while true:
    print("\nOperaciones disponibles")
    print("\n1. Saldo")
    print("\n2. Retiro")
    print("\n3. Deposito")
    print("\n0. Salir")

    opcion = int(input("Elija operacion a realizar entre 0 y 3: "))
    if opcion in range(4):
        if opcion == 1:
            print("Su saldo es: ", saldo)
        elif opcion == 2:
            monto = int(input("Indique el monto a retirar: "))
            if monto > saldo:
                print("Operacion invalida, saldo insuficiente...")
            else:
                saldo = saldo - monto
                print("Operacion exitosa...")
                print("Su saldo actual es: ", saldo)
        elif opcion == 3:
            monto = int(input("Indique el monto a depositar: "))
            saldo = saldo + monto
            print("Su saldo actual es: ", saldo)
        else:
            print("Hasta luego...")
            break
    else:
        print("la opcion seleccionada no esta disponible...")
        
        
                
