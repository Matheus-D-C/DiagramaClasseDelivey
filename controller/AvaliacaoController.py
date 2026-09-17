from typing import List
from model_restaurante.avaliacao_produto import AvaliacaoProduto

class AvaliacaoControle:
    avaliacoes: List[AvaliacaoProduto]

    def __init__(self) -> None:
        self.avaliacoes = []
        self._proximo_id = 1

    def avaliar_produto(self, cliente_id: int, produto_id: int, nota: int, comentario: str) -> AvaliacaoProduto:

        avaliacao = AvaliacaoProduto(id_avaliacao=self._proximo_id, nota = nota, comentario = comentario)
        if avaliacao.validar_nota():
            self.avaliacoes.append(avaliacao)
            self._proximo_id += 1
        return avaliacao

    def listar_avaliacoes_por_produto(self, produto_id: int) -> List[AvaliacaoProduto]:
        return self.avaliacoes

    def remover_avaliacao(self, avaliacao_id: int) -> bool:

        for a in self.avaliacoes:
            if a._id == avaliacao_id:
                self.avaliacoes.remove(a)
                return True
        return False