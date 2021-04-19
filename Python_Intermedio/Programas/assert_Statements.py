def divisors(num):
    divisors = []
    for i in range (1, num + 1):
        if num % i == 0:
            divisors.append(i)
    return divisors

def run():
    num = input('Ingrese un número para obtener sus divisores: ')
    assert num.isnumeric(), "\nʕ•́ᴥ•̀ʔっ ---> Debes ingresar un número."
    # Si la afirmación es verdadera pasalo a entero
    print(divisors(int(num)))


if __name__ == '__main__':
    run()