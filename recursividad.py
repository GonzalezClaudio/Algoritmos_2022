# FACTORIAL INTERACTIVO:
#def factorial_i(numero):
#    factorial=1
#    for i in range (2,6):
#        factorial = factorial*i
    
#    return factorial

#print (factorial_i(5))

#FACTORIAL RECURSIVO:

#def factorial_r(numero):
#    if (numero==1 or numero==0):
#        return 1
#    else:
#        return numero*factorial_r(numero-1)

#print (factorial_r(5))

#FIBONACCI INTERACTIVO:
#def fibonacci_i(numero):
#    fib_1=0
#    fib_2=1
#    fibonacci=0
#    for i in range (2,numero+1):
#        fibonacci=fib_1+fib_2
#        fib_1=fib_2
#        fib_2=fibonacci
#    return fibonacci

#print(fibonacci_i(7))

#FIBONACCI RECURSIVO:
def fibonacci_r(numero):
    if(numero==0 or numero==1):
        return numero
    else:
        return fibonacci_r(numero-1) + fibonacci_r (numero-2)

print (fibonacci_r(8))