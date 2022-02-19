from Analizardata import Analizardata
from Analizarlfp import Analizarlfp
data=Analizardata()
lfp=Analizarlfp()

class Aplicacion:
    def __init__(self):
        self.app()
    
    def app(self):
        while True:
            x=input('''
    1. Cargar datos
    2. Cargar Intrucciones
    3. Analizar
    4. Reportes
    5. Salir
    Escoja una opcion:''')
            if x =="1":
                data.analizador()
            elif x =="2":
                lfp.analizador()
            elif x =="3":
                pass
            elif x =="4":
                pass
            elif x =="5":
                print("Saliendo...")
                break
            else:
                print("Escoja un dato valido porfavor:")

y = Aplicacion()


