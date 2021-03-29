import random 
from bokeh.layouts import row
from bokeh.plotting import figure, show

def crear_datos():
    
    #Creamos el espacio donde se dibujarán los puntitos de datos
    d1 = figure(plot_width=600, plot_height=600, background_fill_color="#ffffff") 
    
    # Generamos unos datos aleatorios
    for _ in range (numero_de_datos):
        x = random.randint(0,10)
        y = random.randint(0,10)
        # Renderizamos 
        d1.circle(x, y, size=10, color="#DC33FF", alpha=0.8)
    # Visualizamos
    show(d1)

if __name__ == '__main__':
    numero_de_datos = int(input('Ingrese la cantidad de datos a usar :'))
    crear_datos()