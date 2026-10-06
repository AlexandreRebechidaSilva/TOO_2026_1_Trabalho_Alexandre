from model.heroi import Heroi
from model.missao import Mis_combate, Mis_coleta, Mis_transporte
from model.inimigo import Inimigo
from model.enums import ClasseHeroi, TipoInimigo


def main():
    heroi = Heroi("Dante", ClasseHeroi.GUERREIRO, 100, 100, 10, 5)
    inimigo = Inimigo("Goblin", TipoInimigo.GOBLIN, 50, 50, 8, 3)

    missoes = [
        Mis_combate("Defender a vila", "Derrotar o goblin", 100, inimigo,2,25),
        Mis_coleta("Coletar ervas", "Encontrar ervas medicinais", 20, "Erva", 5,20),
        Mis_transporte("Levar suprimentos", "Transportar uma carga", 20, "Suprimentos", 3,15,100),
    ]

    for indice, missao in enumerate(missoes):
        print(missao.iniciar_missao())
        if indice == 0:
            print("\nHerói antes da primeira missão:")
            print(heroi.exibir_dados())

        missao.concluir_missao(heroi)

        if indice == 0:
            print("\nHerói depois da primeira missão:")
            print(heroi.exibir_dados())

    try:
        missoes[0].status = "STATUS INVÁLIDO"
    except ValueError as erro:
        print(f"\nErro tratado: {erro}")


if __name__ == "__main__":
    main()