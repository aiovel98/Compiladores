def Menu():

    print ("""************
Calculadora
************
Menu
1) Suma
2) Resta
3) Multiplicacion
4) Division
5) Salir""")
def Calculadora():
    Menu()
    try:
        opc = int(input("Selecione Opcion\n"))
    except ValueError:
        print("La entrada es incorrecta: escribe un numero entero")
        opc = int(input("Selecione Opcion\n"))
    while (opc >0 and opc <5):
        try:
            a = int(input("Ingrese Numero\n"))
            y = int(input("Ingrese Otro Numero\n"))
        except ValueError:
            print("La entrada es incorrecta: escribe un numero entero")
            a = int(input("Ingrese Numero\n"))
            y = int(input("Ingrese Otro Numero\n"))
        if (opc==1):
            try:
                print ("La Suma es:", a+y)
                opc = int(input("Selecione Opcion\n"))
            except ValueError:
                print ("La entrada es incorrecta: escribe un numero entero")
                opc = 1
        elif(opc==2):
            try:
                print("La Resta es:", a - y)
                opc = int(input("Selecione Opcion\n"))
            except ValueError:
                print("La entrada es incorrecta: escribe un numero entero")
                opc = 2
        elif(opc==3):
            try:
                print("La Multiplicacion es:", a * y)
                opc = int(input("Selecione Opcion\n"))
            except ValueError:
                print("La entrada es incorrecta: escribe un numero entero")
                opc = 3
        elif(opc==4):
            try:
              print ("La Division es:", a/y)
              opc = int(input("Selecione Opcion\n"))
            except ZeroDivisionError or ValueError:
              print ("No se Permite la Division Entre 0")
              print("Vuelva a digitar los valores")
              opc = 4
Calculadora()