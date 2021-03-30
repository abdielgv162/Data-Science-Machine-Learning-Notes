# py -m venv env
# env\Scripts\activate.bat
import random 
import math
from bokeh.layouts import row
from bokeh.plotting import figure, show

def crear_datos():#Creamos los puntitos que representarán el dataset
    datos = []
    # Generamos unos datos aleatorios
    for _ in range (numero_de_datos):
        x = random.randint(0,10)
        y = random.randint(0,10)
        datos.append([x,y])
    #Revisamos cuales son
    print(f'Todos los puntos: {datos}')
    return datos

def dist_euclidiana(datos): #Calcular distancia entre puntos M#1
    #Seleccionamos el punto 0 para iniciar el arbol
    #Como son aleatorios, da igual cual escogemos, pero facilita
    #el proceso ya que solo falta recorrer los elementos de la lista.
    actual = datos[0] 
    print(f'\nDato actual: {actual} \n')
    distancias = []
    for i in datos[1::]:
        dis_x = abs((actual[0])-(i[0]))
        dis_y = abs((actual[1])-(i[1]))
        distancia = abs(round((math.sqrt((dis_x)**2+(dis_y)**2)),3))
        distancias.append(distancia)
        print(f'Distancia al punto {i}= {distancia} unidades')
    print(f'\nDistancias: {distancias}')
    minimo = min(distancias)
    print(f'Valor mínimo: {minimo}')
    index = distancias.index(minimo)
    print(f'\nEl valor mínimo es el indice {index} de la lista de distancias,\nque corresponde al punto {datos[index]}.\n')
    
    print(f'Punto actual: {actual}')
    print(f'Punto cercano: {datos[index]}')
    actual = [(actual[0] + datos[index][0] ) / 2, (actual[1] + datos[index][1] ) / 2]
    print(f'Nuevo cluster: {actual}')

def merge_clusters(index,datos):
    print(datos[0])

def dibujar(datos):
    #Delimitamos el espacio y color del plano
    d1 = figure(plot_width=600, plot_height=600, background_fill_color="#ffffff") 
    #Listas vacias para guardar las componentes
    xses = []
    yes = []
    for i in datos:
        x = (i[0])
        y = (i[1])
        xses.append(x)
        yes.append(y)
        #Dibuja punto por punto
        d1.circle(x, y, size=10, color="#DC33FF", alpha=0.8)
    #Muestra el dibujo con todos los puntos
    show(d1)


if __name__ == '__main__':
    numero_de_datos = int(input('Ingrese la cantidad de datos a usar :'))
    datos = crear_datos()
    dist_euclidiana(datos)
    
    #dibujar(datos)