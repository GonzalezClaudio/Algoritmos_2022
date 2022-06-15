from listaexamen import Lista
from cola import Cola
from pila import Pila
from random import randint , choice
from jurassic_park import dinosaurs


class Dino:
    
    def __init__(self, time, zone_code, dino_number, alert_level, name, type ):
        self.time = time
        self.zone_code = zone_code
        self.dino_number = dino_number
        self.alert_level = alert_level
        self.name = name
        self.type=type

    def __str__(self):
        return f"{self.time} | {self.zone_code} | {self.dino_number} | {self.alert_level} | {self.name} | {self.type}"


def busqueda_name(buscado):
    for dino in dinosaurs:
        if(int(buscado) == dino['number']):
            return dino['name']

def busqueda_type(buscado):
    for dino in dinosaurs:
        if(buscado== dino["name"]):
            return dino["type"]





file = open('alerts.txt')

lineas = file.readlines()
lineas.pop(0)
lista_dino1=Lista()
lista_dino2=Lista()

for linea in lineas:
    dato = linea.split(';')
    dato[3] = dato[3][:-1]
    dato.append(busqueda_name(dato[2]))
    dato.append(busqueda_type(dato[4]))
    lista_dino1.insertar(Dino(dato[0],
                              dato[1],
                              dato[2],
                              dato[3],
                              dato[4],
                              dato[5]),
                         campo='name')
    lista_dino2.insertar(Dino(dato[0],
                              dato[1],
                              dato[2],
                              dato[3],
                              dato[4],
                              dato[5]),
                         campo='time')


#listado ordenado por nombre
print("lista ordena por nombre")
lista_dino1.barrido()

#listado ordenado por fecha
print()
print("lista ordena por fecha")
lista_dino2.barrido()

#manterner la info oculta
print()
dato = lista_dino1.eliminar('WYG075', 'zone_code')
dato = lista_dino2.eliminar('WYG075', 'zone_code')
if dato:
    print(f'la info {dato.zone_code} fue oculta')
else:
    print('el codigo no esta en la lista')

dato = lista_dino1.eliminar('SXH966', 'zone_code')
dato = lista_dino2.eliminar('SXH966', 'zone_code')
if dato:
    print(f'la info {dato.zone_code} fue oculta')
else:
    print('el codigo no esta en la lista')

dato = lista_dino1.eliminar('LYF010', 'zone_code')
dato = lista_dino2.eliminar('LYF010', 'zone_code')
if dato:
    print(f'la info {dato.zone_code} fue oculta')
else:
    print('el codigo no esta en la lista')


#modificar el nombre del dino por el codigo
dato= lista_dino1.busqueda("HYD195" , "zone_code")
if (dato):
    lista_dino1.name = "Mosasaurus"
    print("el nombre del codigo HYD195 fue modificado")
else:
    print("no se encontro ese codigo")

#Tyrannosaurus Rex, Spinosaurus, Giganotosaurus con nivel  ́critical’ o ‘high’.
print()
print("barrido de nombre y alert level")
lista_dino1.barrido_nombre()

# solo de los dinosaurios Raptors y Carnotaurus; y los códigos de las zonas 
# donde puedo encontrar dinosaurios Compsognathus
#print()
#print('Lista dinos Raptors y Carnotaurus')
#lista_dino1.barrido_Rap_Car()
#print()
#print('Lista de las zonas donde puedo encontrar dinosaurios Compsognathus')
#lista_dino1.barrido_Zona()

# ultimo descubierto
#lista_dino1.ultimo()

#una con los datos de dinosaurios
#carnívoros y otra con los herbívoros, descarten las de nivel ‘low’ y ‘medium’.
cola_carnivoros= Cola()
cola_herbivoros= Cola()

for i in range(lista_dino1.tamanio()):
    dino = lista_dino1.obtener_elemento(i)
    if("critical" in dino.alert_level or "high" in dino.alert_level ):
        if("carnívoro" in dino.type):
            cola_carnivoros.arribo(dino)
        else:
            if ("herbívoro" in dino.type):
                cola_herbivoros.arribo(dino)
                


print()
print(" cola carnivoros ")
while(not cola_carnivoros.cola_vacia()):
    x=cola_carnivoros.atencion()
    print(x)

print()
print("cola herviboros")
while(not cola_herbivoros.cola_vacia()):
    x=cola_herbivoros.atencion()
    print(x)