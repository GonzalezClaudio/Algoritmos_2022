from grafo import(
    Grafo,
    
)

#PARCIAL: GONZALEZ CLAUDIO
#2 - Dado un grafo no dirigido con personajes de la saga Star Wars, implementar los algoritmos 
# necesarios para resolver las siguientes tareas:
# a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de 
# episodios en los que aparecieron juntos ambos personajes que se relacionan;
#b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;
#c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
#d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, 
# Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;
#e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.

g = Grafo(dirigido=False)

# a. cada vértice debe almacenar el nombre de un personaje, las aristas representan la cantidad de 
# episodios en los que aparecieron juntos ambos personajes que se relacionan;

g.insertar_vertice('ceto')
g.insertar_vertice('dino')
g.insertar_vertice('gerion')
g.insertar_vertice('atropos')
g.insertar_vertice('sirenas')
g.insertar_vertice('piton')
g.insertar_vertice('quimera')
g.insertar_vertice('esteno')
g.insertar_vertice('tifon')
g.insertar_vertice('cloto')
g.insertar_vertice('medusa')
g.insertar_vertice('c-3po')
g.insertar_vertice('yoda')
g.insertar_vertice('leila')


g.insertar_arista('ceto', 'dino', 1)
g.insertar_arista('ceto', 'gerion', 5)
g.insertar_arista('gerion', 'atropos', 6)
g.insertar_arista('atropos', 'sirenas', 1)
g.insertar_arista('atropos', 'piton', 2)
g.insertar_arista('piton', 'quimera', 4)
g.insertar_arista('quimera', 'esteno', 5)
g.insertar_arista('esteno', 'tifon', 1)
g.insertar_arista('esteno', 'cloto', 4)
g.insertar_arista('cloto', 'medusa', 3)
g.insertar_arista('medusa', 'c-3po', 4)
g.insertar_arista('medusa', 'yoda', 3)
g.insertar_arista('yoda', 'leila', 8)
g.insertar_arista('leila', 'luke skywalker', 1)
g.insertar_arista('luke skywalker', 'yoda', 1)


g.barrido_lista_lista()
#b. hallar el árbol de expansión mínimo desde el vértice que contiene a C-3PO, Yoda y la princesa Leia;
arbol=g.kruskal_minimo()

for i in range(len(arbol)):
    arbol=g.kruskal_minimo()
    arbol = arbol[i].split('-')
    peso_total = 0
    for nodo in arbol:
        nodo = nodo.split(';')
        peso_total += int(nodo[2])
        print(f'{nodo[0]} - {nodo[1]} - {nodo[2]} ')
        print(f"\nLos Episodios son: {peso_total} ")
        print()



#c. determinar cuales personajes comparten con otro dos episodios o mas (mostrar el par de pesonajes);
print("c")




#d. cargue al menos los siguientes personajes: Luke Skywalker, Darth Vader, Yoda, Boba Fett, C-3PO, Leia, 
# Rey, Kylo Ren, Chewbacca, Han Solo, R2-D2, Obi-Wan kenobi; BB-8;
g.insertar_vertice('luke skywalker')
g.insertar_vertice('darth vader')
g.insertar_vertice('boba fett')
g.insertar_vertice('rey')
g.insertar_vertice('kylo ren')
g.insertar_vertice('chewbacca')
g.insertar_vertice('han solo')
g.insertar_vertice('R2-D2')
g.insertar_vertice('obi-wan')
g.insertar_vertice('bb-8')

#e. determinar que personaje es el que a compartido episodio con la mayor cantidad del resto de los personajes.