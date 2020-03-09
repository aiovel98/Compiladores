import re
from sys import argv
#def busqueda_patron(patrones, string):
#    for encontrado in patrones:
#        print(re.findall(encontrado, string))
#patron = re.compile(r'\b[a-z][0-9][0-9][a-z]\b|\b[0-9][0-9][0-9]\b') #r convierte la cadena en string pura, sin los comandos \
script, patron, cadena = argv
string = cadena.replace(",", " ")
#patrones = [r'\b[a-z][0-9][0-9][a-z]\b',r'\b[0-9][0-9][0-9]\b']
#busqueda_patron(patrones, string)


patron = r"\b" + patron + r"\b"
print re.findall(r""+patron, string)