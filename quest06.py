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

    def preordem(self):
        return self._preordem_recursivamente(self.raiz)

    def _preordem_recursivamente(self, no_atual):
        if no_atual is None:
            return []

        resultado = [no_atual.valor]  # Visita o nó atual

        # Recursivamente visita os nós à esquerda e à direita
        resultado.extend(self._preordem_recursivamente(no_atual.esquerda))
        resultado.extend(self._preordem_recursivamente(no_atual.direita))

        return resultado


if __name__ == "__main__":
    arvoreB = ArvoreBinaria()
    numeros = [15, 5, 7, 3, 30, 12, 20]

    for numero in numeros:
        arvoreB.insere(numero)

    resultado_preordem = arvoreB.preordem()
    print("Travessia Pré-Ordem:", resultado_preordem)
