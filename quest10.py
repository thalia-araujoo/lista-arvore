class No:
    def __init__(self, valor):
        self.valor = valor
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
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

    def encontrar_valor_maximo(self):
        if self.raiz is None:
            return None

        no_atual = self.raiz
        while no_atual.direita is not None:
            no_atual = no_atual.direita

        return no_atual.valor


if __name__ == "__main__":
    arvoreB = ArvoreBinaria()
    numeros = [12, 5, 18, 3, 9, 12, 20]

    for numero in numeros:
        arvoreB.insere(numero)

    maximo_valor = arvoreB.encontrar_valor_maximo()
    print("Valor máximo na árvore:", maximo_valor)
