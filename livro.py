from produto import Produto
from datetime import datetime

class Livro(Produto):
    Estoque = 0

    dataPublicacao: datetime
    autor: str
    genero: str
    idioma: str

    def __init__(self, codigo: int, nome: str, estoque: int, dataPublicacao: datetime, autor: str, genero: str, idioma: str) -> None:
        super().__init__(codigo, nome, estoque)
        self.dataPublicacao = dataPublicacao
        self.autor = autor
        self.genero = genero
        self.idioma = idioma
        Livro.Estoque += estoque

    @staticmethod
    def getEstoqueCategoria() -> int:
        return Livro.Estoque
    
    def vender(self) -> None:
        Livro.Estoque -= self.estoque
    
    def __str__(self) -> str:
        return super().__str__() + f'Data de publicação: {self.dataPublicacao.date()}\nAutor: {self.autor}\nGênero: {self.genero}\nIdioma: {self.idioma}'