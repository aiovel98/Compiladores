class Calculadora:
    
    def __init__(self):
        print ("""************
                Calculadora
                ************
                """)
    def suma(self,x,y):
        print ("La suma es: ", x+y)
    def resta(self, x, y):
        print ("La resta es: ", x-y)
    def multiplicacion(self, x, y):
        print ("La multiplicacion es: ", x*y)
    def division(self, x, y):
        try:
            print ("La division es: ", x/y)
        except ZeroDivisionError:
            print ("Error, división entre cero")

def Menu():
        resultado = Calculadora()
        print ("Digite dos números")
        a = input("Numero 1: ")
        b = input("Numero 2: ")
        print ("""\n
                    Menu
                    1) Suma
                    2) Resta
                    3) Multiplicacion
                    4) Division
                    5) Salir""")
        opc = input("Seleccione una opcion: ")
        if(opc == 1):
            resultado.suma(a,b)
        elif (opc == 2):
            resultado.resta(a, b)
        elif (opc == 3):
            resultado.multiplicacion(a,b)
        elif (opc == 4):
            resultado.division(a,b)

Menu()