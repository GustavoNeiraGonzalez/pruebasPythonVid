def suma(a,b):
    
    return a+b

print(suma(4 , 3))



valor1 = 5 #variable global

def suma2():
    b = 5 #Variable local
    print(valor1 + b)

suma2()

def Persona(nombre):
    edad = 25

    print(f'Hola {nombre} tienes {edad} años')

Persona('Julia')#usar la funcion


def Amigo(nombre):
    return nombre

def MencionarAmigo(nombre):
    print(f"Hola, mi amigo es {nombre} :)")

MencionarAmigo(Amigo("David"))

MiAmigo = Amigo("David")

MencionarAmigo(MiAmigo)


