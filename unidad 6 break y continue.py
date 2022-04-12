#instruccion break y continue

#ejemplo

i=0

while True:
    if i>=10:

        break

    print(i)
    i=i+1


#break con for

coleccion=[2,4,5,7,8,9,3,4]
for num in coleccion:
    if num == 7:
        break
    print(num)


#continue con while
#revisar!!
var=10
while var == 10:
    var=var-1
    if var==5:
        continue
    print("valor actual de var: " + str(var))


#continue en for

coleccion=[2,4,5,7,8,9,3,4]
for num in coleccion:
    if num % 2 != 0:
        continue
print(num)    
