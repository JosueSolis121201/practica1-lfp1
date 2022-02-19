import matplotlib.pyplot as plt
from fileinput import filename
from operator import le
from tkinter import Tk                               #Libreria para explorador de archivos (Se usara para leer data e instrucciones)
from tkinter.filedialog import askopenfilename
from xmlrpc.client import boolean       #complemento para el explorador ^^^


class instruccioneslfp:
    def __init__(self):
        self.nombre = ""
        self.grafica = ""
        self.titulo = ""
        self.titulox = ""
        self.tituloy = ""
        self.nombre_activado = False
        self.grafica_activado = False
        self.titulo_activado = False
        self.titulox_activado = False
        self.tituloy_activado = False

    def imprimir(self):
        return {
            "nombre":self.nombre,
            "grafica":self.grafica,
            "titulo":self.titulo,
            "titulox":self.titulox,
            "tituloy":self.tituloy,
        }

        


    def grafica_barra(self):
        ## Declaramos valores para el eje x
        eje_x = ['Python', 'R', 'Node.js', 'PHP']
        
        ## Declaramos valores para el eje y
        eje_y = [50,20,35,47]
        
        ## Creamos Gráfica
        plt.bar(eje_x, eje_y)
        
        ## Legenda en el eje y
        plt.ylabel('Cantidad de usuarios')
        
        ## Legenda en el eje x
        plt.xlabel('Lenguajes de programación')
        
        ## Título de Gráfica
        plt.title('Usuarios de lenguajes de programación')
        
        ## Mostramos Gráfica
        plt.show()
    
    
        
 

class Analizarlfp:                                   #Analizador para los .data
    def __init__(self):
        self.texto= ""
        self.id_data= ""
        self.id_instruciones= "" 
        self.data= ""
        self.instruciones= ""
        self.lista_tokens = []
        self.lista_instrucciones = []
        
    #Filtrado para archivos .data
    def leer(self):
        Tk().withdraw()
        archivodata=""
        try:
            filename = askopenfilename(title="Seleccione un archivo",
                                            filetypes=[("Archivos","*.lfp"), 
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
        objeto = instruccioneslfp()

        while self.texto != "":
            letra = self.leer_letra()
            if letra.isalpha() :
                lectura = self.letras_s0()
                if lectura=="nombre":
                    objeto.nombre_activado = True                          #Identificar "lo que es"
                elif lectura == "grafica":
                    objeto.grafica_activado = True
                elif lectura == "titulo":
                    objeto.titulo_activado = True
                elif lectura == "titulox":
                    objeto.titulox_activado = True
                elif lectura == "tituloy":
                    objeto.tituloy_activado = True
                self.lista_tokens.append(lectura)
            elif letra == "\"" or letra == "“" or letra == "”":         #Emparejamiento y almacenamiento contenido identificado
                lectura = self.comillas_s0()
                if objeto.nombre_activado == True:
                    objeto.nombre_activado = False #(Limpiar estado para siguiente lectura)
                    objeto.nombre = lectura
                if objeto.grafica_activado == True:
                    objeto.grafica_activado = False
                    objeto.grafica = lectura
                if objeto.titulo_activado == True:
                    objeto.titulo_activado = False
                    objeto.titulo = lectura
                if objeto.titulox_activado == True:
                    objeto.titulox_activado = False
                    objeto.titulox = lectura
                if objeto.tituloy_activado == True:
                    objeto.tituloy_activado = False
                    objeto.tituloy = lectura

                self.lista_tokens.append(lectura)
            elif letra == "<":
                objeto = instruccioneslfp()
                self.quitar_primera_letra()
                self.lista_tokens.append("<") 
            elif letra == "¿":
                self.quitar_primera_letra()
                self.lista_tokens.append("¿")
            elif letra == "?":
                self.quitar_primera_letra()
                self.lista_tokens.append("?")
            elif letra == ">":

                self.lista_instrucciones.append(objeto)         #Listado de objetos

                self.quitar_primera_letra()
                self.lista_tokens.append(">")
            elif letra == ":":
                self.quitar_primera_letra()
                self.lista_tokens.append(":")   
            elif letra == ",":
                self.quitar_primera_letra()
                self.lista_tokens.append(",")      

            elif letra.isnumeric() == True :   
                lectura = self.numero_s0()
                self.lista_tokens.append(lectura)    
            elif letra.isnumeric() == True :   
                lectura = self.numero_s0()
                self.lista_tokens.append(lectura)

            elif letra == "\n" or letra == "\t" or letra == " ":   
                self.quitar_primera_letra()
           
            
            else:
                self.quitar_primera_letra()
                print({"error":letra})


        for inst in self.lista_instrucciones:
            inst.grafica_barra()
            #print(inst.imprimir())


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

    def numero_s0(self):
        letra = self.leer_letra()
        self.quitar_primera_letra()
        return letra +  self.numero_s1()     
                   
            

    def numero_s1(self):
        letra = self.leer_letra()
        if True ==  letra.isnumeric():
            self.quitar_primera_letra()
            return letra + self.numero_s1()
        else:
            self.quitar_primera_letra()
            return letra 
    
    

            

            



            





        






    