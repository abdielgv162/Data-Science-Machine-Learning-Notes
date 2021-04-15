#Main
def run(): 
    my_list = [1, 'Holi', True, 4.5]
    my_dict = {"fristname": 'Abdiel', "Lastname": 'Guerr'}
    
    #Lista de diccionarios
    super_list = [
        {"fristname": 'Abdiel', "Lastname": 'Guerr'},
        {"fristname": 'ASDFG', "Lastname": 'gdfgdfg'},
        {"fristname": 'ghjkl', "Lastname": 'asdasdsa'},
        {"fristname": 'qwert', "Lastname": 'weqwe'},
        {"fristname": 'zxcvv', "Lastname": 'cvzczxc'},
        {"fristname": 'vbnmm', "Lastname": 'hfghfg'}, 
    ]

    #Diccionario de listas
    super_dict = {
        "natural_nums": [1,2,3,4,5],
        "integer_nums": [-1, -2, 0, 1, 2],
        "floating_nums": [1.1, 2.2, 3.3, 4.4]
    }
    
    # El método .items() nos permite recorrer llaves y valores
    # de un diccionario al mismo tiempo en un ciclo.
    for key, value in super_dict.items():
        print(f'Key: {key}, Value: {value}')

        
#Entry point    
if __name__ == '__main__': 
    run()