class GerenciadorRestaurante:

    def adicionar_cardapio(self, nome: str) -> None:
        print(f"Cardápio '{nome}' registrado via GerenciadorRestaurante.")

    def atualizar_dados(self, nome: str, cnpj: str) -> None:
        print(f"Dados do restaurante atualizados para Nome: '{nome}' e CNPJ: '{cnpj}'.")