from xadrez.tabuleiro.Peca import Peca
from xadrez.tabuleiro.Posicao import Posicao
from xadrez.tabuleiro.TabuleiroException import TabuleiroException


class Tabuleiro:
    def __init__(self, linhas, colunas):
        self.linhas = linhas
        self.colunas = colunas
        self.pecas = self.__crie_matriz(linhas, colunas, None)

    def __crie_matriz(self, n_linhas, n_colunas, valor):
        matriz = []  # lista vazia
        for i in range(n_linhas):
            # cria a linha i
            linha = []  # lista vazia
            for j in range(n_colunas):
                linha += [valor]

            # coloque linha na matriz
            matriz += [linha]

        return matriz

    def peca(self, pos):
        if(isinstance(pos, Posicao)):
            pecas = self.pecas[pos.linha][pos.coluna]
            return pecas
        elif isinstance(pos, tuple):
            linha, coluna = pos
            return self.pecas[linha][coluna]
    
    def livre(self, pos):
        return self.peca(pos) == None

    def posicaoValida(self, pos):
        if(pos.linha < 0 or pos.linha >= self.linhas or pos.coluna < 0 or pos.coluna >= self.colunas):
            return False
        return True

    def validarPosicao(self, pos):
        if(not self.posicaoValida(pos)):
            raise TabuleiroException("Posição Invalida!")

    def existePeca(self, pos):
        self.validarPosicao(pos)
        peca = self.peca(pos)
        return peca is not None
    
    def retirarPeca(self, pos):
        if (self.livre(pos)):
            return None
        
        aux = self.peca(pos)
        aux.posicao = None
        
        self.pecas[pos.linha][pos.coluna] = None
        return aux
    
    def colocarPeca(self, pos, p):
        exists = self.existePeca(pos)
        if (exists):
            raise TabuleiroException("Ja existe uma pessa nessa posição!")
        
        p.posicao = pos
        self.pecas[pos.linha][pos.coluna] = p
