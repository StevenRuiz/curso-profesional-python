def es_primo(numero: int)-> bool:
    return numero%2 != 0


def run():
    print(es_primo(7))


if __name__ == '__main__':
    run()