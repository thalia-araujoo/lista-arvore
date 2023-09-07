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

    def nos_no_nivel(self, nivel_alvo):
        return self._nos_no_nivel_recursivamente(self.raiz, nivel_alvo, 0, [])

    def _nos_no_nivel_recursivamente(self, no_atual, nivel_alvo, nivel_atual, resultado):
        if no_atual is None:
            return resultado

        if nivel_atual == nivel_alvo:
            resultado.append(no_atual.valor)

        # Recursivamente visita os nós nas subárvores esquerda e direita
        resultado = self._nos_no_nivel_recursivamente(no_atual.esquerda, nivel_alvo, nivel_atual + 1, resultado)
        resultado = self._nos_no_nivel_recursivamente(no_atual.direita, nivel_alvo, nivel_atual + 1, resultado)

        return resultado


if __name__ == "__main__":
    arvoreB = ArvoreBinaria()
    numeros = [12, 5, 18, 3, 9, 12, 20, 2, 4, 7, 15, 22]

    for numero in numeros:
        arvoreB.insere(numero)

    nivel_alvo = 2
    nos_no_nivel = arvoreB.nos_no_nivel(nivel_alvo)
    print(f"Nós no nível {nivel_alvo}:", nos_no_nivel)
