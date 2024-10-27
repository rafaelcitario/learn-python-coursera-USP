# n = pecas iniciais
# m = maximo qe pode tirar
# regra n % (m + 1) == 0 Jogador começa
# regra n %(m + 1) != 0 Comp começa


def computador_escolhe_jogada(n: int, m: int) -> int:
    mult = m + 1
    print(n % (mult) != 0 and n - mult >= 1)
    if n % (mult) != 0 and n - mult >= 1:
        takeNumber = n - mult
        return takeNumber
    return m


def jogador_escolhe_jogada(n: int, m: int) -> int:
    player = m + 1
    while player > m:
        print("Oops! Jogada inválida! Tente de novo")
        player = int(input("Quantas peças você vai tirar? "))
        if player <= m:
            break
    return player


def partida():
    pieces = int(input("Quantas peças? "))
    limitToTake = int(input("Limite de peças por jogada? "))
    computerTaken = 0
    playerTaken = 0
    start = True
    while pieces > 0:
        if pieces % (limitToTake + 1) != 0:
            if(start):
                print("Computador começa!")
                start = False
            computerTaken = computador_escolhe_jogada(pieces, limitToTake)
            print("Computador tirou %d peça." % playerTaken)
            print("Agora resta apenas %d peça no tabuleiro." % pieces)
            pieces = pieces - computerTaken
        else:
            if(start):
                print("Você começa!")
                start = False
            playerTaken = jogador_escolhe_jogada(pieces, limitToTake)
            pieces = pieces - playerTaken
            print("Você tirou %d peça." % playerTaken)
            print("Agora resta apenas %d peça no tabuleiro." % pieces)

        if pieces <= 0:
            print("Fim do jogo! O computador ganhou!")
            break


def main():
    playMode = 3
    gameMode = ["Voce escolheu uma partida!", "Voce escolheu um campeonato!"]
    print("Bem-vindo ao jogo do NIM! Escolha:\n")
    while playMode != 1 and playMode != 2:
       playMode = int(input("1 - para jogar uma partida isolada\n2 - para jogar um campeonato "))

    print(playMode)
    print(gameMode[0 if playMode == 1 else 1])
    if playMode != 1:
        for i in range(1, 4):
            print("**** Rodada %d ****" % i)
            partida()
    else:
        print("**** Rodada %d ****" % 1)
        partida()


main()
