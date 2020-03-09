from sys import argv

script, numero1, signo, numero2 = argv
try:
    numero1 = int(numero1)
    numero2 = int(numero2)
    def suma(numero1, signo, numero2):
        return numero1 + numero2
    def resta(numero1, signo, numero2):
        return numero1 - numero2
    def mult(numero1, signo, numero2):
        return numero1 * numero2
    def div(numero1, signo, numero2):
        try:
            return numero1 / numero2
        except ZeroDivisionError:
            print ("Error: división por cero")
    if(signo=="+"):
        print ("La suma es: ",suma(numero1, signo, numero2))
    elif(signo=="-"):
        print ("La resta es: ",resta(numero1, signo, numero2))
    elif (signo=="*"):
        print ("La mult es: ",mult(numero1, signo, numero2))
    elif (signo=="/"):
        print ("La div es: ",div(numero1, signo, numero2))
    else:
        print("Error de operando")
except (TypeError, ValueError):
    print("Error de caracteres")



