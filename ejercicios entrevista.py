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

def EsPalindromo(palabra):
    palindromo = ""
    bucle = len(palabra)
    reverso = bucle-1 # -1 por el valor inicial de palabra que parte en 0
    for i in range (bucle):
        palindromo += palabra[reverso]
        reverso += -1
        
    if palindromo == palabra:
        return (f"{palindromo} es palindromo")
    else:
        return (f"{palindromo} NO es palindromo")

palabra = "radar"
print(EsPalindromo(palabra))
palabra = "hola"
print(EsPalindromo(palabra))
    
# definir una funcion superPosicion() que tome 2 listas y si algun elemento
# entre las listas es igual, devolver true, si no, false. usar bucle for anidado

def superPosicion(x,y):
    bucleX = len(x)
    bucleY = len(y)
    for i in range(bucleX): #2 for para recorrer las listas, y comparar todos
                            #los items con todos los items de las listas
        for b in range(bucleY):
            if (x[i] == y[b]):
                return True
    return False #si no encuentra ninguna similitud, dara false

listaA = ['a','b',1,2,3]
listaB = ['s','g',4,5,3]
print(superPosicion(listaA,listaB))

print('-------')
#definir una funcion GenerarNCaracteres() que tome un numero y un caracter,
#entonces devolver ese caracter por el numero de veces (5,x = xxxxx)

def GenerarNCaracteres(x,caracter):
    try:
        int(x)
        str(caracter)#try except para verificar que los datos sean validos
    except:
        return ("error, ingresar un numero y un caracter, en ese orden")
    mult = caracter * x #simplemente multiplicar el string por el numero
    print(mult)
    
print(GenerarNCaracteres(4,'p'))
print('-------')

#definir un histograma procedicimiento() que tome una lista de numeros e
#imprima el histograma,
#ej: (4,2,6)
# ....
# ..
# ......

def procedimiento(*numeros): #con *numeros convertiras los valores en un array
                             # por lo que no estas limitado a una cantidad fija
    for i in range (len(numeros)):
        try:
            int(numeros[i])
        except:
            return print(f"error en item posicion {i+1}, ingresar",
                         "unicamente numeros")
        print(f"{'.'*numeros[i]}") #multiplicar el string . por la cantidad
        
procedimiento(1,2,3,'p')
print('-------')


# Escribe una función fizz_buzz que tome un número n y devuelva una
#lista de números del 1 a n.
# Para múltiplos de tres, añade "Fizz" en lugar del número y para los
#múltiplos de cinco, añade "Buzz".
# Para números que son múltiplos de ambos tres y cinco, añade "FizzBuzz".

mult = 6
def fizz_buzz(n):
    for i in range (n): # n es el rango a imprimir
        if (i+1) % 3 == 0:  # verifica si es divisible entre 3
            print("fizz")
        elif (i+1) % 5 == 0: # i+1 por el ciclo empieza en 0
            print("buzz")
        else:
            print(i+1)
            
fizz_buzz(15)
print ("------")
# Escribe una función comprimir_cadena que tome una cadena y devuelva una
# versión comprimida de la cadena.
# La cadena comprimida debe usar el formato de contar las letras consecutivas,
# por ejemplo, "aaabbbccc" se convierte en "a3b3c3".
# Si la cadena comprimida no es más corta que la cadena original,
# devuelve la cadena original.

def comprimirCadena(cadena):
    comprimido = ""
    charConsecutivo = ""
    charCount = 0
    for i in range (len(cadena)):
        #print(f"{cadena[i]} + {charConsecutivo}")

        #idea resolver de alguna forma el que no tome los otros ifs
        #haciendo una verificacion con el numero de ciclo

        if cadena[i] == charConsecutivo: #aqui para ver letras consecutivas
            charCount +=1
            #-------------
        elif i == 0:    # este elif verifica SOLO el primer ciclo si hay
                        # caracteres consecutivos, entonces devolver el valor
                        # correcto si es asi, y si no, tambien contemplarlo
            if cadena[i]==cadena[i+1]:#i+1 para saber el valor siguiente
                charConsecutivo = cadena[i]
                charCount +=1
            else:
                comprimido += cadena[i] # devolver caracter normal
                charCount = 0
                charConsecutivo = cadena[i]

            #--------------
        elif charCount != 0:#aqui si charcount no es 0 es decir hubo caract
                            # consecutivos. pero no cumple el primer if
                                # asi que se devuelve lo comprimido
            comprimido += charConsecutivo + str(charCount)
            charCount = 0
            charConsecutivo = cadena[i]

        else:

            #aqui necesito hacer otro if para verificar que la siguiente vuelta
            #del for no me salte la primera verificacion de caracter consecutivo
            comprimido += cadena[i] # devolver caracter normal
            charCount = 0
            charConsecutivo = cadena[i]


    print(comprimido)
comprimirCadena("aaabbccddd")
#por algun motivo no s e

        
        
    

