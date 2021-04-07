# py -m venv env
# env\Scripts\activate.bat
import random 
from random import randint
import math
from bokeh.layouts import row
from bokeh.plotting import figure, show

from bokeh.models import LabelSet, ColumnDataSource
from bokeh.palettes import Category20 as palette


def crear_datos():#Creamos los puntitos que representarán el dataset
    datos = []
    # Generamos unos datos aleatorios
    for _ in range (numero_de_datos):
        x = random.randint(0,10)
        y = random.randint(0,10)
        datos.append([x,y])
    #Revisamos cuales son
    #print(f'Todos los puntos: {datos}')
    return datos

def calcula_y_dibuja(datos): #Calcular distancia entre puntos M#1
    #Seleccionamos el punto 0 para iniciar el arbol
    #Como son aleatorios, da igual cual escogemos, pero facilita
    #el proceso ya que solo falta recorrer los elementos de la lista.
    
    x_datos = []
    y_datos = []
    x_clusters = []
    y_clusters = []
    
    for i in datos:
        #print(i[0])
        x_datos.append(i[0])
    #print(f'X: {x_datos}')
    
    for i in datos:
        #print(i[1])
        y_datos.append(i[1])
    #print(f'Y: {y_datos}')
    
    # create a new plot
    p = figure(
        title="Clusterización jerárquica",
        sizing_mode="stretch_width",
        plot_width=800,
        plot_height=800,
            )

    # add circle renderer with legend_label arguments
    circle = p.circle(
        x_datos,
        y_datos,
        legend_label="Datos originales",
        fill_color= "#000000",
        fill_alpha=10,
        line_color= "#000000",
        size=10,
                        )

    # display legend in top left corner (default is top right corner)
    p.legend.location = "top_right"

    # add a title to your legend
    p.legend.title = "Información de puntitos"

    # change appearance of legend text
    p.legend.label_text_font = "times"
    p.legend.label_text_font_style = "italic"
    p.legend.label_text_color = "navy"

    # change border and background of legend
    p.legend.border_line_width = 3
    p.legend.border_line_color = "#21B4B3"
    p.legend.border_line_alpha = 0.8
    p.legend.background_fill_color = "#092D4D"
    p.legend.background_fill_alpha = 0.2
    
    
    actual = datos[0] 
    while len(datos) > 0:   
        distancias = []
        if actual == datos[0]: 
            print(f'Todos los puntos: {datos}')
            print(f'\nDato actual: {actual} \n')
            clusters = []
            for i in datos[1::]:      
                #####Color hexadecimal aleatorio###########
                hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
                digit_array = []
                for j in range(6):
                    digit_array.append(hex_digits[randint(0,15)])
                joined_digits = ''.join(digit_array)
                hex_number = '#' + joined_digits
                ############################################ 
                dis_x = abs((actual[0])-(i[0]))
                dis_y = abs((actual[1])-(i[1]))
                distancia = abs(round((math.sqrt((dis_x)**2+(dis_y)**2)),3))
                #distancias.append(distancia)
                print(f'Distancia al punto {i}= {distancia} unidades')

                distancias.append(distancia)
                
            print(f'\nDistancias: {distancias}')
            minimo = min(distancias)
            print(f'Valor mínimo: {minimo}')
            index = distancias.index(minimo)
            print(f'\nEl valor mínimo es el indice {index} de la lista de distancias,\nque corresponde al punto {datos[index+1]}.\n')
            print(f'Punto actual: {actual}')
            print(f'Punto cercano: {datos[index+1]}')
            actual = [(actual[0] + datos[index+1][0] ) / 2, (actual[1] + datos[index+1][1] ) / 2]
            print(f'Nuevo cluster: {actual}')
            ####Dibujar Clusters#############
            circle_clusters = p.circle(
                actual[0],
                actual[1],
                legend_label="1er cluster",
                fill_color=hex_number,
                fill_alpha=0.4,
                line_color=hex_number,
                size=10,                   )
                ###############################
            
            #########################
            clusters.append(actual)
            #############################
            print('--------------------------------')
            datos.pop(0)
            datos.pop(index)

        else:
            
            print(f'Todos los puntos: {datos}')
            print(f'\nDato actual: {actual} \n')
            for i in datos[::]:
                #####Color hexadecimal aleatorio###########
                hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
                digit_array = []
                for j in range(6):
                    digit_array.append(hex_digits[randint(0,15)])
                joined_digits = ''.join(digit_array)
                hex_number = '#' + joined_digits
                ############################################ 
                dis_x = abs((actual[0])-(i[0]))
                dis_y = abs((actual[1])-(i[1]))
                distancia = abs(round((math.sqrt((dis_x)**2+(dis_y)**2)),3))
                #distancias.append(distancia)

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
            
            ####Dibujar Clusters#############
            circle_clusters = p.circle(
                actual[0],
                actual[1],
                legend_label="Resto de clusters",
                fill_color=hex_number,
                fill_alpha=0.1,
                line_color=hex_number,
                size=200,                )
                ###############################
            

            
            #########################
            clusters.append(actual)
            #############################
            print('--------------------------------')
            datos.pop(index)
            
        ##################
        print(f'Clusters:{clusters}')     

    show(p)


    # show the results



if __name__ == '__main__':
    numero_de_datos = int(input('Ingrese la cantidad de datos a usar :'))
    datos = crear_datos()
    clusters = calcula_y_dibuja(datos)  


