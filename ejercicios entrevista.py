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

print("--- letras ----")

#crear una funcion que tome un valor, y devuelva si true si es una letra,
# y false si no

def LetraFalseTrue(a):
    a=str(a)
    if not len(a) == 1:
        return "no ingresar mas de 1 caracter"

    if 'a' <= a <= 'z' or 'A' <= a <= 'Z':
        return True
    else:
        return False
        
vocal = 23
print (f"se espera error longitud:  {LetraFalseTrue(vocal)}")


vocal = "2"
print (f"se espera valor False:  {LetraFalseTrue(vocal)}")
vocal = "t"
print (f"se espera valor True:  {LetraFalseTrue(vocal)}")
print("--- vocales ---")

#la misma funcion pero con vocales

def VocalFalseTrue(a):
    a=str(a)
    if not len(a) == 1:
        return "no ingresar mas de 1 caracter"

    if a in 'aeiou':
        return True
    else:
        return False
        
vocal = 23
print (f"se espera error longitud:  {VocalFalseTrue(vocal)}")


vocal = "b"
print (f"se espera valor False:  {VocalFalseTrue(vocal)}")
vocal = "a"
print (f"se espera valor True:  {VocalFalseTrue(vocal)}")


#crear una funcion sumar() y multip() que sumen y multipliquen los
#elementos de una lista

def sumar(lista):
    x = 0
    total = 0
    i = 10 #valor base, se incrementa por si la lista o string es mas alto
    while x<i:
        try:
            int(lista[x])
            total += lista[x]
            x+=1
            i+=1
        except ValueError:
            return "Error, no ingresar caracteres string"
            #maneja error al encontrar un caracter no numerico al convertir a int
        except:
            break
    return total

array = [7, 1 , 2,4]
print("valor esperado 14: ",sumar(array))

print("--- sumar ---")

def multiplicar(lista):
    x = 0
    total = 1
    i = 10 #valor base, se incrementa por si la lista o string es mas alto
    while x<i:
        try:
            int(lista[x])
            total *= lista[x]
            x+=1
            i+=1
        except ValueError:
            return "Error, no ingresar caracteres string"
            #maneja error al encontrar un caracter no numerico al convertir a int
        except:
            break
    return total


array2 = [1,2,3,4,7]
print("valor esperado 168 :",multiplicar(array2))

print("--- multiplicar --")


# Definir una funcion que invierta una cadena de caracteres

def invertirString(cadena):
    x = 0
    stringVolteado = ""
    i = 10 #valor base, se incrementa por si la lista o string es mas alto
    while x<i:
        try:
            print(cadena[x])
            str(cadena[x])
            x+=1
            i+=1
        except ValueError:
            return "Error, no ingresar valores numericos"
            #maneja error al encontrar un caracter numerico 
        except:
            break
            #
    while x>-0: #esta vez 0 para el limite de posicion de caracteres del string
        try:    #(numeros negativos van al final de la lista y te lo devuelve)

            x-=1#-1 desde inicio para evitar errores de posicion

            str(cadena[x])   

            stringVolteado += cadena[x]
        except:
            print('break')

            break
            #
    return stringVolteado

cadena2 = "hola mundo"
print(invertirString(cadena2))
print("---")

# definir una funcion que reconozca una funcion EsPalindromo()
# (palindromo son palabras que se escriben igual al reves y normal ej: radar)


# definir una funcion superPosicion() que tome 2 listas y si algun elemento
# entre las listas es igual, devolver true, si no, false. usar bucle for anidado

