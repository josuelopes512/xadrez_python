from xadrez.tabuleiro.Cor import Cor
from xadrez.tabuleiro.Peca import Peca
from xadrez.tabuleiro.Posicao import Posicao
from xadrez.xadrez.Torre import Torre


class Rei(Peca):
    def __init__(self, tab, cor, partida):
        super().__init__(tab, cor)
        self.partida = partida

    def __str__(self):
        return "R"

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

    def testeTorreParaRoque(self, pos):
        p = self.tabuleiro.peca(pos)
        return p != None and isinstance(p, Torre) and p.cor != self.cor and p.qteMovimentos == 0

    def movimentosPossiveis(self):
        mat = self.__crie_matriz(self.tabuleiro.linhas, self.tabuleiro.colunas)

        posicao = Posicao(0, 0)

        # ESQUERDA
        posicao.definirValores(self.posicao.linha, self.posicao.coluna - 1)
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True

        # DIREITA
        posicao.definirValores(self.posicao.linha, self.posicao.coluna + 1)
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        # ACIMA
        posicao.definirValores(self.posicao.linha - 1, self.posicao.coluna)
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        # ABAIXO
        posicao.definirValores(self.posicao.linha + 1, self.posicao.coluna - 1)
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        # NO
        posicao.definirValores(self.posicao.linha - 1, self.posicao.coluna - 1)
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True

        # NE
        posicao.definirValores(self.posicao.linha - 1, self.posicao.coluna + 1)
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True

        # SE
        posicao.definirValores(self.posicao.linha + 1, self.posicao.coluna + 1)
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True

        # SO
        posicao.definirValores(self.posicao.linha + 1, self.posicao.coluna - 1)
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True

        if (self.qteMovimentos == 0 and not self.partida.xeque):
            posT1 = Posicao(self.posicao.linha, self.posicao.coluna + 3)
            if (self.testeTorreParaRoque(posT1)):
                p1 = Posicao(posicao.linha, posicao.coluna + 1)
                p2 = Posicao(posicao.linha, posicao.coluna + 2)
                if (self.tabuleiro.peca(p1) == None and self.tabuleiro.peca(p2) == None):
                    mat[posicao.linha][posicao.coluna + 2] = True
            
            posT2 = Posicao(self.posicao.linha, self.posicao.coluna - 4)
            if (self.testeTorreParaRoque(posT2)):
                p1 = Posicao(posicao.linha, posicao.coluna - 1)
                p2 = Posicao(posicao.linha, posicao.coluna - 2)
                p3 = Posicao(posicao.linha, posicao.coluna - 3)
                
                if (not any([self.tabuleiro.peca(p1), self.tabuleiro.peca(p2), self.tabuleiro.peca(p3)])):
                    mat[posicao.linha][posicao.coluna - 2] = True

        return mat
