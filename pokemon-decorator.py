def answer(func):
    def wrapper_question(*args, **kwargs):
        print('¿Quién es ese Pokémon?')
        func(*args, **kwargs)
    return wrapper_question


def type_pokemon(func):
    def wrapper_type(*args, **kwargs):
        print('Es de tipo PLANTA')
        func(*args, **kwargs)
    return wrapper_type

@answer
def question(pokemon="Ivysaur"):
    print('¡Es: ' + pokemon + '!')
    print('Es el número 2')


@type_pokemon
def second_type_pokemon():
    print('Ademas es de tipo VENENO')
    print('Aun puede evolucionar')


def run():
    question()
    second_type_pokemon()


if __name__ == '__main__':
    run()