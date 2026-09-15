class Entregador:
    def __init__(self, id_entregador: int, nome: str, veiculo: str):
        self._id = id_entregador
        self._nome = nome
        self._veiculo = veiculo

    def atualizar_veiculo(self, veiculo: str) -> None:
        self._veiculo = veiculo
        
        