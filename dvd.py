from produto import Produto

class DVD(Produto):
    Estoque = 0

    atributoHipotetico: str

    def __init__(self, codigo: int, nome: str, estoque: int, atributoHipotetico: str) -> None:
        super().__init__(codigo, nome, estoque)
        self.atributoHipotetico = atributoHipotetico
        DVD.Estoque += estoque

    @staticmethod
    def getEstoqueCategoria() -> int:
        return DVD.Estoque
    
    def vender(self) -> None:
        DVD.Estoque -= self.estoque
    
    def __str__(self) -> str:
        return super().__str__() + f'Atributo hipotético: {self.atributoHipotetico}'