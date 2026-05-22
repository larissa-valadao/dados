from modelos.restaurante import Restaurante

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_praca.receber_avaliacao('Gui', 3.55)
restaurante_praca.receber_avaliacao('Lais', 0.2)
restaurante_praca.receber_avaliacao('Emy', 10)
restaurante_praca.alternar_estado()

def main():
    Restaurante.listar_restaurantes()

if __name__ == '__main__':
    main()