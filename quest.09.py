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

    def contar_nos(self):
        return self._contar_nos_recursivamente(self.raiz)

    def _contar_nos_recursivamente(self, no_atual):
        if no_atual is None:
            return 0

        # Visita o nó atual e conta os nós nas subárvores esquerda e direita
        return 1 + self._contar_nos_recursivamente(no_atual.esquerda) + self._contar_nos_recursivamente(no_atual.direita)

if __name__ == "__main__":
    arvoreB = ArvoreBinaria()
    numeros = [12, 5, 18, 3, 9, 12, 20]

    for numero in numeros:
        arvoreB.insere(numero)

    total_nos = arvoreB.contar_nos()
    print("Número total de nós na árvore é:", total_nos)
