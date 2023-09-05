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


    def verifica_valor(self, valor):
        return self._verifica_valor_recursivamente(self.raiz, valor)

    def _verifica_valor_recursivamente(self, no_atual, valor):
        if no_atual is None:
            return False
        if valor == no_atual.valor:
            return True
        if valor < no_atual.valor:
            return self._verifica_valor_recursivamente(no_atual.esquerda, valor)
        return self._verifica_valor_recursivamente(no_atual.direita, valor)

# Exemplo de uso:
# Criar uma árvore binária
arvore = ArvoreBinaria()
arvore.insere(5)
arvore.insere(3)
arvore.insere(8)
arvore.insere(2)
arvore.insere(4)
arvore.insere(7)
arvore.insere(9)

# Verificar se um valor está presente na árvore
valor_procurado = 9
if arvore.verifica_valor(valor_procurado):
    print(f"{valor_procurado} está presente na árvore.")
else:
    print(f"{valor_procurado} não está presente na árvore.")
