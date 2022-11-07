from grafo import(
    Grafo,
)



"""
g = Grafo(dirigido=False)

#Ejercicio 14:
#Implementar sobre un grafo no dirigido los algoritmos necesario para dar solución a las siguientes tareas:
# a. cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;
# b. cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la 
# distancia entre los ambientes, se debe cargar en metros;
# c. obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#para conectar todos los ambientes;
# d. determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.


# punto A: cada vértice representar un ambiente de una casa: cocina, comedor, cochera, quincho,
# baño 1, baño 2, habitación 1, habitación 2, sala de estar, terraza, patio;

g.insertar_vertice('cocina')#1
g.insertar_vertice('comedor')#2
g.insertar_vertice('cochera')#3
g.insertar_vertice('quincho')#4
g.insertar_vertice('baño 1')#5
g.insertar_vertice('baño 2')#6
g.insertar_vertice('habitación 1')#7
g.insertar_vertice('habitación 2')#8
g.insertar_vertice('sala de estar')#9
g.insertar_vertice('terraza')#10
g.insertar_vertice('patio')#11


# punto B: cargar al menos tres aristas a cada vértice, y a dos de estas cárguele cinco, el peso de la arista es la 
# distancia entre los ambientes, se debe cargar en metros;

g.insertar_arista('cocina', 'comedor', 1)
g.insertar_arista('cocina', 'baño 2', 5)
g.insertar_arista('cocina', 'habitación 1', 6)
g.insertar_arista('comedor', 'cochera', 1)
g.insertar_arista('comedor', 'quincho', 2)
g.insertar_arista('cochera', 'habitación 1', 4)
g.insertar_arista('cochera', 'habitación 2', 5)
g.insertar_arista('quincho', 'baño 1', 1)
g.insertar_arista('quincho', 'habitación 2', 4)
g.insertar_arista('baño 1', 'habitación 2', 3)
g.insertar_arista('baño 1', 'sala de estar', 4)
g.insertar_arista('baño 2', 'habitación 1', 1)
g.insertar_arista('baño 2', 'terraza', 4)
g.insertar_arista('habitación 1', 'terraza', 3)
g.insertar_arista('habitación 1', 'patio', 4)
g.insertar_arista('habitación 2', 'terraza', 2)
g.insertar_arista('habitación 2', 'sala de estar', 1)
g.insertar_arista('sala de estar', 'patio', 2)
g.insertar_arista('terraza', 'patio', 1)


#punto C: obtener el árbol de expansión mínima y determine cuantos metros de cables se necesitan
#para conectar todos los ambientes;

arbol_min = g.kruskal_minimo()

arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')
print(f"el peso total es {peso_total}")


#punto D: determinar cuál es el camino más corto desde la habitación 1 hasta la sala de estar para
#determinar cuántos metros de cable de red se necesitan para conectar el router con el Smart Tv.

print('\n# existe camino entre habitación 1 y sala de estar')
g.hay_camino('habitación 1', 'sala de estar')
('habitación 1', 'sala de estar')
print('\n# es adyacente')
print(g.es_adyacente('habitación 1', 'sala de estar'))
print('\nEl camino más corto')
resultados = g.dijkstra('habitación 1')
camino = g.camino(resultados, 'habitación 1', 'sala de estar')
print(camino)

print()
print()
"""

#------------------------------------------------------------------------------------------------------------------

#Ejercicio 15: 
#Se requiere implementar un grafo para almacenar las siete maravillas arquitectónicas modernas y naturales 
# del mundo, para lo cual se deben tener en cuenta las siguientes actividades:
# a. de cada una de las maravillas se conoce su nombre, país de ubicación (puede ser más de
#uno en las naturales) y tipo (natural o arquitectónica);
# b. cada una debe estar relacionada con las otras seis de su tipo, para lo que se debe almacenar
# la distancia que las separa;
#c. hallar el árbol de expansión mínimo de cada tipo de las maravillas;
#d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
#e. determinar si algún país tiene más de una maravilla del mismo tipo;
#f. deberá utilizar un grafo no dirigido.


        
g = Grafo(dirigido=False)

# maravillasnaturales
g.insertar_vertice('T', datos={'tipo': 'Nat', 'pais': 'egipto'})
g.insertar_vertice('Z', datos={'tipo': 'Nat', 'pais': 'francia'})
g.insertar_vertice('F', datos={'tipo': 'Nat', 'pais': 'china'})
g.insertar_vertice('X', datos={'tipo': 'Nat', 'pais': 'india'})
g.insertar_vertice('R', datos={'tipo': 'Nat', 'pais': 'eeuu'})
g.insertar_vertice('K', datos={'tipo': 'Nat', 'pais': 'brasil'})

# maravillas arquitectonicas
g.insertar_vertice('L', datos={'tipo': 'Arq', 'pais': 'argentina-brasil-paragauy'})
g.insertar_vertice('J', datos={'tipo': 'Arq', 'pais': 'indonesia'})
g.insertar_vertice('I', datos={'tipo': 'Arq', 'pais': 'sudafrica'})
g.insertar_vertice('M', datos={'tipo': 'Arq', 'pais': 'india'})
g.insertar_vertice('S', datos={'tipo': 'Arq', 'pais': 'china'})
g.insertar_vertice('Y', datos={'tipo': 'Arq', 'pais': 'brasil'})

g.insertar_arista('L', 'J', 6)
g.insertar_arista('L', 'I', 3)
g.insertar_arista('I', 'M', 8)
g.insertar_arista('M', 'S', 2)
g.insertar_arista('M', 'Y', 2)
g.insertar_arista('Y', 'I', 9)

g.insertar_arista('T', 'X', 6)
g.insertar_arista('T', 'F', 3)
g.insertar_arista('T', 'R', 8)
g.insertar_arista('F', 'X', 2)
g.insertar_arista('F', 'R', 2)
g.insertar_arista('X', 'Z', 9)
g.insertar_arista('R', 'Z', 4)
g.insertar_arista('K', 'Z', 3)
g.insertar_arista('R', 'X', 5)




print('Vertices:\n')
g.barrido_vertice()


paises = g.contar_maravillas()
for pais in paises:
    print(pais, paises[pais])


arbol_min = g.kruskal_minimo()

arbol_min = arbol_min[0].split('-')
peso_total = 0
for nodo in arbol_min:
    nodo = nodo.split(';')
    peso_total += int(nodo[2])
    print(f'{nodo[0]}-{nodo[1]}-{nodo[2]}')

print(f"el peso total es {peso_total}")



#Punto c: hallar el árbol de expansión mínimo de cada tipo de las maravillas;
arbol=g.kruskal_minimo()

for i in range(len(arbol)):
    arbol=g.kruskal_minimo()
    arbol = arbol[i].split('-')
    peso_total = 0
    for nodo in arbol:
        nodo = nodo.split(';')
        peso_total += int(nodo[2])
        print(f'{nodo[0]} - {nodo[1]} - {nodo[2]} ')
    print(f"\nLa distancia total a recorrer: {peso_total} Km ")
    print()



#Punto d: determinar si existen países que dispongan de maravillas arquitectónicas y naturales;
print('d. determinar si existen países que dispongan de maravillas arquitectónicas y naturales\n')
paises = g.contar_maravillas()
tiene_maravillas=False
for pais in paises:
    if paises[pais]['Arq']== True and paises[pais]['Nat']== True:
        print(pais,'Tiene de las 2 maravillas')
        tiene_maravillas=True
        
if tiene_maravillas==False:
    print(' No hay ')

#Punto e: determinar si algún país tiene más de una maravilla del mismo tipo;
print()
print('e. determinar si algún país tiene más de una maravilla del mismo tipo\n')
paises = g.contar_maravillas_tipo()
tiene_maravillas=False
for pais in paises:
    if paises[pais]['Arq']>1:
        print(pais, 'Tiene mas de una Maravilla Arquitectonica')
        tiene_maravillas=True
    if paises[pais]['Nat']>1:
        print(pais, 'Tiene mas de una Maravilla Natural')
        tiene_maravillas=True
        
if tiene_maravillas==False:
    print(' No hay paises con las maravillas del mismo tipo ')
    
print()