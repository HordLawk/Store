from produto import Produto

class CD(Produto):
    Estoque = 0

    atributoHipotetico: str

    def __init__(self, codigo: int, nome: str, estoque: int, atributoHipotetico: str) -> None:
        super().__init__(codigo, nome, estoque)
        self.atributoHipotetico = atributoHipotetico
        CD.Estoque += estoque

    @staticmethod
    def getEstoqueCategoria() -> int:
        return CD.Estoque
    
    def vender(self) -> None:
        CD.Estoque -= self.estoque

    def __str__(self) -> str:
        return super().__str__() + f'Atributo hipotético: {self.atributoHipotetico}'