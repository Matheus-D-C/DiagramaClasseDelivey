from typing import List, Optional
from model_restaurante.AvaliacaoProduto import AvaliacaoProduto

class AvaliacaoControle:

    def __init__(self) -> None:
        self.__avaliacoes: List[AvaliacaoProduto] = []

    def avaliarProduto(self, cliente_id: int, produto_id: int, nota: int, comentario: str) -> Optional[AvaliacaoProduto]:
        nova_id = len(self.__avaliacoes) + 1
        avaliacao = AvaliacaoProduto(id_avaliacao=nova_id, nota = nota, comentario = comentario)

        if avaliacao.validar_nota():
            self.__avaliacoes.append(avaliacao)
            print(f"Avaliação registrada para o produto {produto_id} pelo cliente {cliente_id}.")        
            return avaliacao
        else:
            print("Nota inválida! a nota deve ser entre 1 a 5")
            return None

    def listar_avaliacoes_por_produto(self, produto_id: int) -> List[AvaliacaoProduto]:
        return self.__avaliacoes

    def remover_avaliacao(self, avaliacao_id: int) -> bool:
        for a in self.__avaliacoes:
            if a.__id == avaliacao_id:
                self.__avaliacoes.remove(a)
                print(f"Avaliacao {avaliacao_id} removida com sucesso")
                return True
        return False