#para mostrar en pantalla
  #print ("hola")

#para mostrar texto y variables
#num=5
#num2= "hola"

     #print("hola" , num , "chau")

# para pedir que ingrese un dato es con la palabra input, siempre ingresa un string
       # variable= input ("ingrese su nombre")
      #print (variable)

#type es una funcion que te dice de que tipo es la variable ej:
      #print (type(num))


#convercion: como input simepre te pone el dato como string, para poder transformar
#            ese dato como entero se debe utilizar:
     #variable= int (imput ("ingrese su numero"))

#condicionales:
#numero=5
#if (numero>0):
#    print("es mayor")
#    print ("gama verdadera")
#else:
#    print("es menor")

#print ("fin del codigo")

# cuando ponemos if else se reemplaza por elif:
#if (numero>0):
#    print("es positivo")
#elif (numero < 0):
#    print ("es negativo")
#else:
#    print ("es neutro")

#print("fin del codigo")

#ciclos:
#while:
#while (numero>0):
#    print(numero)
#    numero -= 1

#for
#for i in range (1,11): #arranca en 0 (por lo tanto va a ir hasta el 10)
#    print("interaccion" , i)

#Funciones: (en python noexiste procedimiento)
# una funcion se define con la palabra reservada def seguido al nombre de la funcion
numero=4
def suma(num1,num2): """esta funcion realiza la suma entre dos numeros"""
    print ("la suma es:" , num1+num2)

#llamamos a la funcion por su nombre ej:
suma (numero , 5)