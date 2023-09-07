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

    def travessia_em_niveis(self):
        if self.raiz is None:
            return []

        resultado = []
        nivel_atual = 0

        while True:
            nivel = self._travessia_nivel(self.raiz, nivel_atual, [])
            if nivel:
                resultado.extend(nivel)
                nivel_atual += 1
            else:
                break

        return resultado

    def _travessia_nivel(self, no_atual, nivel_alvo, resultado_nivel):
        if no_atual is None:
            return []

        if nivel_alvo == 0:
            resultado_nivel.append(no_atual.valor)
        elif nivel_alvo > 0:
            esquerda = self._travessia_nivel(no_atual.esquerda, nivel_alvo - 1, resultado_nivel)
            direita = self._travessia_nivel(no_atual.direita, nivel_alvo - 1, resultado_nivel)

        return resultado_nivel


if __name__ == "__main__":
    arvoreB = ArvoreBinaria()
    numeros = [12, 5, 18, 3, 9, 12, 20]

    for numero in numeros:
        arvoreB.insere(numero)

    resultado_travessia = arvoreB.travessia_em_niveis()
    print("Travessia em Níveis:", resultado_travessia)
