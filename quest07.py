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

    def posordem(self):
        return self._posordem_recursivamente(self.raiz)

    def _posordem_recursivamente(self, no_atual):
        if no_atual is None:
            return []

        resultado = []

        # Recursivamente visita os nós à esquerda e à direita
        resultado.extend(self._posordem_recursivamente(no_atual.esquerda))
        resultado.extend(self._posordem_recursivamente(no_atual.direita))

        resultado.append(no_atual.valor)  # Visite o nó atual

        return resultado


if __name__ == "__main__":
    arvoreB = ArvoreBinaria()
    numeros = [12, 5, 18, 3, 9, 12, 20]

    for numero in numeros:
        arvoreB.insere(numero)

    resultado_posordem = arvoreB.posordem()
    print("Travessia Pós-Ordem:", resultado_posordem)
