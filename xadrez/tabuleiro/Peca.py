from abc import ABC, abstractmethod
import random


class Peca(ABC):
    def __init__(self):
        pass
    
    def __init__(self, tabuleiro, cor):
        self.tabuleiro = tabuleiro
        self.cor = cor
        self.posicao = None
        self.qteMovimentos = 0
        self.__hash__()
    
    def __hash__(self):
        self.hash = random.getrandbits(128)
    
    def incrementarMovimentos(self):
        self.qteMovimentos += 1
    
    def decrementarQteMovimentos(self):
        self.qteMovimentos -= 1
    
    def existeMovimentosPossiveis(self):
        mov = self.movimentosPossiveis()
        for i in range(self.tabuleiro.linhas):
            for j in range(self.tabuleiro.colunas):
                if (mov[i][j]):
                    return True
        return False
    
    def movimentoPossivel(self, posicao):
        return self.movimentosPossiveis()[posicao.linha][posicao.coluna]
    
    @abstractmethod
    def movimentosPossiveis(self):
        pass