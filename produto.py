from abc import ABC, abstractmethod

class Produto(ABC):
    codigo: int
    nome: str
    estoque: int

    def __init__(self, codigo: int, nome: str, estoque: int) -> None:
        self.codigo = codigo
        self.nome = nome
        self.estoque = estoque
    
    @staticmethod
    @abstractmethod
    def getEstoqueCategoria() -> int:
        pass
    
    @abstractmethod
    def vender(self) -> None:
        pass

    def __str__(self) -> str:
        return f'Código: {self.codigo}\nNome: {self.nome}\nEstoque: {self.estoque}\n'