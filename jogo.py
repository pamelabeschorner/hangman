from partida import Partida

class Jogo:
    def __init__(self):
        self.chegou_no_fim = False

    def jogar(self):
        while not self.chegou_no_fim:
            partida = Partida()
            partida.jogar()
            jogar_novamente = input("\nVocê gostaria de jogar novamente? ")
            if jogar_novamente == "sim":
                self.chegou_no_fim = False
            else:
                self.chegou_no_fim = True

