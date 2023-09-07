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


    def nos_filhos(self, no_pai):
        filhos = []
        if no_pai is not None:
            if no_pai.esquerda:
                filhos.append(no_pai.esquerda)
            if no_pai.direita:
                filhos.append(no_pai.direita)
        return filhos


if __name__ == "__main__":
    arvoreB = ArvoreBinaria()
    numeros = [12, 5, 18, 3, 9, 12, 20, 2, 4, 7, 15, 22]

    for numero in numeros:
        arvoreB.insere(numero)

    no_alvo = arvoreB.raiz.direita  # Suponha que estamos interessados nos filhos do nó 18

    filhos_do_no = arvoreB.nos_filhos(no_alvo)
    if filhos_do_no:
        valores_filhos = [no.valor for no in filhos_do_no]
        print(f"Os filhos do nó com valor {no_alvo.valor} são:", valores_filhos)
    else:
        print(f"O nó com valor {no_alvo.valor} não possui filhos.")
