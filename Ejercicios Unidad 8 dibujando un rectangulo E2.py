# ejercicio 2 dibujar un rectangulo


def esp_ast(nspace, nasterisco):
    print(nspace*" ",nasterisco*"*")


def rectangulo(base, altura):
    for x in range(0, altura):
        esp_ast(base+altura, base)


def principal():
    base = int(input("Indique la base del rectangulo: "))
    altura = int(input("Indique la altura del rectangulo: "))
    print()
    if base > 0 and altura > 0 and base != altura:
        rectangulo(base, altura)
    else:
        if base == altura:
            print("La base y la altura deben ser diferentes")
        else:
            print("La base y la altura deben ser positivas")

principal()
            
