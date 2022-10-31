from arbol import (
    nodoArbol,
    insertar_nodo,
    preorden,
    inorden_villano,
    inorden_empieza_con,
    contar_heroes,
    eliminar_nodo,
    inorden,
    postorden_heroes,
    crear_bosque,
    contar_nodos,
    arbol_vacio,
    busqueda,
    descripciones,
    contar_Vencedor,
    inorden_Heracles,
    inorden_No_vencidas,
    capturadas,
    por_nivel,
    inorden_capturada,
)

# EJERCICIO 5:
# Dado un árbol con los nombre de los superhéroes y villanos de la saga Marvel Cinematic 
# Universe (MCU), desarrollar un algoritmo que contemple lo siguiente:
# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo 
# booleano que indica si es un héroe o un villano, True y False respectivamente;
#b. listar los villanos ordenados alfabéticamente;
#c. mostrar todos los superhéroes que empiezan con C;
#d. determinar cuántos superhéroes hay el árbol;
#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre;
#f. listar los superhéroes ordenados de manera descendente;
#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes 
# y otro a los villanos, luego resolver las siguiente tareas:
#I. determinar cuántos nodos tiene cada árbol;
#II. realizar un barrido ordenado alfabéticamente de cada árbol

"""
arbol = nodoArbol()
heroes = nodoArbol()
villanos = nodoArbol()


lista = [
    ['iron man', False, 1960],
    ['capiana marvel', False, 1890],
    ['thor', False, 1962],
    ['doctor strange', False, 1961],
    ['thanos', True, 1962],
    ['red skull', True, 1963],
    ['capitan america', False, 2000],
]

for nombre, villano, anio in lista:
    datos = {'villano': villano,
             'anio_aparicion': anio}
    
    insertar_nodo(arbol, nombre, datos)


# a. además del nombre del superhéroe, en cada nodo del árbol se almacenará un campo 
# booleano que indica si es un héroe o un villano, True y False respectivamente;
print ("PUNTO A")
preorden(arbol)
print()

#b. listar los villanos ordenados alfabéticamente;
print ("PUNTO B")
print(" Villanos ordenados alfabeticamente")
print()
inorden_villano(arbol)
print()

#mostrar todos los superhéroes que empiezan con C;
print("PUNTO C")
print("super Heroes que empiezan con c")
print()
inorden_empieza_con(arbol, "c")
print()

#d. determinar cuántos superhéroes hay el árbol;
print("PUNTO D")
print("Cantidad de super Heroes")
print()
print(contar_heroes(arbol))
print()


#e. Doctor Strange en realidad está mal cargado. Utilice una búsqueda por proximidad para
#encontrarlo en el árbol y modificar su nombre;
print("PUNTO E")
print()
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

#f. listar los superhéroes ordenados de manera descendente;
print("PUNTO F")
print()
postorden_heroes(arbol)
print()

#g. generar un bosque a partir de este árbol, un árbol debe contener a los superhéroes 
# y otro a los villanos, luego resolver las siguiente tareas:
#I. determinar cuántos nodos tiene cada árbol;
#II. realizar un barrido ordenado alfabéticamente de cada árbol

print("PUNTO G")
print()
crear_bosque(arbol, heroes , villanos)
print()
print("Total:" , contar_nodos(arbol), "Nodos")
print("Heroes:" , contar_nodos(heroes), "Nodos")
print("Villanos" , contar_nodos(villanos) , "Nodos")
print()
print("Arbol de Villanos\n")
preorden(villanos)
print()
print("Arbol de Heroes\n")
preorden(heroes)
print()
"""
#-------------------------------------------------------------------------------------------------

#EJERCICIO 23:
# Implementar un algoritmo que permita generar un árbol con los datos de la siguiente tabla y
# resuelva las siguientes consultas:
# a. listado inorden de las criaturas y quienes la derrotaron;
# b. se debe permitir cargar una breve descripción sobre cada criatura;
# c. mostrar toda la información de la criatura Talos;
# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
# e. listar las criaturas derrotadas por Heracles;
# f. listar las criaturas que no han sido derrotadas;
# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
# i. se debe permitir búsquedas por coincidencia;
# j. eliminar al Basilisco y a las Sirenas;
# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
# m. realizar un listado por nivel del árbol;
# n. muestre las criaturas capturadas por Heracles.

# Criaturas          Derrotado por       Criaturas         Derrotado por
#   Ceto                   -            Cerda de Cromión      Teseo
#   Tifón                 Zeus             Ortro              Heracles
#   Equidna           Argos Panoptes     Toro de Creta        Teseo
#   Dino                   -         Jabalí de Calidón      Atalanta
#   Pefredo                -             Carcinos               -
#    Enio                  -              Gerión            Heracles
#   Escila                 -               Cloto                -
#   Caribdis               -             Láquesis               -
#   Euríale                -             Átropos                -
#   Esteno                 -         Minotauro de Creta       Teseo
#   Medusa              Perseo            Harpías               -
#   Ladón               Heracles       Argos Panoptes        Hermes
# Águila del Cáucaso       -           Aves del Estínfalo       -
#   Quimera             Belerofonte         Talos               Medea
# Hidra de Lerna        Heracles          Sirenas                -
# León de Nemea         Heracles             Pitón              Apolo
# Esfinge               Edipo         Cierva de Cerinea           -
# Dragón de la Cólquida   -               Basilisco               -
# Cerbero                 -          Jabalí de Erimanto           -


arbol = nodoArbol()
arbol_vencedores = nodoArbol()

lista = [
    ['Ceto', None],               ['Tifón', 'Zeus'],                ['Equidna', 'Argos Panoptes'],
    ['Dino', None],               ['Pefredo', None],                ['Enio', None],
    ['Escila', None],             ['Caribdis', None],               ['Euríale', None],
    ['Esteno', None],             ['Medusa', 'Perseo'],             ['Ladón', 'Heracles'],
    ['Aguila del Cáucaso', None], ['Quimera', 'Belerofonte'],       ['Hidra de Lerna', 'Heracles'],
    ['León de Nemea', 'Heracles'],['Esfinge', 'Edipo'],             ['Dragón de la Cólquida', None],
    ['Cerbero', None],            ['Cerda de Cromión', 'Teseo'],    ['Ortro', 'Heracles'],
    ['Toro de Creta', 'Teseo'],   ['Jabalí de Calidón', 'Atalanta'],['Carcinos', None],
    ['Gerión', 'Heracles'],       ['Cloto', None],                  ['Láquesis', None],
    ['Atropos', None],            ['Minotauro de Creta', 'Teseo'],  ['Harpías', None],
    ['Argos Panoptes', 'Hermes'], ['Aves del Estínfalo', None],     ['Talos', 'Medea'],
    ['Sirenas', None],            ['Pitón', 'Apolo'],               ['Cierva de Cerinea', None],
    ['Basilisco', None],          ['Jabalí de Erimanto', None],
]

for criatura, vencedor in lista:
    datos = {'vencedor': vencedor}
    insertar_nodo(arbol, criatura, datos)

# a. listado inorden de las criaturas y quienes la derrotaron;
print("punto A")
print("listado inorden de las criaturas y quienes la derrotaron\n")
inorden(arbol)
print()


# b. se debe permitir cargar una breve descripción sobre cada criatura;
print()
print("Punto B")
print("se debe permitir cargar una breve descripción sobre cada criatura\n")
clave = input("ingrese como comienza la criatura a buscar: ").capitalize()
descripciones(arbol)
inorden_empieza_con(arbol, clave)
buscado = input("ingrese nombre que desea modificar: ")
pos = busqueda(arbol, buscado)
print(busqueda(arbol, buscado))
print()
descri = input("Ingresar la descripcion: ")
if pos:
    pos["datos"]["descripcion"] = descri
print()
print("La criatura quedo así:\n")
pos = busqueda(arbol, buscado)
if pos:
    print(pos["info"], pos["datos"])


# c. mostrar toda la información de la criatura Talos;
print()
print("Punto C")
print("mostrar toda la información de la criatura Talos\n")
print(busqueda(arbol, 'Talos'))
print()


# d. determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas;
print()
print("Punto D")
print("determinar los 3 héroes o dioses que derrotaron mayor cantidad de criaturas\n")
ListaVencedor=list()

def Lista_vencedor(arbol):
    if(arbol is not None):
        Lista_vencedor(arbol['izq'])
        if arbol['datos']['vencedor'] is not None:
            dato=(arbol['datos']['vencedor'])
            if dato in ListaVencedor:
                ListaVencedor.append(dato)
            else:
                ListaVencedor.append(dato)
        Lista_vencedor(arbol['der'])
        
Lista_vencedor(arbol)

for n in range(3):
    Mayor=(max(set(ListaVencedor), key= ListaVencedor.count))
    print(Mayor,contar_Vencedor(arbol,Mayor))
    for n in range(contar_Vencedor(arbol,Mayor)):
        ListaVencedor.remove(Mayor)


# e. listar las criaturas derrotadas por Heracles;
print()
print("Punto E")
print("listar las criaturas derrotadas por Heracles\n")
inorden_Heracles(arbol)


# f. listar las criaturas que no han sido derrotadas;
print()
print("Punto F")
print("listar las criaturas que no han sido derrotadas\n")
inorden_No_vencidas(arbol)


# g. además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe
# o dios que la capturo;
print()
print("Punto G")
print("Además cada nodo debe tener un campo “capturada” que almacenará el nombre del héroe o dios que la capturo\n")
capturadas(arbol)


# h. modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de
# Erimanto indicando que Heracles las atrapó;
print()
print("Punto H")
print("modifique los nodos de las criaturas Cerbero, Toro de Creta, Cierva Cerinea y Jabalí de Erimanto indicando que Heracles las atrapó\n")
pos = busqueda(arbol,"Cerbero")
if pos:
    pos["datos"]["capturada"] = "Heracles"
print(pos["info"], pos["datos"])

pos = busqueda(arbol,"Toro de Creta")
if pos:
    pos["datos"]["capturada"] = "Heracles"
print(pos["info"], pos["datos"])

pos = busqueda(arbol,"Cierva de Cerinea")
if pos:
    pos["datos"]["capturada"] = "Heracles"
print(pos["info"], pos["datos"])

pos = busqueda(arbol,"Jabalí de Erimanto")
if pos:
    pos["datos"]["capturada"] = "Heracles"
print(pos["info"], pos["datos"])

# i. se debe permitir búsquedas por coincidencia;
print()
print("Punto I")
print("Se debe permitir búsquedas por coincidencia\n")
clave = input("ingrese como comienza la criatura a buscar: ").capitalize()
inorden_empieza_con(arbol, clave)
print()


# j. eliminar al Basilisco y a las Sirenas;
print()
print("Punto J")
print("Eliminar al Basilisco y a las Sirenas\n")
print("Listado previo\n")
inorden(arbol)
eliminar_nodo(arbol, "Basilisco")
eliminar_nodo(arbol, "Sirenas")
print()
print("Nuevo Listado\n")
inorden(arbol)
print()


# k. modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles
# derroto a varias;
print()
print("Punto K")
print("Modificar el nodo que contiene a las Aves del Estínfalo, agregando que Heracles derroto a varias\n")
pos = busqueda(arbol,'Aves del Estínfalo')
if pos:
    pos['datos']['vencedor'] = 'Heracles'
print(pos)

# l. modifique el nombre de la criatura Ladón por Dragón Ladón;
print()
print("Punto L")
print("Modifique el nombre de la criatura Ladón por Dragón Ladón\n")
clave = input("ingrese parte de lo que desea buscar: ").capitalize()
inorden_empieza_con(arbol, clave)
print()
clave = input("ingrese nombre que desea modificar: ")
print()
datos_guardados=arbol["datos"]
pos = eliminar_nodo(arbol, clave)
if pos:
    name = input("ingrese nuevo nombre: ")
    insertar_nodo(arbol, name, datos_guardados)
else:
    print("valor no encontrado en el arbol")
print()
inorden(arbol)
print()

# m. realizar un listado por nivel del árbol;
print()
print("Punto M")
print("Realizar un listado por nivel del árbol\n")
por_nivel(arbol)


# n. muestre las criaturas capturadas por Heracles.
print()
print("Punto N")
print("Muestre las criaturas capturadas por Heracles\n")
inorden_capturada(arbol)
