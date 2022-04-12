#ejercicio 5
#cajero automatico

#con 5 opciones: consulta de saldo disponible, extraer dinero, depositar dinero,
#transferencias y la opción de salir.

#siempre tiene que dar el saldo disponible desde un principio

print("-----------------------------------------------")        

from random import randrange
saldo = randrange(0,5000000)

print("Bienvenido al cajero automatico")
print()
print("Opciones disponibles: ")
print("1. Consulta de saldo disponible")
print("2. Extraer dinero")
print("3. Depositar dinero")
print("4. Transferencias")
print("0. Salir")

opcion = int(input("Seleccione la opcion: "))


if opcion in range(5):
    if opcion == 0:
        print("Hasta luego...")
    elif opcion == 1:
        print("Su saldo disponible es: ", saldo)
    elif opcion == 2: 
        print("Su saldo disponible es: ", saldo)
        monto = int(input("Indique monto a retirar: "))
        if monto > saldo:
            print("Saldo no disponible")
        else:
            saldo = saldo - monto
            print("se a retirado con exito su dinero")
            print("su saldo actual es: ", saldo)
    elif opcion == 3:
        print("Su saldo disponible es: ", saldo)
        monto = int(input("Indique el monto a depositar: "))
        saldo = saldo + monto
        print("Su saldo actual es: ", saldo)
    else:
        cuenta = input("Indique el numero de cuenta a transferir: ")
        print("Su saldo disponible es: ", saldo)
        monto = int(input("Indique el monto a transferir: "))
        if monto > saldo:
            print("La operacion no se ejecuto por saldo insuficiente")
        else:
            print("Transferencia realizada con exito")
            saldo = saldo - monto
            print("Su saldo actual es: ", saldo)
else:
    print("Opcion invalida... vuelva mañana")
