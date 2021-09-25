from models.calcular import Calcular


def main() -> None:
    pontos: int = 0
    jogar(pontos)


def jogar(pontos: int) -> None:
    print(100 * '\n')
    dificuldade: int = int(input('Informe o nível de dificuldade desejado [1, 2, 3 ou 4]: \n>> '))

    calc: Calcular = Calcular(dificuldade)

    print('\n-------\nInforme o resultado para a seguinte operação: ')
    calc.mostrar_operacao()

    resultado: int = int(input('>> '))

    if calc.checar_resultado(resultado):
        pontos += 1
        print(f'Você tem {pontos} pontos(s).\n-------')

    continuar: int = int(input('Deseja continuar no jogo? [1 - sim, 0 - não] \n>> '))

    if continuar:
        jogar(pontos)
    else:
        print(f'Você finalizou com {pontos} ponto(s).')
        print('Até a próxima!')


if __name__ == '__main__':
    main()

