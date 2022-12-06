from xadrez.tabuleiro.Peca import Peca
from xadrez.tabuleiro.Posicao import Posicao


class Cavalo(Peca):
    def __init__(self, tab, cor):
        super().__init__(tab, cor)
    
    def __str__(self):
        return "C"
    
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
    
    def movimentosPossiveis(self):
        mat = self.__crie_matriz(self.tabuleiro.linhas, self.tabuleiro.colunas)
        
        posicao = Posicao(0, 0)

        posicao.definirValores(self.posicao.linha - 1, self.posicao.coluna - 2)        
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        posicao.definirValores(self.posicao.linha - 2, self.posicao.coluna - 1)        
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        posicao.definirValores(self.posicao.linha - 2, self.posicao.coluna + 1)        
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        posicao.definirValores(self.posicao.linha - 1, self.posicao.coluna + 2)        
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        posicao.definirValores(self.posicao.linha + 1, self.posicao.coluna + 2)        
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        posicao.definirValores(self.posicao.linha + 2, self.posicao.coluna + 1)        
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        posicao.definirValores(self.posicao.linha + 2, self.posicao.coluna - 1)        
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        posicao.definirValores(self.posicao.linha + 1, self.posicao.coluna - 2)        
        if (self.tabuleiro.posicaoValida(posicao) and self.podeMover(posicao)):
            mat[posicao.linha][posicao.coluna] = True
        
        return mat
