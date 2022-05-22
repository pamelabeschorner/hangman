from random import choice
from forca import Forca
import os

class Partida:

    def __init__(self):
        self.forca = Forca()
        self.chegou_no_fim = False
        self.alfabeto = "abcdefghijklmnopqrstuvxwyz"
        self.lista = ["Amendoim", "Banheiro", "Caatinga", "Casa", "Cachorro", "Campeonato", "Catapora", "Empenhado", "Esparadrapo", "Forca", "Magenta", "Menta", "Moeda", "Palavra", "Pneumonia"]
        self.limite_de_erros = 6
        self.palavra = choice(self.lista).lower()
        self.numero_de_erros = 0
        self.letras_escolhidas = []

    def imprimirPalavra(self):
        for letra in self.palavra:
            if letra in self.letras_escolhidas:
                print(letra, end = " ")
            else:
                print("_", end =" ")

    def imprimirListaDeLetrasEscolhidas(self):
        if self.numero_de_erros < 5:
            print("\n\nAs seguintes letras ja foram escolhidas: " + str(self.letras_escolhidas))
        else:
            print(" ")

    def imprimirNumeroDeTentativas(self):
        restante = self.limite_de_erros - self.numero_de_erros
        if restante > 1:
            print("\nVocê tem " + str(restante) + " chances.\n")
        else:
            print("\nSua última chance, use com sabedoria: \n")

    def imprimirResultadoFinal(self):
        if self.chegouNoFimPorSucesso():
            print("\nParabéns! Você venceu!!" + "\n" + '\033[1m' + self.palavra + '\033[1m')
        else:
            print("\nVocê perdeu! Mais sorte na próxima." + "\nA palavra correta era " + '\033[1m'  + self.palavra + '\033[1m')

    def chegouNoFimPorSucesso(self):
        sucesso = True
        for letra in self.palavra:
            if letra not in self.letras_escolhidas:
                sucesso = False
        return sucesso

    def chegouNoFimPorFalha(self):
        self.numero_de_erros = self.numero_de_erros + 1
        if self.numero_de_erros < self.limite_de_erros:
            return False
        else:
            return True

    def imprimir_estado_da_partida(self):
        self.forca.imprimir(self.numero_de_erros)
        self.imprimirPalavra()
        self.imprimirListaDeLetrasEscolhidas()
        self.imprimirNumeroDeTentativas()

    def input_valido(self, input_usuario):
        if input_usuario in self.letras_escolhidas:
            print("\nEssa letra ja foi escolhida.")
            return False

        elif len(input_usuario) != 1:
            print("\nDigite apenas UMA letra por tentativa.")
            return False

        elif input_usuario not in self.alfabeto:
            print("\nIsso não é uma letra.")
            return False
        else:
            return True


    def jogar(self):
        while not self.chegou_no_fim:
            self.imprimir_estado_da_partida()
            letra_escolhida = input("Digite uma letra: ").lower()
            os.system('clear')
            if self.input_valido(letra_escolhida):
                self.letras_escolhidas.append(letra_escolhida)
                if letra_escolhida in self.palavra:
                    self.chegou_no_fim = self.chegouNoFimPorSucesso()
                else:
                    self.chegou_no_fim = self.chegouNoFimPorFalha()
        self.imprimirResultadoFinal()
