from xadrez.tabuleiro.TabuleiroException import TabuleiroException
from xadrez.utils.Hashset import HashSet

from xadrez.tabuleiro.Peca import Peca
from xadrez.tabuleiro.Posicao import Posicao
from xadrez.tabuleiro.Tabuleiro import Tabuleiro
from xadrez.tabuleiro.Cor import Cor

from xadrez.xadrez.PosicaoXadrez import PosicaoXadrez
from xadrez.xadrez.Torre import Torre
from xadrez.xadrez.Cavalo import Cavalo
from xadrez.xadrez.Dama import Dama
from xadrez.xadrez.Bispo import Bispo
from xadrez.xadrez.Peao import Peao
from xadrez.xadrez.Rei import Rei


class PartidaXadrez:
    def __init__(self):
        self.tabuleiro = Tabuleiro(8, 8)
        self.turno = 1
        self.jogadorAtual = Cor.BRANCO
        self.xeque = False
        self.vulneravelEnPassant = None
        self.terminada = False
        self.pecas = HashSet()
        self.capturadas = HashSet()
        self.colocarPecas()
    
    def colocarNovaPeca(self, coluna, linha, peca):
        self.tabuleiro.colocarPeca(PosicaoXadrez(coluna, linha).ToPosicao(), peca)
        self.pecas.add(peca)
    
    def colocarPecas(self):
        x = "abcdefgh"

        self.colocarNovaPeca("a", 1, Torre(self.tabuleiro, Cor.BRANCO))
        self.colocarNovaPeca("b", 1, Cavalo(self.tabuleiro, Cor.BRANCO))
        self.colocarNovaPeca("c", 1, Bispo(self.tabuleiro, Cor.BRANCO))
        self.colocarNovaPeca("d", 1, Dama(self.tabuleiro, Cor.BRANCO))
        self.colocarNovaPeca("e", 1, Rei(self.tabuleiro, Cor.BRANCO, self))
        self.colocarNovaPeca("f", 1, Bispo(self.tabuleiro, Cor.BRANCO))
        self.colocarNovaPeca("g", 1, Cavalo(self.tabuleiro, Cor.BRANCO))
        self.colocarNovaPeca("h", 1, Torre(self.tabuleiro, Cor.BRANCO))

        for item in x:
            self.colocarNovaPeca(item, 2, Peao(self.tabuleiro, Cor.BRANCO, self))


        self.colocarNovaPeca("a", 8, Torre(self.tabuleiro, Cor.PRETO))
        self.colocarNovaPeca("b", 8, Cavalo(self.tabuleiro, Cor.PRETO))
        self.colocarNovaPeca("c", 8, Bispo(self.tabuleiro, Cor.PRETO))
        self.colocarNovaPeca("d", 8, Dama(self.tabuleiro, Cor.PRETO))
        self.colocarNovaPeca("e", 8, Rei(self.tabuleiro, Cor.PRETO, self))
        self.colocarNovaPeca("f", 8, Bispo(self.tabuleiro, Cor.PRETO))
        self.colocarNovaPeca("g", 8, Cavalo(self.tabuleiro, Cor.PRETO))
        self.colocarNovaPeca("h", 8, Torre(self.tabuleiro, Cor.PRETO))

        for item in x:
            self.colocarNovaPeca(item, 7, Peao(self.tabuleiro, Cor.PRETO, self))
    
    def validarPosicaoDeOrigem(self, pos):
        peca = self.tabuleiro.peca(pos)
        if (peca == None):
            raise TabuleiroException("Não existe peça na posição de origem escolhida!")
        
        if(self.jogadorAtual != peca.cor):
            raise TabuleiroException("A peça na posição de origem escolhida não é sua!")

        if (not peca.existeMovimentosPossiveis()):
            raise TabuleiroException("Não há movimentos possiveis para a peça de origem escolhida!")

    def validarPosicaoDeDestino(self, origem, destino):
        if (not self.tabuleiro.peca(origem).movimentoPossivel(destino)):
            raise TabuleiroException("Posição de destino invalida!")

