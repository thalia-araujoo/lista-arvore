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

    def encontrar_caminho_para_no(self, valor):
        caminho = []
        self._encontrar_caminho_para_no_recursivamente(self.raiz, valor, caminho)
        return caminho

    def _encontrar_caminho_para_no_recursivamente(self, no_atual, valor, caminho):
        if no_atual is None:
            return False

        # Adicione o valor do nó atual ao caminho
        caminho.append(no_atual.valor)

        # Se encontrarmos o nó com o valor desejado, retornamos True
        if no_atual.valor == valor:
            return True

        # Verifique recursivamente as subárvores esquerda e direita
        if (self._encontrar_caminho_para_no_recursivamente(no_atual.esquerda, valor, caminho) or
                self._encontrar_caminho_para_no_recursivamente(no_atual.direita, valor, caminho)):
            return True

        # Se não encontrarmos o valor no nó atual ou em suas subárvores, remova o valor do caminho
        caminho.pop()
        return False


if __name__ == "__main__":
    arvoreB = ArvoreBinaria()
    numeros = [12, 5, 18, 3, 9, 12, 20, 2, 4, 7, 15, 22]

    for numero in numeros:
        arvoreB.insere(numero)

    valor_alvo = 15
    caminho_para_no = arvoreB.encontrar_caminho_para_no(valor_alvo)
    if caminho_para_no:
        print(f"Caminho para o nó com valor {valor_alvo}:", caminho_para_no)
    else:
        print(f"O nó com valor {valor_alvo} não foi encontrado na árvore.")
