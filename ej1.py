def factorial(numero, resul=1):
    
    if numero <= 1:
        return resul
    return factorial(numero - 1, resul * numero)

print(factorial(5))

def suma(lista):
    if len(lista)==0:
        return 0
    return lista[0]+ suma(lista[1:])
numeros=[1,2,3,4,5]
print(suma(numeros))
