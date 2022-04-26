def run():
    my_set1 = {'Hola', 34, 45.5, False, 'Adios', 'pikachu', 'planta', 'balon'}
    my_set2 = {5, True, 'bienvenido', 'bulbasaur', 'pikachu', 34, 'raqueta', 'balon'}
    
    my_set3 = my_set1 | my_set2
    my_set4 = my_set1 & my_set2
    my_set5 = my_set2 - my_set1
    my_set6 = my_set1 - my_set2
    my_set7 = my_set1 ^ my_set2

    print(my_set3)
    print(my_set4)
    print(my_set5)
    print(my_set6)
    print(my_set7)

    # lista = [1, 1, 2, 2, 4]
    # print(set(lista))

if __name__ == '__main__':
    run()