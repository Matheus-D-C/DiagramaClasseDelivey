from Entrega import Entrega 
from Entregador import Entregador

class GerenciadorEntrega:
    def atribuirEntregador(self, e: Entrega, ent: Entregador) -> None:
        e.entregador = ent
        print(f"Entregador {ent.nome} atribuído à Entrega ID {e.id}.")

    def agendarEntrega(self, e: Entrega) -> None:
        e.statusEntrega = "Agendada"
        print(f"Entrega ID {e.id} foi agendada com sucesso.")

    def atualizarStatusEntrega(self, entrega_id: int, status: str) -> None:
        print(f"Status da Entrega ID {entrega_id} alterada para {status}.")
        