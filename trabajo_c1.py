import re
class validarPass():
    def __init__(self):
        print("Validar contraseña...(No admite comillas)\n")
    def validar(self):
        self.passw = str(input("Ingrese la contraseña: "))
        self.patron = r"^[A-Z][0-9][0-9][0-9][a-z][a-z][a-z](?:[!@#$%^&*(),.¿¡?:{}|<>]{3})$"
        self.response = bool(re.search(self.patron, self.passw))
        if (self.response):
            print("La contraseña es correcta\n")
            self.sw = str(input("Desea continuar?[s/n]"))
            return self.sw
        else:
            print("Contraseña incorrecta.\n")
            self.sw = str(input("Desea continuar?[s/n]"))
            return self.sw
app = validarPass()
sw = app.validar()

while(sw=="s"):
    app = validarPass()
    sw = app.validar()

        
