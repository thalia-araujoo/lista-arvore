class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class BinaryTree:
    def __init__(self):
        self.raiz = None

    def insere(self, valor):
        if self.raiz is None:
            self.raiz = No(valor)
        else:
            self._insere_recursivamente(self.raiz, valor)

    def _insere_recursivamente(self, no_atual, valor):
        if valor < no_atual.valor:
            if no_atual.esquerda is None:
                no_atual.esquerda = No(valor)
            else:
                self._insere_recursivamente(no_atual.esquerda, valor)
        elif valor > no_atual.valor:
            if no_atual.direita is None:
                no_atual.direita = No(valor)
            else:
                self._insere_recursivamente(no_atual.direita, valor)

    def altura(self):
        return self._calcula_altura(self.raiz)

    def _calcula_altura(self, no_atual):
        if no_atual is None:
            return 0
        altura_esquerda = self._calcula_altura(no_atual.esquerda)
        altura_direita = self._calcula_altura(no_atual.direita)
        return max(altura_esquerda, altura_direita) + 1

# Exemplo de uso:
if __name__ == "__main__":
    arvore = BinaryTree()
    numeros = [5, 15, 17, 3, 7, 12, 20]

    for numero in numeros:
        arvore.insere(numero)

    print("Altura:", arvore.altura())
