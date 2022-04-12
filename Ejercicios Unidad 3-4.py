#ejercicio 1
#numero par o impar

#ejemplo del uso de módulo(%)  6 % 2 = 0 (el cero significa el residuo)


numero = int(input("Introduzca un número: "))

if numero % 2 == 0:
    print ("El numero", numero, "es PAR")
else:
    print("El numero", numero, "es IMPAR")


#ejercicio 2
#determinar el mayor de 3 numeros dados


num1 = int(input("Ingrese el primer numero entero: "))
num2 = int(input("Ingrese el segundo numero entero: "))
num3 = int(input("Ingrese el tercer numero entero: "))

if num1 != num2 and num2 != num3 and num1 != num3:
        if num1 > num2 and num1 > num3:
            print("de {}, {}, {} el mayor es {}".format(num1,num2,num3,num1))
        elif num2 > num1 and num2 > num3:
            print("de {}, {}, {} el mayor es {}".format(num1,num2,num3,num2))
        else:
            print("de {}, {}, {} el mayor es {}".format(num1,num2,num3,num3))
else:
    print("Existen 2 o mas numeros iguales, por lo tanto no hay numero mayor")



#ejercicio 3
#comprobar vocales mayusculas o minusculas


letra = input("Indique una vocal: ")
if letra == 'a' or letra == 'e' or letra == 'i' or letra == 'o' or letra == 'u':
    print("la letra", letra, "es vocal y minuscula")
elif letra == 'A' or letra == 'E' or letra == 'I' or letra == 'O' or letra == 'U':
    print("la letra", letra, "es vocal y mayuscula")
else:
    print("la letra", letra, "es una consonante")


#ejercicio 4
#calculadora aritmetica

#con las 4 operaciones basicas 


print("*** Calculadora Aritmetica ***")

print("Operaciones que puede realizar: \" +, -, *, /\"")
operacion = input("Seleccione la operacion: ")
x = int(input("Ingrese un valor entero: "))
y = int(input("Ingrese otro valor entero: "))
if operacion == '+':
    print("La suma es: ", x+y)
elif operacion == '-':
    print("La resta es: ", x-y)
elif operacion == '*':
    print("La multiplicacion es: ", x*y)
else:
    if y != 0 and y<=x:
        print("La division es: ", x/y)
    else:
        print("La operacion no se puede realizar, el divisor es 0")





    
