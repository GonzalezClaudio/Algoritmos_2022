from lista import Lista
from random import randint , choice

# Ejercicio 15:
# Se cuenta con una lista de entrenadores Pokémon. De cada uno de estos se conoce: 
# nombre, cantidad de torneos ganados, cantidad de batallas perdidas y 
# cantidad de batallas ganadas. Y además la lista de sus Pokémons, de los cuales se sabe: 
# nombre, nivel, tipo y subtipo. Se pide resolver las siguientes actividades 
# utilizando lista de lista implementando las funciones necesarias:
# a. obtener la cantidad de Pokémons de un determinado entrenador;
# b. listar los entrenadores que hayan ganado más de tres torneos;
# c. el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
# d. mostrar todos los datos de un entrenador y sus Pokémos;
# e. mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
# f. los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador 
# (tipo y subtipo);
# g. el promedio de nivel de los Pokémons de un determinado entrenador;
# h. determinar cuántos entrenadores tienen a un determinado Pokémon;
# i. mostrar los entrenadores que tienen Pokémons repetidos;
# j. determinar los entrenadores que tengan uno de los siguientes Pokémons: 
# Tyrantrum, Terrakion o Wingull;
# k. determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

#class Entrenador:

#    def __init__(self, nombre, torneos_ganados, batallas_perdidas, batallas_ganadas):
#        self.nombre = nombre
#        self.torneos_ganados = torneos_ganados
#        self.batallas_ganadas = batallas_ganadas
#        self.batallas_perdidas = batallas_perdidas
    
#    def __str__(self):
#        return self.nombre

#class Pokemon:

#    def __init__(self, nombre, nivel, tipo, subtipo):
#        self.nombre = nombre
#        self.nivel = nivel
#        self.tipo = tipo
#        self.subtipo = subtipo

#    def __str__(self):
#        return f"{self.nombre} - {self.nivel}"

#lista_entrenadores = Lista()

#enternadores = [
#    {'name': 'uno', 'tg': 15, 'bg': 45,  'bp': 11},
#    {'name': 'dos', 'tg': 3, 'bg': 12,  'bp': 35},
#    {'name': 'tres', 'tg': 0, 'bg': 50,  'bp': 50},
#    {'name': 'cuatro', 'tg': 1, 'bg': 10,  'bp': 1},
#    {'name': 'cinco', 'tg': 7, 'bg': 25, 'bp': 8},
#]

#pokemons = [
#    {'name': 'pok1', 'nivel': 45, 'tipo': 'electrico', 'subtipo': 'normal'},
#    {'name': 'pok2', 'nivel': 12, 'tipo': 'fuego', 'subtipo': 'dragon'},
#    {'name': 'pok3', 'nivel': 90, 'tipo': 'volador', 'subtipo': 'lucha'},
#    {'name': 'pok4', 'nivel': 20, 'tipo': 'agua', 'subtipo': None},
#    {'name': 'pok5', 'nivel': 27, 'tipo': 'planta', 'subtipo': 'tierra'},
#    {'name': 'pok6', 'nivel': 53, 'tipo': 'roca', 'subtipo': 'acero'},

#]

#for entrenador in enternadores:
#    lista_entrenadores.insertar(Entrenador(entrenador['name'],
#                                           entrenador['tg'],
#                                           entrenador['bp'],
#                                           entrenador['bg']), 'nombre')

#for entrenador in enternadores:
#    for i in range(randint(1, 5)):
#        pokemon = choice(pokemons)
#        pos = lista_entrenadores.busqueda(entrenador['name'], 'nombre')
#        pos.sublista.insertar(Pokemon(pokemon['name'],
#                                      pokemon['nivel'],
#                                      pokemon['tipo'],
#                                      pokemon['subtipo']), 'nombre')

#lista_entrenadores.barrido_lista_lista() 
#print()   


# punto a: cantidad de pok de un entrenador
#print()
#print("punto a: cantidad de pokemon de un entrenador")
#print()
#entrenador = input('ingrese nombre del entrenador ')
#pos = lista_entrenadores.busqueda(entrenador, 'nombre')
#if(pos):
#    print(f"el entrenador tiene {pos.sublista.tamanio()} pokemons")
#else:
#    print('el entrenador no esta en la lista')
#print()
 

# Punto b: entrenadores con mas de tres torneos
#print()
#print("punto b: entrenadores con mas de tres torneos")
#print()
#lista_entrenadores.barrido_entrenador_mas_tres()
#print()

#punto c: el Pokémon de mayor nivel del entrenador con mayor cantidad de torneos ganados;
#print()
#print("punto c: pokemon con mayor cantidad de torneos ganados")
#print()
#mayor = lista_entrenadores.mayor_de_lista('torneos_ganados')
#print(mayor.info, mayor.sublista.mayor_de_lista('nivel').info)
#print()

#punto d: mostrar todos los datos de un entrenador y sus Pokémos;
#print()
#print("punto d: datos de un entrenador y sus pokemons")
#print()
#entrenador = input('ingrese nombre del entrenador ')
#pos = lista_entrenadores.busqueda(entrenador, 'nombre')
#if(pos):
#    print(f"el entrenador tiene {pos.info}")
#    print('sus pokemons')
#    pos.sublista.barrido()
#else:
#    print('el entrenador no esta en la lista')
#print()

# punto e: mostrar los entrenadores cuyo porcentaje de batallas ganados sea mayor al 79 %;
#print("punto e: porcentaje mayor a 79")
#lista_entrenadores.barrido_porcentaje_victorias()

# punto f: los entrenadores que tengan Pokémons de tipo fuego y planta o agua/volador 
# (tipo y subtipo);
#print()
#print("punto f: entrenadores con pokemon de tipo fuego y planta o agua/volador")
#print()
#lista_entrenadores.barrido_tipo()

# punto g: el promedio de nivel de los Pokémons de un determinado entrenador;
#print()
#print("punto g: promedio de nivel de los Pokémons de un determinado entrenador")
#print()
#entrenador = input('ingrese nombre del entrenador: ')
#print()
#pos = lista_entrenadores.busqueda(entrenador, 'nombre')
#if(pos):
#    print('Listado de pokémones')
#    pos.sublista.barrido()
#    print(f"el entrenador tiene {pos.sublista.tamanio()} pokemons")
#    print(f"El promedio es: {pos.sublista.suma_nivel()/pos.sublista.tamanio()}")
#else:
#    print('el entrenador no esta en la lista')

# punto h: determinar cuántos entrenadores tienen a un determinado Pokémon;
#print()
#print("punto h: cuantos entrenadores tienen a un determinado pokemons")
#print()
#buscado = input('Ingresar en Nombre del Pokémon: ')
#print()
#lista_entrenadores.barrido_pokemonbuscado(buscado)

# punto i: mostrar los entrenadores que tienen Pokémons repetidos;
#print()
#print("punto i: entrenadores con pokemon repetidos")
#print()
#lista_entrenadores.barrido_repetido()

#punto j: determinar los entrenadores que tengan uno de los siguientes Pokémons: 
# Tyrantrum, Terrakion o Wingull;
#print()
#print("punto j: entrenadores con pokemon Tyrantrum, Terrakion o Wingull ")
#print()
#lista_entrenadores.entrenador_depokemon()

#punto k: determinar si un entrenador “X” tiene al Pokémon “Y”, tanto el nombre del entrenador
# como del Pokémon deben ser ingresados; además si el entrenador tiene al Pokémon se
# deberán mostrar los datos de ambos;

#print()
#print("punto k")
#entrenador = input('Ingrese nombre del entrenador: ')
#buscado = input('Ingresar en Nombre del Pokémon: ')
#print()
#pos = lista_entrenadores.busqueda(entrenador, 'nombre')
#if(pos):
#    pospok=pos.sublista.busqueda(buscado,'nombre')
#    if (pospok):
#        print(f"el entrenador: {pos.info}, tiene el pokemon: {pospok.info}")
#    else:
#        print('El entrenador no posee ese Pokémon')
#else:
#    print('El entrenador no esta en la lista')
#print()


#------------------------------------------------------------------------------------------

# Ejercicio 21:
# Se cuenta con una lista de películas de cada una de estas se dispone de los 
# siguientes datos:
# nombre, valoración del público –es un valor comprendido entre 0-10–, 
# año de estreno y recaudación. Desarrolle los algoritmos necesarios para realizar 
# las siguientes tareas:
# A) permitir filtrar las películas por año –es decir mostrar todas las películas de un 
# determinado año–;
# B). mostrar los datos de la película que más recaudo;
# C) indicar las películas con mayor valoración del público, puede ser más de una;
# D). mostrar el contenido de la lista en los siguientes criterios de orden 
# –solo podrá utilizar una lista auxiliar–:
# I. por nombre,
# II. por recaudación,
# III. por año de estreno,
# IV. por valoración del público.

#class Pelicula:
    
#    def __init__(self, nombre, anio, valor, recaudacion):
#        self.nombre = nombre
#        self.anio = anio
#        self.valor = valor
#        self.recaudacion = recaudacion
    
#    def __str__(self):
#         return f"{self.nombre} - {self.anio} - {self.valor} - {self.recaudacion}"

#Lista_de_peliculas = Lista()
#Lista_aux= Lista()

#peliculas = [
#    {'film':'La red social',            'year':'2010','star':'10','many':'   100.00'},
#    {'film':'Toy Story 3',              'year':'2010','star':' 7','many':'  2000.00'},
#    {'film':'Skyfall',                  'year':'2012','star':' 7','many':' 11851.00'},
#    {'film':'Origen',                   'year':'2010','star':' 6','many':'   500.00'},
#    {'film':'El Gran Hotel Budapest',   'year':'2014','star':' 6','many':'  4044.00'},
#    {'film':'El topo',                  'year':'2011','star':' 5','many':'  2500.00'},
#    {'film':'Wonder',                   'year':'2017','star':' 7','many':' 87817.00'},
#    {'film':'La invención de Hugo',     'year':'2011','star':' 1','many':'  1700.00'},
#    {'film':'Coco',                     'year':'2017','star':'10','many':' 34044.00'},
#    {'film':'Gravity',                  'year':'2013','star':' 4','many':' 15454.00'},
#    {'film':'Marvel Los Vengadores',    'year':'2012','star':' 8','many':'300000.00'},
#    {'film':'Blue Jasmine',             'year':'2013','star':' 3','many':'  5440.00'},
#    {'film':'Descifrando Enigma',       'year':'2014','star':' 9','many':' 14464.00'},
#    {'film':'Sicario',                  'year':'2015','star':' 4','many':'  5145.00'},
#    {'film':'12 años de esclavitud',    'year':'2013','star':' 5','many':'  5814.00'},
#    {'film':'Bohemian Rhapsody',        'year':'2018','star':' 9','many':' 84554.00'},
#]

#for peli in peliculas:
#    Lista_de_peliculas.insertar(Pelicula(peli['film'],
#                                         peli['year'], 
#                                         peli['star'],
#                                         peli['many']),'nombre')

#Lista_de_peliculas.barrido()

# Punto a: permitir filtrar las películas por año –es decir mostrar todas las películas de un 
# determinado año–;
#print()
#print("punto a")
#aniobuscado = input('Ingrese el año que desea buscar:')
#print()
#Lista_de_peliculas.barrido_anio(aniobuscado)

#punto b: mostrar los datos de la película que más recaudo;
#print()
#print("punto b")
#mayor = Lista_de_peliculas.mayor_recaudacion()
#print(mayor.info)
#print()

#Punto c: indicar las películas con mayor valoración del público, puede ser más de una;
#print("punto c")
#mayor = Lista_de_peliculas.mayor_valor()
#estrellas=(mayor.info.valor)
#Lista_de_peliculas.barrido_valor(estrellas)

# Punto d: mostrar el contenido de la lista en los siguientes criterios de orden 
# –solo podrá utilizar una lista auxiliar–:
# I. por nombre,
# II. por recaudación,
# III. por año de estreno,
# IV. por valoración del público.

#print()
#print("punto d")
#opcion=input('Elija una opción: (1)por nombre, (2)por recaudación, (3)por año de estreno, (4)por valoración del público.')
#print()

#if opcion=='1':
#    orden='nombre'
#elif opcion=='2':
#    orden='recaudacion'
#elif opcion=='3':
#    orden='anio'
#elif opcion=='4':
#    orden='valor'
#else:
#    print('Ha colocada una opcion incorrecta')

#for peli in peliculas:
#    Lista_aux.insertar(Pelicula(peli['film'],
#                                peli['year'], 
#                                peli['star'],
#                                peli['many']),orden)

#Lista_aux.barrido()


#------------------------------------------------------------------------------------------

# Ejercicio 22:

#Se dispone de una lista de todos los Jedi, de cada uno de estos se conoce su nombre, 
# maestros, colores de sable de luz usados y especie. implementar las funciones necesarias 
# para resolver las actividades enumeradas a continuación:
# a. listado ordenado por nombre y por especie;
# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
# d. mostrar los Jedi de especie humana y twi'lek;
# e. listar todos los Jedi que comienzan con A;
# f. mostrar los Jedi que usaron sable de luz de más de un color;
# g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
# h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

class Jedi:

    def __init__(self, nombre, especie, maestro, sable_luz):
        self.nombre = nombre
        self.especie = especie
        self.maestro = maestro
        self.sable_luz = sable_luz

    def __str__(self):
        return f"{self.nombre} | {self.especie} | {self.maestro} | {self.sable_luz}"


lista_jedi = Lista()
lista_jedi2 = Lista()

file = open('jedis.txt')
lineas = file.readlines()

lista = []

lineas.pop(0)  # quitar cabecera
for linea in lineas:
    datos = linea.split(';') #separa el texto cuando encuentra ;
    datos.pop(-1) #elimina el ultimo elemento
    print(datos[4].split('/'))
    lista_jedi.insertar(Jedi(datos[0],
                             datos[2],
                             datos[3].split('/'),
                             datos[4].split('/')),
                        campo='nombre')
    lista_jedi2.insertar(Jedi(datos[0],
                              datos[2],
                              datos[3],
                              datos[4].split('/')),
                         campo='especie')
    lista.append(Jedi(datos[0],
                      datos[2],
                      datos[3].split('/'),
                      datos[4].split('/')))
# a. listado ordenado por nombre y por especie; 
lista_jedi.barrido()
print()
lista_jedi2.barrido()

# b. mostrar toda la información de Ahsoka Tano y Kit Fisto;
dato = lista_jedi.busqueda('kit fisto', 'nombre')
if dato:
    print(f'el Jedi {dato.info}')
else:
    print('el Jedi no esta en la lista')

dato = lista_jedi.busqueda('ahsoka tano', 'nombre')
if dato:
    print(f'el Jedi {dato.info}')
else:
    print('el Jedi no esta en la lista')

# c. mostrar todos los padawan de Yoda y Luke Skywalker, es decir sus aprendices;
print()
print("maestros")
lista_jedi.barrido_jedi_master()

# d. mostrar los Jedi de especie humana y twi'lek;
print()
print("especie")
lista_jedi.barrido_especie()

# e. listar todos los Jedi que comienzan con A;
print()
lista_jedi.barrido_comienza_con(['a'])

# f. mostrar los Jedi que usaron sable de luz de más de un color;
print()
print("sable de luz mas de un color")
lista_jedi.barrido_sabledeluz()

#g. indicar los Jedi que utilizaron sable de luz amarillo o violeta;
print()
print("color amarillo o violeta")
lista_jedi.barrido_aov()

#h. indicar los nombre de los padawans de Qui-Gon Jin y Mace Windu, si los tuvieron.

print()
print("punto h")
print()
dato = lista_jedi.busqueda('qui-gon jin', 'nombre')
if dato:
    print(f'Los padawans del Jedi {dato.info.nombre} son, {dato.info.maestro}')
else:
    print('el Jedi no esta en la lista')
dato = lista_jedi.busqueda('mace windu', 'nombre')
if dato:
    print(f'Los padawans del Jedi {dato.info.nombre} son, {dato.info.maestro}')
else:
    print('el Jedi no esta en la lista')
print()

