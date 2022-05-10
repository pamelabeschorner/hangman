from random import choice

lista = ["Amendoim", "Banheiro", "Caatinga", "Casa", "Cachorro", "Campeonato", "Catapora", "Empenhado", "Esparadrapo", "Forca", "Magenta", "Menta", "Moeda", "Palavra", "Pneumonia"]
limite_de_erros = 6
chegou_no_fim_do_jogo = False
palavra = None
numero_de_erros = None
chegou_no_fim_da_partida = None
letras_escolhidas = None

def resetar_partida():
    global palavra, numero_de_erros, chegou_no_fim_da_partida, letras_escolhidas
    palavra = choice(lista).lower()
    numero_de_erros = 0
    chegou_no_fim_da_partida = False
    letras_escolhidas = []

def chegouNoFimPorSucesso():
    sucesso = True
    for letra in palavra:
        if letra not in letras_escolhidas:
            sucesso = False
    return sucesso

def chegouNoFimPorFalha():
    global numero_de_erros
    numero_de_erros = numero_de_erros + 1
    if numero_de_erros < limite_de_erros:
        return False
    else:
        return True

def imprimirNumeroDeTentativas():
    restante = limite_de_erros - numero_de_erros
    if restante > 1:
        print("\nVocê tem " + str(restante) + " chances.\n")
    else:
        print("\nSua última chance, use com sabedoria: ")

def imprimirForca():
    global numero_de_erros
    if numero_de_erros == 0:
        print("""
  +---+
  |   |
      |
      |
      |
      |
=========
        """)
    elif numero_de_erros == 1:
        print("""
  +---+
  |   |
  O   |
      |
      |
      |
=========
        """)
    elif numero_de_erros == 2:
        print("""
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
        """)
    elif numero_de_erros == 3:
        print("""
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========
        """)
    elif numero_de_erros == 4:
        print("""
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
        """)
    elif numero_de_erros == 5:
        print("""
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
        """)
    else:
        print("""
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========='
        """)

def imprimirPalavra():
    #print("palavra")
    for letra in palavra:
        if letra in letras_escolhidas:
            print(letra, end = " ")
        else:
            print("_", end =" ")

def imprimirListaDeLetrasEscolhidas():
    if numero_de_erros < 5:
        print("\n\nAs seguintes letras ja foram escolhidas: " + str(letras_escolhidas))
    else:
        print(" ")

def imprimirResultadoFinal():
    if chegouNoFimPorSucesso():
        print("\nParabéns! Você venceu!!" + "\n" + '\033[1m' + palavra + '\033[1m')
    else:
        print("\nVocê perdeu! Mais sorte na próxima." + "\nA palavra correta era " + '\033[1m'  + palavra + '\033[1m')
    #print("resultado final")


while not chegou_no_fim_do_jogo:
    resetar_partida()
    while not chegou_no_fim_da_partida:
        imprimirForca()
        imprimirPalavra()
        imprimirListaDeLetrasEscolhidas()
        imprimirNumeroDeTentativas()
        letra_escolhida = input("Digite uma letra ou 'SAIR' para sair do jogo: ").lower()
        letras_escolhidas.append(letra_escolhida)
        if letra_escolhida == "sair":
            break
        elif letra_escolhida in palavra:
            chegou_no_fim_da_partida = chegouNoFimPorSucesso()
        else:
            chegou_no_fim_da_partida = chegouNoFimPorFalha()
    imprimirResultadoFinal()
    jogar_novamente = input("Você gostaria de jogar novamente? ")
    if jogar_novamente == "sim":
        chegou_no_fim_do_jogo = False
    else:
        chegou_no_fim_do_jogo = True



    # if letra_escolhida in correct_word:
    #     pos = palavra.find(letra)
    #         for i in range(pos, len(palavra)):
    #                 if letra == palavra[i]:
    #                     riscos[i] = letra
