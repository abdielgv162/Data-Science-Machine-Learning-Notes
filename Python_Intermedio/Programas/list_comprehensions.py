# Comentar varias lineas de código
# Ctrl K + Ctrl C

def without_list_comprehensions():
    list_n_to_2 = []
    for i in range(1, 101):
        list_n_to_2.append(i**2)

    print(f'Lista de naturales al cuadrado:\n {list_n_to_2}')


    n_to_2_not_divisible3 = []
    for i in range (101):
        n_to_2_not_divisible3.append(i**2)
        if (i**2)%3 == 0:
            n_to_2_not_divisible3.remove(i**2)

    print('\nLista de naturales al cuadrado que NO son divisibles entre 3\n' 
            , n_to_2_not_divisible3)

def using_list_comprehensions():
    list_n_to_2 = [n**2 for n in range(101)]
    dict_n_to_2 = {n: n**2 for n in range(101)}

    print(f'Lista de naturales del 1-100 al cuadrado: \n{list_n_to_2}')
    print(f'\n Diccionario de naturales del 1-100 al cuadrado:\n{dict_n_to_2}')

if __name__ == '__main__':
    without_list_comprehensions()