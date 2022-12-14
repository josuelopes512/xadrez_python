from xadrez.tabuleiro.Cor import Cor
from xadrez.tabuleiro.Peca import Peca
from xadrez.tabuleiro.Posicao import Posicao
from xadrez.tabuleiro.TabuleiroException import TabuleiroException
from xadrez.utils.Hashset import HashSet
from xadrez.xadrez.Bispo import Bispo
from xadrez.xadrez.Cavalo import Cavalo
from xadrez.xadrez.Dama import Dama
from xadrez.xadrez.PartidaXadrez import PartidaXadrez
from xadrez.xadrez.Peao import Peao
from xadrez.xadrez.Rei import Rei
from xadrez.xadrez.Torre import Torre


class RealizaJogada(PartidaXadrez):
    def __init__(self):
        super().__init__()

    def executarMovimento(self, origem, destino):
        p = self.tabuleiro.retirarPeca(origem)
        p.incrementarMovimentos()
        pecaCapturada = self.tabuleiro.retirarPeca(destino)
        self.tabuleiro.colocarPeca(destino, p)
        if (pecaCapturada != None):
            self.capturadas.add(pecaCapturada)

        # jogadaespecial roque pequeno
        if (isinstance(p, Rei) and destino.coluna == origem.coluna + 2):
            origemT = Posicao(origem.linha, origem.coluna + 3)
            destinoT = Posicao(origem.linha, origem.coluna + 1)
            T = self.tabuleiro.retirarPeca(origemT)
            T.incrementarMovimentos()
            self.tabuleiro.colocarPeca(destinoT, T)

        # jogadaespecial roque grande
        if (isinstance(p, Rei) and destino.coluna == origem.coluna - 2):
            origemT = Posicao(origem.linha, origem.coluna - 4)
            destinoT = Posicao(origem.linha, origem.coluna - 1)
            T = self.tabuleiro.retirarPeca(origemT)
            T.incrementarMovimentos()
            self.tabuleiro.colocarPeca(destinoT, T)

        # jogadaespecial en passant
        if (isinstance(p, Peao)):
            if (origem.coluna != destino.coluna and pecaCapturada == None):
                posP = None
                if (p.cor == Cor.BRANCO):
                    posP = Posicao(destino.linha + 1, destino.coluna)
                else:
                    posP = Posicao(destino.linha - 1, destino.coluna)

                pecaCapturada = self.tabuleiro.retirarPeca(posP)
                self.capturadas.add(pecaCapturada)

        return pecaCapturada

    def pecasCapturadas(self, cor):
        aux = HashSet()
        for x in self.capturadas.toList():
            peca = self.pecas.get(x)

            if not peca:
                continue

            if not isinstance(peca, Peca):
                continue

            if (peca.cor == cor):
                aux.add(x)
        return aux

    def pecasEmJogo(self, cor):
        aux = HashSet()
        for x in self.pecas.toList():
            peca = self.pecas.get(x)

            if not peca:
                continue

            if not isinstance(peca, Peca):
                continue

            if (peca.cor == cor):
                aux.add(x)
        aux.ExceptWith(self.pecasCapturadas(cor))
        return aux

    def rei(self, cor):
        for x in self.pecasEmJogo(cor).toList():
            peca = self.pecas.get(x)

            if not peca:
                continue

            if not isinstance(peca, Peca):
                continue

            if (isinstance(peca, Rei)):
                return peca
        return None

    def adversaria(self, cor):
        if (cor == Cor.BRANCO):
            return Cor.PRETO
        else:
            return Cor.BRANCO

    def estaEmXeque(self, cor):
        R = self.rei(cor)
        if (R == None):
            raise TabuleiroException(
                "N??o tem rei da cor " + cor + " no tabuleiro!")

        for x in self.pecasEmJogo(self.adversaria(cor)).toList():
            mat = x.movimentosPossiveis()
            if (mat[R.posicao.linha][R.posicao.coluna]):
                return True
        return False

    def desfazMovimento(self, origem, destino, pecaCapturada):
        p = self.tabuleiro.retirarPeca(destino)
        p.decrementarQteMovimentos()
        if (pecaCapturada != None):
            self.tabuleiro.colocarPeca(destino, pecaCapturada)
            self.capturadas.remove(pecaCapturada)
        self.tabuleiro.colocarPeca(origem, p)

        # #jogadaespecial roque pequeno
        if (isinstance(p, Rei) and destino.coluna == origem.coluna + 2):
            origemT = Posicao(origem.linha, origem.coluna + 3)
            destinoT = Posicao(origem.linha, origem.coluna + 1)
            T = self.tabuleiro.retirarPeca(destinoT)
            T.decrementarQteMovimentos()
            self.tabuleiro.colocarPeca(origemT,  T)

        # #jogadaespecial roque grande
        if (isinstance(p, Rei) and destino.coluna == origem.coluna - 2):
            origemT =  Posicao(origem.linha, origem.coluna - 4)
            destinoT =  Posicao(origem.linha, origem.coluna - 1)
            T = self.tabuleiro.retirarPeca(destinoT)
            T.decrementarQteMovimentos()
            self.tabuleiro.colocarPeca(origemT, T)

        # #jogadaespecial en passant
        if (isinstance(p, Peao)):
            if (origem.coluna != destino.coluna and pecaCapturada == self.vulneravelEnPassant):
                peao = self.tabuleiro.retirarPeca(destino)
                posP = Posicao(3, destino.coluna) if (p.cor == Cor.BRANCO) else Posicao(4, destino.coluna)
                self.tabuleiro.colocarPeca(posP, peao)
    
    def estaEmXeque(self, cor):
        R = self.rei(cor)
        if (R == None):
            raise TabuleiroException("N??o tem rei da cor " + cor + " no tabuleiro!");
        adv_cor = self.adversaria(cor)
        for x in self.pecasEmJogo(adv_cor).toList():
            peca = self.pecas.get(x)

            if not peca:
                continue

            if not isinstance(peca, Peca):
                continue

            mat = peca.movimentosPossiveis()
            if (mat[R.posicao.linha][R.posicao.coluna]):
                return True
        return False

    def testeXequemate(self, cor):
        if (not self.estaEmXeque(cor)):
            return False
        for x in self.pecasEmJogo(cor).toList():
            peca = self.pecas.get(x)

            if not peca:
                continue

            if not isinstance(peca, Peca):
                continue


            mat = x.movimentosPossiveis()
            for i in range(0, self.tabuleiro.linhas):
                for j in range(0, self.tabuleiro.colunas):
                    if (mat[i][j]):
                        origem = x.posicao
                        destino = Posicao(i, j)
                        pecaCapturada = self.executarMovimento(origem, destino)
                        testeXeque = self.estaEmXeque(cor)
                        self.desfazMovimento(origem, destino, pecaCapturada)
                        if (not testeXeque):
                            return False
        return True
    
    def mudaJogador(self):
        if(self.jogadorAtual == Cor.BRANCO):
            self.jogadorAtual = Cor.PRETO
        else:
            self.jogadorAtual = Cor.BRANCO
    
    def realizarJogada(self, origem, destino):
        pecaCapturada = self.executarMovimento(origem, destino)
        if (self.estaEmXeque(self.jogadorAtual)):
            self.desfazMovimento(origem, destino, pecaCapturada)
            raise TabuleiroException("Voc?? n??o pode se colocar em xeque!")

        p = self.tabuleiro.peca(destino)

        # jogadaespecial promocao
        if (isinstance(p, Peao)):
        
            if ((p.cor == Cor.BRANCO and destino.linha == 0) or (p.cor == Cor.PRETO and destino.linha == 7)):
                p = self.tabuleiro.retirarPeca(destino)
                self.pecas.remove(p)
                
                print()
                print("#--- PROMO????O! ---#")
                print("Op????es de promo????o:")
                print(
                    " - Dama[D]\n - Torre[T]\n - Bispo[B]\n - Cavalo[C]")
                print("Digite o caractere da op????o escolhida: ")

                escolha = input().upper()
                
                if escolha == 'D':
                    dama = Dama(self.tabuleiro, p.cor)
                    self.tabuleiro.colocarPeca(destino, dama)
                    self.pecas.add(dama)
                elif escolha == 'T':
                    dama = Torre(self.tabuleiro, p.cor)
                    self.tabuleiro.colocarPeca(destino, dama)
                    self.pecas.add(dama)
                elif escolha == 'B':
                    dama = Bispo(self.tabuleiro, p.cor)
                    self.tabuleiro.colocarPeca(destino, dama)
                    self.pecas.add(dama)
                elif escolha == 'C':
                    dama = Cavalo(self.tabuleiro, p.cor)
                    self.tabuleiro.colocarPeca(destino, dama)
                    self.pecas.add(dama)

        if (self.estaEmXeque(self.adversaria(self.jogadorAtual))):
            self.xeque = True
        else:
            self.xeque = False
        

        if (self.testeXequemate(self.adversaria(self.jogadorAtual))):
        
            self.terminada = True
        
        else:
        
            self.turno += 1
            self.mudaJogador()
        

        # jogadaespecial en passant
        if (isinstance(p, Peao) and (destino.linha == origem.linha - 2 or destino.linha == origem.linha + 2)):
            self.vulneravelEnPassant = p
        else:
            self.vulneravelEnPassant = None
