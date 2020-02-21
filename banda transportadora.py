# Banda transportadora (selección de objetos: chico, mediano, grande)
#integrantes:
# FIGUEROA MARTINEZ ARMANDO
# MARTINEZ VALENCIA LUIS EDUARDO
# HERNANDEZ TOVAR ANDRES
# GARCIA GARCAIA SALVADOR 
p=0
g=0
m=0
class encendido:
    def __init__(self):
        pass
    def encendido (self,estado):
        if estado == "encendido" or "continua":
            p=0
            m=0
            g=0
            return("i")
        else:
            return("o")

class caja:
    def __init__(self):
        pass
    def caja (self,tamaño):
        
       
        if tamaño == "pequeño":
            global p
            p=p+1
            
        if tamaño == "mediano":
            global m
            m=m+1
           
        if tamaño == "grande":
            global g
            g =g+1
        print("el numero de pequeñas es ",p,"\n","el numero de medianas es ",m,"\n","el numero de grandes es ",g,"\n")
act="o"
while act==("o"):
    a=input(" Escribe encendido para activar la banda transportadora \n ")
    caja1=caja()
    encendido1=encendido()
    act=encendido1.encendido(a)
while (act==("i")) :
    tamaño = input(" dame el tamaño pequeño,grande o mediano\n ")
    caja1.caja(tamaño)
    continua= input(" Escribe continua si deseas que la banda siga funcionando \n ")
    act=encendido1.encendido(continua)








