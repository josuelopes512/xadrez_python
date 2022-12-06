from xadrez.tabuleiro.Cor import Cor
from xadrez.tabuleiro.Peca import Peca
from xadrez.tabuleiro.Posicao import Posicao


class Peao(Peca):
    def __init__(self, tab, cor, partida):
        super().__init__(tab, cor)
        self.partida = partida

    def __str__(self):
        return "P"

    def podeMover(self, pos):
        p = self.tabuleiro.peca(pos)
        return p == None or p.cor != self.cor

    def __crie_matriz(self, n_linhas, n_colunas):
        matriz = []
        valor = False
        for _ in range(n_linhas):
            linha = []
            for _ in range(n_colunas):
                linha += [valor]
            matriz += [linha]

        return matriz

    def existeInimigo(self, pos):
        p = self.tabuleiro.peca(pos)
        return p != None and p.cor != self.cor

    def movimentosPossiveis(self):
        mat = self.__crie_matriz(self.tabuleiro.linhas, self.tabuleiro.colunas)

        posicao = Posicao(0, 0)

        if (self.cor == Cor.BRANCO):
            posicao.definirValores(self.posicao.linha - 1, self.posicao.coluna)
            if (self.tabuleiro.posicaoValida(posicao) and self.tabuleiro.livre(posicao)):
                mat[posicao.linha][posicao.coluna] = True

            posicao.definirValores(self.posicao.linha - 2, self.posicao.coluna)
            posicao_2 = Posicao(self.posicao.linha - 1, self.posicao.coluna)
            if (self.tabuleiro.posicaoValida(posicao_2) and self.tabuleiro.livre(posicao_2) and self.tabuleiro.posicaoValida(posicao) and self.tabuleiro.livre(posicao) and self.qteMovimentos == 0):
                mat[posicao.linha][posicao.coluna] = True

            posicao.definirValores(
                self.posicao.linha - 1, self.posicao.coluna - 1)
            if (self.tabuleiro.posicaoValida(posicao) and self.existeInimigo(posicao)):
                mat[posicao.linha][posicao.coluna] = True

            posicao.definirValores(
                self.posicao.linha - 1, self.posicao.coluna + 1)
            if (self.tabuleiro.posicaoValida(posicao) and self.existeInimigo(posicao)):
                mat[posicao.linha][posicao.coluna] = True

            if (posicao.linha == 3):
                posicao_esquerda = Posicao(posicao.linha, posicao.coluna - 1)
                if (self.tabuleiro.posicaoValida(posicao_esquerda) and self.existeInimigo(posicao_esquerda) and self.tabuleiro.peca(posicao_esquerda) == self.partida.vulneravelEnPassant):
                    mat[posicao.linha - 1][posicao.coluna] = True

                posicao_direita = Posicao(posicao.linha, posicao.coluna + 1)
                if (self.tabuleiro.posicaoValida(posicao_direita) and self.existeInimigo(posicao_direita) and self.tabuleiro.peca(posicao_direita) == self.partida.vulneravelEnPassant):
                    mat[posicao.linha - 1][posicao.coluna] = True
        else:
            posicao.definirValores(self.posicao.linha + 1, self.posicao.coluna)
            if (self.tabuleiro.posicaoValida(posicao) and self.tabuleiro.livre(posicao)):
                mat[posicao.linha][posicao.coluna] = True

            posicao.definirValores(self.posicao.linha + 2, self.posicao.coluna)
            posicao_2 = Posicao(self.posicao.linha + 1, self.posicao.coluna)
            if (self.tabuleiro.posicaoValida(posicao_2) and self.tabuleiro.livre(posicao_2) and self.tabuleiro.posicaoValida(posicao) and self.tabuleiro.livre(posicao) and self.qteMovimentos == 0):
                mat[posicao.linha][posicao.coluna] = True

            posicao.definirValores(
                self.posicao.linha + 1, self.posicao.coluna - 1)
            if (self.tabuleiro.posicaoValida(posicao) and self.existeInimigo(posicao)):
                mat[posicao.linha][posicao.coluna] = True

            posicao.definirValores(
                self.posicao.linha + 1, self.posicao.coluna + 1)
            if (self.tabuleiro.posicaoValida(posicao) and self.existeInimigo(posicao)):
                mat[posicao.linha][posicao.coluna] = True

            if (posicao.linha == 4):
                posicao_esquerda = Posicao(posicao.linha, posicao.coluna - 1)
                if (self.tabuleiro.posicaoValida(posicao_esquerda) and self.existeInimigo(posicao_esquerda) and self.tabuleiro.peca(posicao_esquerda) == self.partida.vulneravelEnPassant):
                    mat[posicao.linha + 1][posicao.coluna] = True

                posicao_direita = Posicao(posicao.linha, posicao.coluna + 1)
                if (self.tabuleiro.posicaoValida(posicao_direita) and self.existeInimigo(posicao_direita) and self.tabuleiro.peca(posicao_direita) == self.partida.vulneravelEnPassant):
                    mat[posicao.linha + 1][posicao.coluna] = True

        return mat
