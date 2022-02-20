from Analizardata import Analizardata
from Analizarlfp import Analizarlfp


class Aplicacion:
    def __init__(self):
        self.app()
        self.data=Analizardata()
        self.lfp=Analizarlfp()
    
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
                self.data=Analizardata()
                self.data.analizador()
            elif x =="2":
                self.lfp=Analizarlfp()
                self.lfp.analizador()
            elif x =="3":
                
                
                for ins in self.lfp.lista_instrucciones:
                    print("hola")
                    ins.graficas(self.data.lista_productos)
            elif x =="4":
                self.reporte(self.data.lista_productos)
            elif x =="5":
                print("Saliendo...")
                break
            else:
                print("Escoja un dato valido porfavor:")


    def totalProducto(self,prod):
        precio = 0
        cantidad = 0
        if len(prod.numericos) > 1:
            precio = float(prod.numericos[0])
            cantidad = float(prod.numericos[1])
        elif len(prod.numericos) > 0:
            precio = float(prod.numericos[0])
        total = int(precio * cantidad)
        return total

    def reporte(self,listaInstruccionesdata):
        
        inicio = "<html><head><link rel=\"stylesheet\" type=\"text/css\" href=\"estilo.css\" media=\"screen\" /></head><body>"
        cuerpo = "<h1> Josue Daniel Solis Osorio 202001574</h1> <table class=\"styled-table\"><thead><tr><th>Nombre Producto</th><th>Precio</th><th>Total</th><th>Total Ventas</th></tr></thead><tbody>"

        for x in listaInstruccionesdata:
            
            i = 0
            while i < len(x.producto):#Ordenamiento Burbuja
                j = 0
                while j < len(x.producto) - 1:
                    productoActual = x.producto[j]
                    productoSiguiente = x.producto[j + 1]
                    if(self.totalProducto(productoActual) < self.totalProducto(productoSiguiente)):
                        x.producto[j] = productoSiguiente
                        x.producto[j+1] = productoActual
                    j = j + 1 
                i = i +1
            for prod in x.producto:
                precio = 0
                cantidad = 0
                if len(prod.numericos) > 1:
                    precio = float(prod.numericos[0])
                    cantidad = float(prod.numericos[1])
                elif len(prod.numericos) > 0:
                    precio = float(prod.numericos[0])
                total = int(precio * cantidad)

                html_producto = "<tr>"+"<td>"+prod.nombre+"</td>"+"<td>"+str(precio)+"</td>"+"<td>"+str(cantidad)+"</td>"+"<td>"+str(total)+"</td>"+"</tr>"
                cuerpo = cuerpo + html_producto


            
        mas = "<h4> Producto más vendido : " + x.producto[0].nombre+ "</h4>"
        menos = "<h4> Producto menos vendido" + x.producto[-1].nombre+ "</h4>"
        final = inicio + cuerpo + mas + menos + "</tbody></table></html></body>"

        f = open ('report_202001574.html','w')
        f.write(final)
        f.close()

y = Aplicacion()


