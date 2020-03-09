import sys
class Calculadora:
    def __init__(self):
        print ("""************
                Calculadora
                ************
                """
                )
    def suma(self,x,y):
        print ("La suma es: ", x+y)
    def resta(self, x, y):
        print ("La resta es: ", x-y)
    def multi(self, x, y):
        print ("La multiplicacion es: ", x*y)
    def divi(self, x, y):
        try:
            print ("La division es: ", x/y)
        except ZeroDivisionError:
            print ("Error, división entre cero")

def Menu():
    while True:
        resultado = Calculadora()
        print ("Digite dos números")
        try:
            a = int(input("Numero 1: "))
            b = int(input("Numero 2: "))
            print ("""
                    Menu
                    1) Suma
                    2) Resta
                    3) Multiplicacion
                    4) Division
                    5) Salir""")
            opc = int(input("Seleccione una opcion: "))
            if(opc == 1):
                resultado.suma(a,b)
            elif (opc == 2):
                resultado.resta(a, b)
            elif (opc == 3):
                resultado.multi(a,b)
            elif (opc == 4):
                resultado.divi(a,b)
            elif (opc == 5):
                break
        except:
            print ("Error, tipo de dato invalido")
Menu()