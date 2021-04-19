def divisors(num):
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    try:
        num = int(input('Ingrese un número para obtener sus divisores: '))
        
        if num < 0: 
            raise Exception("\nʕ•́ᴥ•̀ʔっ ---> No puedes ingresar números negativos")
        elif num == 0:
            raise Exception("\nʕ•́ᴥ•̀ʔっ ---> No puedes ingresar el número 0")
        
        print(divisors(num))
        
    except ValueError:
        print("\nʕ•́ᴥ•̀ʔっ ---> Debes de ingresar un número entero")
        
    except Exception as ve:
        print(ve)
        
    except Exception2 as ve2:
        print(ve2)
        
if __name__ == '__main__':
    run()