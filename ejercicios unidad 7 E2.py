#ejercicio 2 contar vocales (cada una) en una cadena

cadena = input("ingrese una oracion: ")

vocales = ['a', 'e', 'i', 'o', 'u']

print("\nla cantidad de vocales son: ")

for i in range(len(vocales)):
    print("\t", vocales[i], " --> ", cadena.count(vocales[i]))
    
#revisar no hay letra U 
