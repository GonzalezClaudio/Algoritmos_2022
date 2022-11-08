from arbol import (
    nodoArbol,
    insertar_nodo,
    preorden,
    altura,
    numeros_par_imp,
    inorden_empieza_con,
    eliminar_nodo,
    inorden,
    postorden,
    crear_bosque,
    contar_nodos,
    arbol_vacio,
    busqueda,
    descripciones,
    por_nivel,
    inorden_altura,
    inorden_peso,
)

#Gonzalez Claudio

# 1 - Desarrollar un algoritmo que permita implementar un árbol como índice para hacer consultas de 
# personajes de la saga de Star Wars, de los cuales se sabe su nombre, altura y peso. 
# Además deberá contemplar los siguientes requerimientos (debe cargar al menos 20 personajes):
# a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
# b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker
# c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;
# d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;
# e. mostrar un listado por nivel de los personajes del árbol;
# f. determinar si Grogu esta en el árbol y responder lo siguiente:
# mostrar toda su información;
# en que tipo de nodo esta (hoja, intermedio o raíz);
# que altura tiene el nodo dentro del árbol.


arbol = nodoArbol()


lista = [
    ['iron man', 0.5, 40],
    ['luke skywalker', 10, 80],
    ['thor', 2, 6],
    ['mandalorian', 10, 40],
    ['thanos', 20, 5],
    ['red skull', 25, 90],
    ['capitan america', 3, 25],
    ['yoda', 5, 20],
    ['grogu' , 0.4 , 95],
    ['ceto' , 0.3 , 20],
    ['dino' , 2 , 5],
    ['gerion' , 86 , 0],
    ['basilisco' , 0.2 , 95],

]

for nombre, altura, peso in lista:
    datos = {'altura': altura,
             'peso': peso}
    
    insertar_nodo(arbol, nombre, datos)

inorden(arbol)

# a. se debe poder cargar un nuevo personaje, modificarlo (cualquiera de sus campos) y darlo de baja;
"""
clave = input('ingrese parte de lo que desea buscar: ')
inorden_empieza_con(arbol, clave)
print()
clave = input('ingrese nombre que desea modificar: ')
print()
datos_guardados=arbol['datos']
pos = eliminar_nodo(arbol, clave)
if pos:
    name = input('ingrese nuevo nombre: ')
    insertar_nodo(arbol, name, datos_guardados)
else:
    print('valor no encontrado en el arbol')
print()
inorden(arbol)
print()
"""

# b. mostrar toda la información de Yoda, Mandalorian y Luke Skywalker

print()
print("Punto b")
print("mostrar toda la información de yoda\n")
print(busqueda(arbol, 'yoda'))
print()
print("mostrar toda la información de mandalorian\n")
print(busqueda(arbol, 'mandalorian'))
print()
print("mostrar toda la información de luke skywalker\n")
print(busqueda(arbol, 'luke skywalker'))
print()


# c. mostrar un listado ordenado alfabéticamente de los personajes que miden menos de 0.9 metro;

print()
print("Punto E")
print("listar con altura menor a 0.9\n")
inorden_altura(arbol)

# d. mostrar un listado ordenado alfabéticamente de los personajes que pesan mas de 75 kilos;

print()
print("Punto E")
print("listar con peso mas de 75 kilos\n")
inorden_peso(arbol)

# e. mostrar un listado por nivel de los personajes del árbol;

print()
print("barrido por nivel")
por_nivel(arbol)

# f. determinar si Grogu esta en el árbol y responder lo siguiente:
# mostrar toda su información;
# en que tipo de nodo esta (hoja, intermedio o raíz);
# que altura tiene el nodo dentro del árbol.

print()
print("informacion de grogu\n")
clave = 'grogu'
pos=busqueda(arbol,clave)
if pos:
    print("se encuentra el personaje",clave)
else:
    print("El personaje" , clave , "No se encuentra en el arbol")

print(busqueda(arbol,clave))



