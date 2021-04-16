def main():
    dict_naturals = {key: key**3 for key in range(101)}
    print(f'Dictionary comprehensions:\n{dict_naturals}')
    
if __name__ == '__main__':
    main()