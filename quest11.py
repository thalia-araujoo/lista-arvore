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

    def e_arvore_busca(self):
        return self._e_arvore_busca_recursivamente(self.raiz, float('-inf'), float('inf'))

    def _e_arvore_busca_recursivamente(self, no_atual, valor_minimo, valor_maximo):
        if no_atual is None:
            return True

        valor = no_atual.valor

        # Verifica se o valor do nó atual está dentro dos limites permitidos
        if valor <= valor_minimo or valor >= valor_maximo:
            return False

        # Verifica recursivamente as subárvores esquerda e direita
        return (self._e_arvore_busca_recursivamente(no_atual.esquerda, valor_minimo, valor) and
                self._e_arvore_busca_recursivamente(no_atual.direita, valor, valor_maximo))

# Exemplo de uso:
if __name__ == "__main__":
    arvoreB = ArvoreBinaria()
    numeros = [12, 5, 18, 3, 9, 12, 20]

    for numero in numeros:
        arvoreB.insere(numero)

    e_valida = arvoreB.e_arvore_busca()
    if e_valida:
        print("A árvore é uma árvore de busca válida.")
    else:
        print("A árvore não é uma árvore de busca válida.")
