from cola import Cola
from random import randint

# Ejercicio 18:
# Dada una cola con los códigos de turnos de atención (con el formato #@@@, donde # es una
#letra de la A hasta la F y “@@@” son tres dígitos desde el 000 al 999), desarrollar 
# un algoritmo que resuelva las siguientes situaciones:
# a. cargar 1000 turnos de manera aleatoria a la cola.
# b. separar la cola con datos en dos colas, cola_1 con los turnos que empiezan 
# con la letra A, C y F, y la cola_2 con el resto de los turnos (B, D y E).
# c. determinar cuál de las colas tiene mayor cantidad de turnos, y de esta cuál 
# de las letras tiene mayor cantidad.
# d. mostrar los turnos de la cola con menor cantidad de elementos, cuyo número 
# de turno sea mayor que 506.
    
c = Cola()
c1 = Cola()
c2 = Cola()
c1aux= Cola()
c2aux=Cola()
contadorTurno1=0
contadorTurno2=0
A=0
B=0
C=0
D=0
E=0
F=0

print("cola original")
#punto A
for i in range(10):
    dato = (chr(randint(65, 70)) , randint(000,999))
    c.arribo(dato)
    print(dato)
    

# punto b        
while(not c.cola_vacia()):
    x = c.atencion()
    if (x[0]=="A" or x[0]=="C" or x[0]=="F"):
        c1.arribo(x)
    else:
        c2.arribo(x)
        


#punto c 
print("cola 1")   
while (not c1.cola_vacia()):
    x=c1.atencion()
    print(x)
    contadorTurno1 += 1
    if (x[1]>506):
        c1aux.arribo(x)
    if(x[0]=="A"):
        A += 1
    else:
        if(x[0]=="C"):
            C +=1
        else:
            F +=1
    
    
print("cola 2")
while (not c2.cola_vacia()):
    x=c2.atencion()
    print(x)
    contadorTurno2 +=1
    if(x[1]>506):
        c2aux.arribo(x)
    if(x[0]=="B"):
        B += 1
    else:
        if(x[0]=="D"):
            D +=1
        else:
            E +=1


if (contadorTurno1 > contadorTurno2):
    print("")
    print("la cola 1 es de mayor tamaño")
    if (A > C and A > F):
        print("la letra con mas cantidad es la A")
    else:
        if (C > F and C > A):
            print("la letra con mas cantidad es la C")
        else:
            print("la letra con mas cantidad es la F")
else:
    print("")
    print("la cola 2 es de mayor tamaño")
    if (B > D and B > E):
        print("la letra con mas cantidad es la B")
    else:
        if (D > B and D > E):
            print("la letra con mas cantidad es la D")
        else:
            print("la letra con mas cantidad es la E")

#Punto d
if (contadorTurno1 > contadorTurno2):
    while (not c2aux.cola_vacia()):
        x=c2aux.atencion()
        print("")
        print("cola menor 2: con turno mayor a 506")
        print(x)
else:
    while (not c1aux.cola_vacia()):
        x=c1aux.atencion()
        print("")
        print("cola menor 1: con turno mayor a 506")
        print(x)

#------------------------------------------------------------------------------------------

#Ejercicio 22:
# Se tienen una cola con personajes de Marvel Cinematic Universe (MCU), 
# de los cuales se conoce el nombre del personaje, el nombre del superhéroe y 
# su género (Masculino M y Femenino F) –por ejemplo {Tony Stark, Iron Man, M}, 
# {Steve Rogers, Capitán América, M}, {Natasha Romanoff, Black Widow, F}, etc., 
# desarrollar un algoritmo que resuelva las siguientes actividades:
# a. determinar el nombre del personaje de la superhéroe Capitana Marvel;
# b. mostrar los nombre de los superhéroes femeninos;
# c. mostrar los nombres de los personajes masculinos;
# d. determinar el nombre del superhéroe del personaje Scott Lang;
# e. mostrar todos datos de los superhéroes o personaje cuyos nombres comienzan
#    con la letra S;
# f. determinar si el personaje Carol Danvers se encuentra en la cola e indicar su nombre
#    de superhéroes.

class  Personajes ( object ):
     

    def  __init__ ( self , NombrePersonaje , NombreHeroe , Genero ):
        self.NombrePersonaje  =  NombrePersonaje 
        self.NombreHeroe  =  NombreHeroe
        self.Genero  =  Genero

    def  __str__ ( self ):
        return self.NombrePersonaje  + '-' + self . NombreHeroe + '-' + self . Genero
    
C = Cola()
CFemenino=Cola()
CMasculino=Cola()


personajes = Personajes ("Tony Stark", "Iron Man", "M")
C.arribo (personajes)
personajes = Personajes ("Steve Rogers", "Capitán América", "M")
C.arribo (personajes)
personajes = Personajes ("Natasha Romanoff", "Black Widow", "F")
C.arribo (personajes)
personajes = Personajes ("Carol Danvers","Capitana Marvel" , "F")
C.arribo (personajes)
personajes = Personajes ("AntMan","Scott Lang" ,"M" )
C.arribo (personajes)

while(not C.cola_vacia()):
    x=C.atencion()
    #Punto A
    if (x.NombreHeroe == "Capitana Marvel"):
        print()
        print("Nombre de la capitana Marvel:" , x.NombrePersonaje)
        
    #Punto B
    if (x.Genero=="F"):
        CFemenino.arribo(x)
    #Punto C
    if (x.Genero=="M"):
        CMasculino.arribo(x)
    #Punto D
    if (x.NombreHeroe == "Scott Lang"):
        print("Nombre de Scott Lang:" , x.NombrePersonaje)
        print("")
    #Punto E
    if (x.NombrePersonaje[0] == "S" or x.NombreHeroe[0] == "S"):
        print("Datos de personajes que comienzan con S")
        print(x)
        print()
    #Punto F
    if (x.NombrePersonaje == "Carol Danvers"):
        print()
        print("La personaje Carol Danvers se encuentra en la cola")
        print("su nombre de super heroe es: " , x.NombreHeroe)
        

#punto B
print("Personajes femeninos")
while(not CFemenino.cola_vacia()):
    x=CFemenino.atencion()
    print(x.NombrePersonaje)
    
#Punto C
print("")
print("Personajes masculinos")
while(not CMasculino.cola_vacia()):
    x=CMasculino.atencion()
    print(x.NombrePersonaje)
