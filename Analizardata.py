from fileinput import filename
from operator import le
from pickle import TRUE
from tkinter import Tk                               #Libreria para explorador de archivos (Se usara para leer data e instrucciones)
from tkinter.filedialog import askopenfilename       #complemento para el explorador ^^^


class instruccionesdata:            #Clase para alamacenamiento y reconocimiento de valores
    def __init__(self):
        self.nombre_mes = ""
        self.nombre_producto = ""
        self.año = ""
        self.producto = []
        self.precio = ""
        self.cantidad = ""
        self.año_activado = False
        self.producto_activado = False
        self.precio_activado = False
        self.cantidad_activado = 0
        self.nombre_producto_activado = False

    def imprimir(self):
        return {
            "PRODUCTOS":self.producto,
            "nombre":self.nombre_mes,
            "año":self.año,
            "nombre del producto":self.nombre_producto,
            "precio":self.precio,
            "cantidad":self.cantidad,
        }

class datoProducto:
    def __init__(self):
        self.nombre = ""
        self.numericos = []
        

    def imprimir(self):
        print("//////////",self.nombre,self.numericos,"//////////")
    




class Analizardata:                                   #Analizador para los .data
    def __init__(self):
        self.texto= ""
        self.id_data= ""
        self.id_instruciones= "" 
        self.data= ""
        self.instruciones= ""
        self.lista_tokens = []
        self.lista_productos = []               #Lista de productos


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
        objeto = instruccionesdata()
        producto = datoProducto()

        while self.texto != "":
            letra = self.leer_letra()
            if letra.isalpha() :            #Inicio de lectura 
                lectura = self.letras_s0()             
                objeto.nombre_mes = lectura #Guardando Mes

                self.lista_tokens.append(lectura)
            elif letra == "\"" or letra == "“" or letra == "”":
                lectura = self.comillas_s0()
                objeto.nombre_producto_activado = True
                print (objeto.nombre_producto)
                if objeto.nombre_producto_activado == True:    
                    objeto.nombre_producto_activado = False
                    producto.nombre = lectura
                

                   
                   

                self.lista_tokens.append(lectura)
            elif letra == ":":
                self.quitar_primera_letra()
                objeto.año_activado = True   #Activando año
                self.lista_tokens.append(":")   
            elif letra == "(":
                self.quitar_primera_letra()
                self.lista_tokens.append("(")
            elif letra == "[":
                objeto.cantidad_activado = True
                producto = datoProducto()
                self.quitar_primera_letra()
                self.lista_tokens.append("[")
            elif letra == ")":
                self.quitar_primera_letra()
                self.lista_productos.append(objeto)
                self.lista_tokens.append(")")
            elif letra == "]":
                self.quitar_primera_letra()
                self.lista_tokens.append("]")
            elif letra == ";":
                self.quitar_primera_letra()
                objeto.producto.append(producto)
                self.lista_tokens.append(";") 
            elif letra == ",":
                self.quitar_primera_letra()
                self.lista_tokens.append(",")
            elif letra.isnumeric() == True :   
                lectura = self.numero_s0()
                if objeto.año_activado == True :
                    objeto.año_activado = False   #reset
                    objeto.año = lectura         #Guardando Año
                else:
                    producto.numericos.append(lectura)
             

                self.lista_tokens.append(lectura)     ##############

            elif letra == "\n" or letra == "\t" or letra == " ":   
                self.quitar_primera_letra()
           
            
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

    def numero_s0(self):
        letra = self.leer_letra()
        self.quitar_primera_letra()
        return letra +  self.numero_s1()     
                   
            

    def numero_s1(self):
        letra = self.leer_letra()
        if True ==  letra.isnumeric():
            self.quitar_primera_letra()
            return letra + self.numero_s1()
        elif letra == ".":
            self.quitar_primera_letra()
            return letra + self.numero_s2()
        else:
            return ""

    def numero_s2(self):
        letra = self.leer_letra()
        if True ==  letra.isnumeric():
            self.quitar_primera_letra()
            return letra + self.numero_s2()
        else:
            return ""
        
    
    

            

            



            





        






    