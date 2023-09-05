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

    def travessia_inordem(self):
        resultado = []
        self._travessia_inordem_recursiva(self.raiz, resultado)
        return resultado

    def _travessia_inordem_recursiva(self, no_atual, resultado):
        if no_atual is not None:
            # Primeiro visitamos a subárvore esquerda
            self._travessia_inordem_recursiva(no_atual.esquerda, resultado)
            # Em seguida, visitamos o nó atual
            resultado.append(no_atual.valor)
            # Por fim, visitamos a subárvore direita
            self._travessia_inordem_recursiva(no_atual.direita, resultado)

# Exemplo de uso:
# Criar uma árvore binária
arvore = ArvoreBinaria()
arvore.insere(10)
arvore.insere(3)
arvore.insere(6)
arvore.insere(2)
arvore.insere(4)
arvore.insere(14)
arvore.insere(9)

# Realizar a travessia inordem
valores_inordem = arvore.travessia_inordem()
print(valores_inordem)  # Deve imprimir [2, 3, 4, 6, 9, 10, 14]
