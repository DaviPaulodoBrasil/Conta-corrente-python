from Cliente import Cliente
from ContaCorrente import ContaCorrente


class MT(ContaCorrente):

    def __init__(self, numero: str, saldo: float, cliente: Cliente) -> None:
        super().__init__(numero, saldo, cliente)

    def transferir(self, quantidade: float, conta: ContaCorrente) -> None:
        conta._saldo += quantidade
