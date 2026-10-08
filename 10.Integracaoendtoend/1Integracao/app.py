"""App minima de estoque usada no teste de integracao."""


class Produto:
    def __init__(self, nome: str, quantidade: int) -> None:
        self.nome = nome
        self.quantidade = quantidade


class Estoque:
    def __init__(self) -> None:
        self.produtos: dict[str, int] = {}

    def adicionar_produto(self, produto: Produto) -> None:
        """Cadastra o produto ou, se ja existe, soma a quantidade."""
        if produto.nome not in self.produtos:
            self.produtos[produto.nome] = produto.quantidade
        else:
            self.produtos[produto.nome] += produto.quantidade

    def verifica_quantidade(self, nome_produto: str) -> int:
        return self.produtos.get(nome_produto, 0)
