#ejercicio 1 modificar los elementos en una lista

lista = [30,50,21,-39,0]
i=0
for x in lista:
    lista[i] = x + 1
    i=i+1
print(lista)

ListaC = ['abc', 'def', 'ghi', 'jkl']
i=0
for x in ListaC:
    ListaC[i] = x + '-p'
    i=i+1
print(ListaC)


for i in range(0,len(ListaC),2):
    ListaC[i] = "python"
print(ListaC)    
