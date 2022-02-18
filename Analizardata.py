from fileinput import filename
from operator import le
from tkinter import Tk                               #Libreria para explorador de archivos (Se usara para leer data e instrucciones)
from tkinter.filedialog import askopenfilename       #complemento para el explorador ^^^

class Analizardata:                                   #Analizador para los .data
    def __init__(self):
        self.texto= ""
        self.id_data= ""
        self.id_instruciones= "" 
        self.data= ""
        self.instruciones= ""
        self.lista_tokens = []

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

        except:
            print("no se selecciono ningun archivo")
            return

        archivodata=archivodata.lower()     #Case-Insensitive por ende esto hace dejar todo minusculas, para mayusculas es .upper()

        #Lectura
        return archivodata


    def analizador(self):
        self.texto = self.leer()

        while self.texto != "":
            letra = self.leer_letra()
            if letra.isalpha():
                lectura = self.letras_s0()
                self.lista_tokens.append(lectura)
            elif letra == "\"" or letra == "“" or letra == "”":
                lectura = self.comillas_s0()
                self.lista_tokens.append(lectura)
            elif letra == ":":
                self.quitar_primera_letra()
                self.lista_tokens.append(":")
            else:
                self.quitar_primera_letra()
                print({"error":letra})

        print(self.lista_tokens)

    def quitar_primera_letra(self):
        if(self.texto != ""):
            self.texto=self.texto[1:]
    
    def leer_letra(self):
        if(self.texto != ""):
            return self.texto[0]
        else:
            return ""    

    def letras_s0(self):
        letra = self.leer_letra()
        if letra.isalpha():
            self.quitar_primera_letra()
            return letra + self.letras_s1()

    def letras_s1(self):
        letra = self.leer_letra()
        if letra.isalpha():
            self.quitar_primera_letra()
            return letra + self.letras_s1()
        elif letra.isnumeric():
            self.quitar_primera_letra()
            return letra + self.letras_s1()
        else:
            return ""
        
    def comillas_s0(self):
        letra = self.leer_letra()
        if letra == '\"' or letra == "“" or letra == "”":
            self.quitar_primera_letra()
            return letra +  self.comillas_s1()

    
    def comillas_s1(self):
        letra = self.leer_letra()
        if letra != '\"'and letra != "“" and letra != "”":
            self.quitar_primera_letra()
            return letra + self.comillas_s1()
        else:
            self.quitar_primera_letra()
            return letra 
            





        






    