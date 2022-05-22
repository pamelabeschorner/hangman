class Forca:
    def __int__(self):
        pass

    def imprimir(self, numero_de_erros):
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
