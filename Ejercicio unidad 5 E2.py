#Ejercicio 2
#operaciones de conjuntos con listas

a = [1,2,4] 

b = [1,2,3,5]

#union -> conjunto con los elementos del conjunto A y del conjunto B sin elementos repetidos

aub = list(a)
for ele in b:
    if not ele in aub:
        aub.append(ele)

print("union ->", sorted(aub))

#interseccion -> conjunto con los elementos comunes en ambos conjuntos

ainterb = []

for ele in b:
    if ele in a:
        ainterb.append(ele)

print("interseccion ->", sorted(ainterb))

#diferencia -> A - B, conjunto con los elementos de A que no esten en B

adifb = list(a)

for ele in b:
    if ele in adifb:
        adifb.remove(ele)

print("diferencia ->", sorted(adifb))

#diferencia simetrica -> conjunto con elementos de A que no esten en B y viceversa

adifsb = list()
for ele in a:
    if not ele in b:
        adifsb.append(ele)

for ele in b:
    if not ele in a:
        adifsb.append(ele)
        
print("diferencia Simetrica ->", sorted(adifsb))

#super conjunto -> se verifica si A contiene a B
super = True

for ele in b:
    if not ele in a:
        super = False
        break
if super:
    print("Super conjunto")
else:
    print("No super conjunto")
    
#subconjunto -> se verifica si A esta contenido en B
sub = True

for ele in a:
    if not ele in b:
        sub = False
        break
if sub:
    print("Subconjunto")
else:
    print("No subconjunto")

#disjuntos -> se verifica que los elementos de ambos conjuntos sean diferentes
disJ = True
for ele in a:
    if not ele in b:
        disJ = False
        break
if disJ:
    print("Disjuntos")
else:
    print("No disjuntos")


