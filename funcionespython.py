def suma(a,b):
    
    return a+b #simple funcion de sumar 

print(suma(4 , 3)) #imprimir en consola

#----------------


valor1 = 5 #variable global

def suma2():
    b = 5 #Variable local
    print(valor1 + b)

#----------------

suma2()

def Persona(nombre):
    edad = 25

    print(f'Hola {nombre} tienes {edad} años')

Persona('Julia')#usar la funcion

#----------------

def Amigo(nombre): #funcion a usar en otra funcion
    return nombre

def MencionarAmigo(nombre):
    print(f"Hola, mi amigo es {nombre} :)")

MencionarAmigo(Amigo("David")) #se usa la funcion Amigo
                   #dentro de la funcion MencionarAmigo
#----------------

MiAmigo = Amigo("David") # variable que obtendra el valor
                #de la funcion Amigo

MencionarAmigo(MiAmigo) #uso de la variable


#----------------

