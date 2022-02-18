from fileinput import filename
from tkinter import Tk                               #Libreria para explorador de archivos (Se usara para leer data e instrucciones)
from tkinter.filedialog import askopenfilename       #complemento para el explorador ^^^

class Analizardata:                                   #Analizador para los .data
    def __init__(self):
        self.texto= ""
        self.id_data= ""
        self.id_instruciones= "" 
        self.data= ""
        self.instruciones= ""

    #Filtrado para archivos .data
    def leer(self):
        Tk().withdraw()
        archivodata=""
        try:
            filename = askopenfilename(title="Seleccione un archivo",
                                            filetypes=[("Archivos","*.data"), 
                                                        ("All files","*")])
            print(filename)
            with open(filename) as infile:
                archivodata=infile.read().strip()       #limpia cualquier carracter "corrupto"
            print(str(archivodata))

        except:
            print("no se selecciono ningun archivo")
            return

        archivodata=archivodata.lower()     #Case-Insensitive por ende esto hace dejar todo minusculas, para mayusculas es .upper()

        #Lectura
        for caracter in archivodata:
            print()



    