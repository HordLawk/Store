from produto import Produto
from livro import Livro
from cd import CD
from dvd import DVD

class Loja:
    produtos: dict[int, Produto] = {}

    @staticmethod
    def adicionar(p: Produto) -> dict[int, Produto]:
        Loja.produtos[p.codigo] = p
        return Loja.produtos

    @staticmethod
    def buscarCodigo(codigo: int) -> Produto:
        return Loja.produtos[codigo]

    @staticmethod
    def buscarNome(nome: str) -> Produto:
        for p in Loja.produtos.values():
            if p.nome == nome:
                return p

    @staticmethod
    def vender(codigo: int) -> Produto:
        p = Loja.produtos[codigo]
        Loja.produtos.pop(codigo)
        p.vender()
        return p

    @staticmethod
    def listar() -> str:
        produtosStr = "\n\n".join([str(x) for x in Loja.produtos.values()])
        return f'Livros: {Livro.getEstoqueCategoria()}\nCDs: {CD.getEstoqueCategoria()}\nDVDs: {DVD.getEstoqueCategoria()}\n\n{produtosStr}'