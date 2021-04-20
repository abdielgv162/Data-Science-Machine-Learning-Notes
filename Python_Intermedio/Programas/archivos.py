def read():
    numbers = []
    with open("../Programas/archivos/numbers.txt" , "r", encoding="UTF-8") as  f:
        for line in f: 
            numbers.append(int(line))
        print(numbers)

def write():
    names = ["Abdiel", "uwu", ":(", "Holi", "Jesús"]
    with open("../Programas/archivos/names.txt", "w", encoding="UTF-8") as f:
        for name in names:
            f.write(name)
            f.write("\n")

def run():
    write()


if __name__ == '__main__':
    run()