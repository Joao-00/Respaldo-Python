#ejercicio 3 menu para clientes

global diccClien
diccClien = {}

def buscarCliente():
    print("Buscar Cliente")
    idC = input("Ingrese Identificacion: ")
    if diccClien.get(idC,0) == 0:
        print("Cliente no registrado")
    else:
        print(idC,diccClien[idC])

    

def listarCliente():
    print("Listado Clientes")
    print("Identificador    Nombre")
    for id, cli in diccClien.items():
        print("{}              {}".format(id,cli))

def registrarCliente():
    print("Registrar Cliente")
    idClient = input("Ingrese su identificacion: ")
    nombreClient = input("Ingrese Nombre: ")
    diccClien[idClient]= nombreClient


def opciones():
    print("\n")
    msg = "Gestor de clientes"
    print(msg)
    print("-" * len(msg))
    opcmen = {1: "Registrar clientes", 2: "Listar clientes", 3: "Buscar cliente", 4: "Salir"}
    for op, opm in opcmen.items():
        print("{}. {}".format(op,opm))


def menu():
    op = 0

    while op != 4:
        opciones()
        op = int(input("Indique su opcion[1..4] -> "))
        if op in range(1,5):
            if op == 1:
                registrarCliente()
            elif op == 2:
                listarCliente()
            elif op == 3:
                buscarCliente()
            else:
                print("... bye")
        else:
            print("opcion no valida")

menu()            
                
