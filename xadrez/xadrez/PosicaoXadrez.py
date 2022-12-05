from xadrez.tabuleiro.Posicao import Posicao

class PosicaoXadrez:
    def __init__(self, coluna, linha):
        self.linha = linha
        self.coluna = coluna
    
    def __str__(self):
        return f"{self.coluna}{self.linha}"
    
    def ToPosicao(self):
        return Posicao(8 - self.linha, ord(self.coluna) - ord('a'))