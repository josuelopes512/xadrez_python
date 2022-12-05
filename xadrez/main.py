import os

from Tela import Tela
from tabuleiro.TabuleiroException import TabuleiroException
from xadrez.PartidaXadrez import PartidaXadrez
from xadrez.RealizarJogada import RealizaJogada


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
            pass
        except Exception as e:
            pass
    Tela.imprimirPartida(partida)
except TabuleiroException as te:
    pass
except Exception as e:
    pass

