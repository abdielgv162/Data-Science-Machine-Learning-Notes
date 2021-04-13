import random 
from random import randint
import math
import matplotlib.pyplot as plt
import numpy as np


def crear_datos_y_ks(numero_de_datos, k):
    # Generamos un dataset de datos aleatorios
    # Y nuestras K's en puntos aleatorios también
    datos = []
    ks = []
    for _ in range (numero_de_datos):
        x = random.randint(0,100)
        y = random.randint(0,100)
        datos.append([x,y])
    for _ in range (k):
        k_x = random.randint(0,100)
        k_y = random.randint(0,100)
        ks.append([k_x,k_y])
    return datos,ks


def dibujar(datos_y_k):
    print(f'\nEstos son los datos que recibe: {datos_y_k[0]}')
    print(f'Estos son los K puntos que recibe: {datos_y_k[1]}\n')
    # Coordenadas
    x = []
    for i in datos_y_k[0]:
        x.append(i[0])
    y = []
    for i in datos_y_k[0]:
        y.append(i[1])
    # K puntos
    k_x = []
    for i in datos_y_k[1]:
        k_x.append(i[0])
    k_y = []
    for i in datos_y_k[1]:
        k_y.append(i[1])
    # Dibuja
    fig, ax = plt.subplots()
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.plot(x, y, 'o', color='#000000')
    plt.plot(k_x, k_y, 'P')
    plt.show()
    #print(f'Datos: {datos_y_k[0]}')
    #print(f' K: {datos_y_k[1]}')
    return datos_y_k[0], datos_y_k[1]
    

def centroide_mas_cercano(coordenadas):
    #print(f'Coordenadas: {coordenadas}')
    plt.figure(figsize=(10, 10))
    fig, ax = plt.subplots()
    plt.ylabel('Y')
    plt.xlabel('X')
    plt.suptitle('Primera iteración')
    #print(f'Datos que recibe: {coordenadas[0]}')
    #print(f'K puntos originales: {coordenadas[1]}')
    
    #Separamos componentes X de los datos
    x_datos = []
    for i in coordenadas[1]:
        x_datos.append([i[0]])
    #print(f'X: {x_datos}')   
    #Separamos componentes Y de los datos
    y_datos = []
    for i in coordenadas[1]:
        y_datos.append([i[1]])
    #print(f'Y: {y_datos}')
    
    #Para cada PUNTO
    for i in coordenadas[0]:
        #####Color hexadecimal aleatorio###########
        hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        digit_array = []
        for j in range(6):
            digit_array.append(hex_digits[randint(0,15)])
        joined_digits = ''.join(digit_array)
        hex_number = '#' + joined_digits
        ############################################ 
        distancias = []
        for j in coordenadas[1]:
            dis_x = abs((i[0])-(j[0]))
            dis_y = abs((i[1])-(j[1]))
            distancia = abs(round((math.sqrt((dis_x)**2+(dis_y)**2)),3))
            #print(distancia)
            distancias.append(distancia)
            minimo = min(distancias)
            #print(minimo)
        #print(f'Distancias: {distancias}')
        minimo = min(distancias)
        #print(f'Distancia minima: {minimo}')
        index = distancias.index(minimo)
        #print(f'El punto {i} tiene asignado al centroide {coordenadas[1][index]}\n')
        # Dibuja los puntos individuales
        plt.plot(i[0], i[1], 'o', color='#000000')
        plt.plot(coordenadas[1][index][0], coordenadas[1][index][1], marker='P')
        #Traza la linea
        plt.plot([i[0],coordenadas[1][index][0]], [ i[1],coordenadas[1][index][1] ], color=hex_number )
        #print(f'Punto X = {i[0]} , Centoride X = {coordenadas[1][index][0]} ')
        #print(f'Punto Y = {i[1]} , Centroide Y = {coordenadas[1][index][1]} ')      
        ################################################################### 
        #print(f'X : {x_datos} , Y: {y_datos}')
        x_datos[index].append( i[0] )
        y_datos[index].append( i[1] )
    #print(f'X : {x_datos} , Y: {y_datos}')
        #print('------------------------------------')
    #print(coordenadas[0])    
    plt.show()
    return x_datos, y_datos, coordenadas


def promedios_y_recalcula(nuevos):
    for k in range(1):
        
        #print(f' DATOS NUEVOS:\n {nuevos}')
        #print(f'K Xs anteriores: {nuevos[0]}')
        #print(f'K Ys anteriores: {nuevos[1]}')
        #print(f'Datos: {nuevos[2][0]}')
        #print(f'K puntos: {nuevos[2][1]}')

    
        
        nuevo_cluster_x = []
        nuevo_cluster_y = []
        clusters = []
        distancias = []

        for j in nuevos[0]:
            promedio_x = 0
            promedio_x = round(sum(j)/len(j),3)
            nuevo_cluster_x.append([promedio_x])
        #print(f'\nPromedios X: {nuevo_cluster_x}')    

        for j in nuevos[1]:
            promedio_y = 0
            promedio_y = round(sum(j)/len(j),3)
            nuevo_cluster_y.append([promedio_y])
        #print(f'Promedios Y: {nuevo_cluster_y}')
        #print('----------------------------------------')

        #clusters.append([nuevo_cluster_x,nuevo_cluster_y])
        #print(f'Clusters: {clusters}')
        
        
        ##### Dibujamos el lienzo y ejes ############
        plt.figure(figsize=(10, 10))
        fig, ax = plt.subplots()
        plt.ylabel('Y')
        plt.xlabel('X')
        plt.suptitle(f'Iteración número: {k+2}')
        
        
        #print(f'\nDatos: {nuevos[2][0]}')      
        #print(f'Nueva lista de K puntos: {nuevo_cluster_x} , Y: {nuevo_cluster_y}')  
        k_puntos = []
        for i in zip(nuevo_cluster_x, nuevo_cluster_y):
            k_puntos.append(i)
            plt.plot(i[0], i[1], marker='P') 
        #print(f'Nuevos K puntos:  {k_puntos}')
        
        #Separamos componentes X de los K
        
        x_datos = []            
        for i in nuevo_cluster_x:
            x_datos.append(i)
        #print(f'X: {x_datos}')   
            
        #Separamos componentes Y de los K
        y_datos = []
        for i in nuevo_cluster_y:
            y_datos.append(i)
        #print(f'Y: {y_datos}')
        
        #print('  -------------------------------------------- ')
        
        
        #Por cada DATO
        for i in nuevos[2][0]: 
            
            #######Color hexadecimal aleatorio###############################################
            hex_digits = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
            digit_array = []
            for j in range(6):
                digit_array.append(hex_digits[randint(0,15)])
            joined_digits = ''.join(digit_array)
            hex_number = '#' + joined_digits
            #################################################################################
            
            ########  Dibuja los puntos individuales  ###################################
            plt.plot(i[0], i[1], 'o', color='#000000')
            
            distancias = []
            ## POR CADA NUEVO K punto
            for j in k_puntos:
                ## CALCULA LA DISTANCIA DE CADA PUNTO A CADA K
                dis_x = abs((i[0])-(j[0][0]))
                dis_y = abs((i[1])-(j[1][0]))
                distancia = abs(round((math.sqrt((dis_x)**2+(dis_y)**2)),3))
                distancias.append(distancia)
                minimo = min(distancias) 
            #print(f'Distancias: {distancias}')
            minimo = min(distancias)
            #print(f'Distancia minima: {minimo}')
            # Marca el indice de las distancias que corresponde
            # Con el indice del cluster más cercano
            index = distancias.index(minimo)
            
            #print(f'El punto {i} tiene asignado al centroide {k_puntos[index]}\n')
            #print('-------------------------------------------')

            #Traza la linea
            plt.plot([i[0], k_puntos[index][0][0]], [ i[1],k_puntos[index][1][0] ], color=hex_number )
            ################################################################### 
            
            x_datos[index].append( i[0] )
            y_datos[index].append( i[1] )
                
            #print(f'X: {x_datos}') 
            #print(f'Y: {y_datos}')    

            
        nuevo = []
        nuevo.append(x_datos)
        nuevo.append(y_datos)
        nuevo.append(nuevos[2][0])
        nuevo.append(k_puntos)    
        #print(nuevo[0][0])
        #print(nuevo[1][0])
    
if __name__ == '__main__':
    numero_de_datos = int(input('¿De que tamaño será el dataset?: '))
    k = int(input("¿Cuantos grupos se obtendrán (K)?: "))
    datos_y_k = crear_datos_y_ks(numero_de_datos, k)
    coordenadas = dibujar(datos_y_k)
    nuevos = centroide_mas_cercano(coordenadas)
    nuevo1 = promedios_y_recalcula(nuevos)
