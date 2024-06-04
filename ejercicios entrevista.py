#definir una funcion maxx() que tome como argumento 2 numeros
#y devuelva el valor mayor de ellos.
#(python ya tiene una funcion max incorporada, esto es practica)

def maxx(num1, num2):
    try:
        num1 = int(num1)
        num2 = int(num2)
    except :
        return "Error, ingresar valores numericos"
    if  num1 > num2 :
        return num1
    else:
        return num2
print(maxx('a',0))
print(maxx(2,0))
print("----")
#realizar la misma funcion anterior pero con 3 valores

def max3(num1, num2,num3):
    try:
        num1 = int(num1)
        num2 = int(num2)
        num3 = int(num3)
    except :
        return "Error, ingresar valores numericos"
    
    if  num1 > num2 and num1>num3 :
        return num1
    elif num2>num3:
        return num2
    else:
        return num3
    
print(max3(7,2,3))
print(max3(1,0,4))
print(max3(1,9,4))

print("----")

#definir una funcion que calcule la longitud de una lista y de los string
#sin usar len()

def LongitudLista(lista,nombre):
    x = 0
    i = 10 #valor base, se incrementa por si la lista o string es mas alto
    while x<i:
        try:
            lista[x] #esto dará error cuando la posicion x sea mayor a la
                    #longitud de la lista por eso usamos el except (es el catch)
            #print(f"{lista[x]}")
            # - prueba de imprimir la lista

            x+=1
            i+=1
        except:
            #print("except prueba")
            # - prueba para ver si se retorna el break e imprime la longitud
            # - de la lista
            #print(x)
            break

    return (f"la longitud de {nombre} es: {x}")

array = ['a', 1 , 'XD','4']
print(LongitudLista(array,"lista"))

caracteres = "asdds} %"
print(LongitudLista(caracteres,"String"))


#crear una funcion que tome un valor, y devuelva si true si es una vocal,
# y false si no
