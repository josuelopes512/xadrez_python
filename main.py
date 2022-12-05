import os

from xadrez.Tela import Tela
from xadrez.tabuleiro.TabuleiroException import TabuleiroException
from xadrez.xadrez.PartidaXadrez import PartidaXadrez
from xadrez.xadrez.RealizarJogada import RealizaJogada


try:
    partida = RealizaJogada()

    while (not partida.terminada):
        try:
            Tela.imprimirPartida(partida)
            
            print("\n")
            print("Origem: ")
            origem = Tela.lerPosicaoXadrez().ToPosicao()
            partida.validarPosicaoDeOrigem(origem)
            
            posicoesPossiveis = partida.tabuleiro.peca(origem).movimentosPossiveis()
            
            os.system('cls')
            Tela.imprimirTabuleiro(partida.tabuleiro, posicoesPossiveis)
            
            print("\n")
            print("Destino: ")
            destino = Tela.lerPosicaoXadrez().ToPosicao()
            partida.validarPosicaoDeDestino(origem, destino)

            partida.realizarJogada(origem, destino)
            
        except TabuleiroException as te:
            print(te)
        except Exception as e:
            print(e)
    Tela.imprimirPartida(partida)
except TabuleiroException as te:
    print(te)
except Exception as e:
    print(e)

