import random
import os
from functools import reduce

drawing = [''' 
 _     _                                               ______                      
| |   | |                                             / _____)                     
| |__ | |  ____  ____    ____  ____    ____  ____    | /  ___   ____  ____    ____ 
|  __)| | / _  ||  _ \  / _  ||    \  / _  ||  _ \   | | (___) / _  ||    \  / _  )
| |   | |( ( | || | | |( ( | || | | |( ( | || | | |  | \____/|( ( | || | | |( (/ / 
|_|   |_| \_||_||_| |_| \_|| ||_|_|_| \_||_||_| |_|   \_____/  \_||_||_|_|_| \____)
                       (_____|                                                     
                                                                                        
''',
'''
   +---+
   |   |
       |
       |
       |
       |
=========''', 
           
'''
   +---+
   |   |
   O   |
       |
       |
       |
=========''', 
           
'''
   +---+
   |   |
   O   |
   |   |
       |
       |
 =========''', 
                     
'''
   +---+
   |   |
   O   |
  /|   |
       |
       |
 =========''',
                     
'''
   +---+
   |   |
   O   |
  /|\  |
       |
       |
 =========''',
                     
'''
   +---+
   |   |
   O   |
  /|\  |
  /    |
       |
 =========''', 
                     
'''
   +---+
   |   |
   O   |
  /|\  |
  / \  |
       |
=========''',
'''
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼

'''
]

# Obtenemos una palabra random de nuestro archivo de palabras
def getting_word():
    words = []
    with open("../Programas/archivos/diccionario_palabras.txt" , "r", encoding="UTF-8") as  f:
        for line in f:
            # removemos espacios y ponemos todo en mayusculas
            words.append(line.strip().upper())
    word = random.choice(words)
    #print(word)
    #print(len(word))
    return word

# Omitimos los acentos
def without_accent_mark(word):
    word_changed = (
        ("Á", "A"),
        ("É","E"),
        ("Í","I"),
        ("Ó","O"),
        ("Ú","U"),
    ) 
    for a,b in word_changed:
        word = word.replace(a,b)
    print(f'{word}\n')
    return word 

def juega(without_accent):
    
    list_words = [n for n in without_accent]
    list_lines = ["_" for n in without_accent ]
    #print(f'without_accent:{without_accent}')
    #print(f'list_words:{list_words}')
    #print(f'list_lines:{list_lines}')
    
    #Lo hacemos en forma de diccionario para después usar get()
    index = {}
    
    # Iteramos el indice y la letra dentro de nuestra palabra.
    # enumerate() agrega un contador a un iterable y lo devuelve en forma de objeto enumerado
    # en este caso, nuestra palabra.
    for idx, letter in enumerate(without_accent):
        #print(f'index: {idx}, letter:{letter}')
        #.get() devuelve el valor del elemento con la clave especificada 
        if not index.get(letter): 
            index[letter] = []
        # Agregamos en que indices se repite cada letra
        index[letter].append(idx)
        #print(index)
    hearts = 6
    if hearts == 5:
        print(drawing[2])
    elif hearts == 4:
        print(drawing[3]) 
    elif hearts == 3:
        print(drawing[4]) 
    elif hearts == 2:
        print(drawing[5]) 
    elif hearts == 1:
        print(drawing[6])
    while True:
        # Limpiamos pantalla en cada iteración
        os.system("cls")
        print(drawing[0])
        print(drawing[1])
        print('ʕ•́ᴥ•̀ʔっ ---> ¡Adivina la palabra!\n')
        # Esto representa los guiones de cada letra
        for underscore in list_lines:
            print(underscore + " ", end="")
        print("\n")
        # strip() remueve los espacios al inicio y al final del string
        # upper() pone todo en MAYUSCULAS
        print(f'Vidas: {hearts}')
        char = input("ʕ•́ᴥ•̀ʔっ ---> Ingresa una letra: ").strip().upper()
        # Sumiento que: char.isalpha() = True
        # isalpha() es verdadero si todos los caracteres de la  cadena son letras,
        # si no, por ejemplo, si recibe un número; retornará falso.
        assert char.isalpha(), "ʕ•́ᴥ•̀ʔっ ---> Ingresa letras individuales, pls"

        if char in list_words:
            for idx in index[char]:
                # Asigna a los indices de los underscores la letra
                list_lines[idx] = char
        else:
            hearts = hearts-1
            print('\n Ups! Intenta de nuevo')
            print(f'Vidas: {hearts}')            

        # Si ya no hay undescores en la lista de undescores (solo hay letras)
        if "_" not in list_lines:
            os.system("cls") # Limpia pantalla
            print("¡Ah prro! Acertaste la palabra que era", without_accent)
            break
            
        
        
        elif hearts == 0:
            print('\n( ͡° ͜ʖ ͡°) ----> ¡Perdiste!\n')
            print(f'{drawing[7]}\n')
            print(f'\n{drawing[8]}')
            break
    
def run():

    word = getting_word() 
    without_accent = without_accent_mark(word)
    juega(without_accent)

if __name__ == '__main__':
    run()