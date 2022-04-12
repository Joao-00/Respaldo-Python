#cadena de caracteres

#sintaxis
#id_Variable="conjunto de caracteres"
#>>> linea = "programacion"

#id_variable = """Conjunto
#                       de
#                         caracteres"""


#resaltar palabras

text = "Que bonito es \"Programar\""
print(text)

#\n > salto de linea o linea nueva

esc = 'Programando \n en \n \'python\''
print(esc)

#\t > tabulador

Esc = "Programando \t en \t \'python\'"
print(Esc)

# \'texto\' > comillas simples
# \"texto\" > comillas dobles


#para que no se interprete el \n como tal usar raw string
s = r'C:\python\noticias'
print(s)

se='C:\python\noticias' #muestra de error
print(se)


#operaciones con cadenas
#acceso a caracteres especificos de la cadena a traves de [], desde posicion 0
x = 'programando en python'

print('x[0] = ',x[0])


#concatenar 2 o mas cadenas, a traves de operador + o dos cadenas escritas una al lado de la otra o con ()

cad1 = 'Programando en ...'
cad2 = 'Python'
cadR = cad1 + cad2
print(cadR)

#comprobando existencia de sub-cadena en una cadena a traves de in

print('a' in cadR)
print('bn' in cadR)
print('hon' in cadR)

#repetir una cadena usando el operador *

cadR = (cad1 + cad2 * 3)
print(cadR)


#funciones
#len(): funcion que devuelve la longitud de una cadena

len(cadR)

#str(): convierte el argumento dado en cadena

str(len(cadR))
