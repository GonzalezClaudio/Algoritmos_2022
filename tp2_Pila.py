from pila import Pila
from random import randint

#Ejercicio 19:
#Dada una pila de películas de las que se conoce su título, estudio cinematográfico 
# y año de estreno, desarrollar las funciones necesarias para resolver las siguientes 
# actividades:
# a. mostrar los nombre películas estrenadas en el año 2014;
# b. indicar cuántas películas se estrenaron en el año 2018;
# c. mostrar las películas de Marvel Studios estrenadas en el año 2016.

class  Pelicula ( object ):
     

    def  __init__ ( self , titulo , estudio , estreno ):
        self.titulo  =  titulo
        self.estudio  =  estudio
        self.estreno  =  estreno

    def  __str__ ( self ):
        return self.titulo + '-' + self . estudio + '-' + self . estreno

pila = Pila()
pila_aux = Pila()
cont_2018 = 0

pelicula = Pelicula ('Mark III', 'Vengadores I', "2018")
pila.apilar (pelicula)
pelicula = Pelicula ('iron man I', 'Marvel', "2016")
pila.apilar (pelicula)
pelicula = Pelicula ('Avengers1', 'Marvel', "2014")
pila.apilar (pelicula)
pelicula = Pelicula ('Spider-Man', 'Pixar', "2018")
pila.apilar (pelicula)
pelicula = Pelicula ('Capitan America', 'Pixar', "2014")
pila.apilar (pelicula)


while (not pila.pila_vacia()):
    x=pila.desapilar()
    #punto A
    if (x.estreno== "2014"):
        print("las peliculas estrenada en el año 2014 son: ",  x.titulo)
    #punto B
    if (x.estreno=="2018"):
        cont_2018 += 1
        
    #punto c
    if (x.estreno=="2016" and x.estudio=="Marvel"):
        print("estudios estrenado en el 2016 , por Marvel" , x.titulo)
    else:
        pila_aux.apilar(x)

print("cantidad de peliculas estrenadas en el 2018:" , cont_2018)

#-------------------------------------------------------------------------------------------

#Ejercicio 24:
#Dada una pila de personajes de Marvel Cinematic Universe (MCU), de los cuales 
# se dispone de su nombre y la cantidad de películas de la saga en la que participó, 
# implementar las funciones necesarias para resolver las siguientes actividades:
# a. determinar en qué posición se encuentran Rocket Raccoon y Groot, tomando 
# como posición uno la cima de la pila;
# b. determinar los personajes que participaron en más de 5 películas de la saga, 
# además indicar la cantidad de películas en la que aparece;
# c. determinar en cuantas películas participo la Viuda Negra (Black Widow);
# d. mostrar todos los personajes cuyos nombre empiezan con C, D y G

class  Pelicula ( object ):
     

    def  __init__ ( self , titulo , personaje , cantidad ):
        self.titulo  =  titulo
        self.personaje  =  personaje
        self.cantidad = cantidad
    

    def  __str__ ( self ):
        return self.titulo + '-' + self . personaje + "-" + self . cantidad

pila = Pila()
pila_aux = Pila()


   

pelicula = Pelicula ('Mark III', "cviuda negra" , "6")
pila.apilar (pelicula)
pelicula = Pelicula ('iron man I', 'capitan america' , "3")
pila.apilar (pelicula)
pelicula = Pelicula ('Avengers1', 'groot' , "7")
pila.apilar (pelicula)
pelicula = Pelicula ('Spider-Man','Rocket Raccoon' , "4")
pila.apilar (pelicula)
pelicula = Pelicula ('Capitan America', 'diron man', "3")
pila.apilar (pelicula)

cont= 0
cont1=0
cont2=0

while (not pila.pila_vacia()):
    x=pila.desapilar()
    cont += 1
    #punto A
    if (x.personaje == "Rocket Raccoon"):
        cont1=cont
    if (x.personaje=='groot'):
        cont2=cont
    #punto b
    if (x.cantidad >= "5"):
        print("el personaje " , x.personaje , "participo en " , x.cantidad , "peliculas")
    #punto c
    if (x.personaje=="viuda negra"):
        print("cantidad de peliculas que participo la viuda negra" , x.cantidad)
    #punto d
    if(x.personaje[0]=="c"):
        print ("personajes que empiezan con c" , x.personaje)
    if(x.personaje[0]=="d"):
        print ("personajes que empiezan con d" , x.personaje)
    if(x.personaje[0]=="g"):
        print ("personajes que empiezan con g" , x.personaje)
    pila_aux.apilar(x)


print("posicion de Rocket Raccon" , cont1)
print("posicion de Groot" , cont2)
