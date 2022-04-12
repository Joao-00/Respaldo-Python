#simbología: == igualdad    != diferente de    > mayor que    < menor que    >= mayor o igual    <= menor o igual
#todos los operadores tienen la misma prioridad

#operadores logicos: and (y logico), or (o logico), not (no logico).
#orden de precedencia: 1. not  2. and  3. or

#recordar: v+v = v, v+f= f, f+v = f, f+f= v.

#operadores de asignación: =, +=, -=, *=, /=, //=, %=    (sirve para el ahorro de codigo)
#dato a considerar:  +=, -=, *=, /= aumenta, disminuye, multiplica o divide la cantidad existente en una variable
#//=  division entera a una variable existente
#%=  modulo
#ejemplo   para a=3     a%=2  a=3%2  a=1 





#condicionales simples:
# if <condición>:
#       acción 1
# acción N
#el espacio de la acción 1 se denomina identación y significa que todo lo que posea este espacio está dentro del condicional

#ejemplo:
edu = "G-Talent.net"
#si (if) edu es igual a "G-Talent.net"
if edu == "G-Talent.net":
    print("Vive la experiencia!")
print("Gracias") #mensaje que se ejecutará de todos modos aún que no se cumpla la condición







#ejemplo de condicional doble

edu = "G-Talent.nett"
if edu == "G-Talent.net":
    print("Vive la experiencia!")
else:    
    print("aprovecha la oportunidad!")
print("Gracias")



#condicionales encadenados

#if <condicion>:
#   accion 1
#   accion N
#elif <condicion>:
#   accion 1
#   accion N

#ejemplo:
y=0
if y>0:
    print("Número Positivo")
elif y<0:
    print("Número Negativo")
else:
    print("Número Neutro Cero")


#condición anidada
#if <condicion>:
#   accion 1
#   accion N
#elif <condición>:
#   if<condicion>:
#       accion1
#       accion N


#ejemplo
y=7

if y>0:
    print("Numero Positivo")
    if y in range(1,10):
        print("Dentro de Rango")
    else:
        print("Fuera de Rango")
elif y<0:
    print("Número Negativo")
else:
    print("Número Neutro Cero")







