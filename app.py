from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'gourmet')

restaurante_praca.receber_avaliacao('Guilherme', 4)
restaurante_praca.receber_avaliacao('Gabriel', 3)
restaurante_praca.receber_avaliacao('Rafaela', 5)


def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()