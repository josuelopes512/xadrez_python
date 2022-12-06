from xadrez.tabuleiro.Cor import Cor
from xadrez.xadrez.PosicaoXadrez import PosicaoXadrez

class Tela:
    @staticmethod
    def imprimirPartida(partida):
        Tela.imprimirTabuleiro(partida.tabuleiro)
        print("\n")
        Tela.imprimirPecasCapturadas(partida)
        print("\n")
        print(f"Turno: {partida.turno}")
        
        if (not partida.terminada):
            print(f"Aguardando jogada: {partida.jogadorAtual}")
            if (partida.xeque):
                print("XEQUE!")
        else:
            print("XEQUEMATE!")
            print("Vencedor: " + partida.jogadorAtual)
    
    def lerPosicaoXadrez():
        s = input().strip()
        coluna = s[0]
        linha = int(s[1])
        return PosicaoXadrez(coluna, linha)
    
    @staticmethod
    def imprimirConjunto(conjunto):
        print("[")

        for x in conjunto.toList():
            print(x + " ")

        print("]")
    
    @staticmethod
    def imprimirPecasCapturadas(partida):
        print("Peças capturadas: ")
        print("Brancas: ")
        Tela.imprimirConjunto(partida.pecasCapturadas(Cor.BRANCO))
        print("\n")
        print("Pretas: ")
        Tela.imprimirConjunto(partida.pecasCapturadas(Cor.PRETO))
        print("\n")
    
    #@staticmethod
    #def imprimirTabuleiro(tabuleiro):
    #    for i in range(0, tabuleiro.linhas):
    #        print(8 - i + " ")
    #        for j in range(0, tabuleiro.colunas):
    #            Tela.imprimirPeca(tabuleiro.peca(i, j))
    #        print("\n")
    #    print("  A B C D E F G H")
    
    @staticmethod
    def imprimirTabuleiro(tabuleiro, posicoesPossiveis=None):
        if posicoesPossiveis:
            for i in range(0, tabuleiro.linhas):
                x = str(8-i)
                print(f"{x} ")
                data_print = ""
                for j in range(0, tabuleiro.colunas):
                    peca = tabuleiro.peca((i, j))
                    if (not peca):
                        data_print += "- "
                    else:
                        data_print += f"{peca} "
                print(data_print.strip())
            print("  A B C D E F G H")
        else:
            for i in range(0, tabuleiro.linhas):
                data_print = ""
                for j in range(0, tabuleiro.colunas):
                    peca = tabuleiro.peca((i, j))
                    if (not peca):
                        data_print += "- "
                    else:
                        data_print += f"{peca} "
                print(data_print.strip())
    
    @staticmethod
    def imprimirPeca(peca):
        if (not peca):
            print("- ")
        else:
            if (peca.cor == Cor.BRANCO):
                print(peca)
            else:
                print(peca)
            print(" ")