#argumentos por referencia o valor

#ejemplo

def incrementa(a):
    a+=1
    return a

a = 1
b = incrementa(a)

print("a: ", a)
print("b: ", b)
