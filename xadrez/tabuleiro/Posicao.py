

class Posicao:
    def __init__(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
    
    def definirValores(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna
    
    def __str__(self):
        return f"{self.linha}, {self.coluna}."