from tkinter import *
from tkinter import font
from tkinter import messagebox
import re
import getpass
class Aplicacion():
    def __init__(self):
        #Creacion del frame
        self.root = Tk()
        self.root.resizable(0,0)
        self.frame = Frame(self.root, width="640", height="480")
        self.frame.pack()
        fuente = font.Font(weight='bold')
        #-----


        #Strings en donde se va a guardar la informacion en la caja de texto
        self.usuario = StringVar()
        self.clave = StringVar()
        
        #-----


        #Labels, cajas de texto y botones
        #self.usuario.set(getpass.getuser())
        self.lb1 = Label(self.frame, text="Usuario: ", font=fuente)
        self.txt1 = Entry(self.frame, textvariable=self.usuario, width=30)
        self.lb2 = Label(self.frame, text="Contraseña: ", font=fuente)
        self.txt2 = Entry(self.frame, textvariable=self.clave, width=30, show="*")
        self.bt1 = Button(self.frame, text="Validar", command=self.validarClave)
        self.bt2 = Button(self.frame, text="Cancelar", command=quit)
        #-----

        #Solo personalizacion de los widgets
        self.lb1.pack(side=TOP, fill=BOTH, expand=True, padx=5, pady=5)
        self.txt1.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.lb2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.txt2.pack(side=TOP, fill=X, expand=True, padx=5, pady=5)
        self.bt1.pack(side=LEFT, fill=BOTH, expand=True, padx=5, pady=5)
        self.bt2.pack(side=RIGHT, fill=BOTH, expand=True, padx=5, pady=5)
        #-----


        #Para "focusear" la caja de texto al inicio del frame
        self.txt1.focus_set()


        #Final del frame
        self.root.mainloop()
    def validarClave(self):
        self.patron = "^[A-Z][0-9][0-9][0-9][a-z][a-z][a-z][-*/+#$%&]$"
        respuesta = bool(re.search(self.patron, self.txt2.get()))
        if(respuesta):
            messagebox.showinfo("Validacion", "Contraseña correcta")
        else:
            messagebox.showerror("Validacion", "Contraseña incorrecta")

app = Aplicacion()