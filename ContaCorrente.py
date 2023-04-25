from Cliente import Cliente


class ContaCorrente:

    def __init__(self, numero:str, saldo: float, cliente: Cliente) -> None:
        self._numero = numero
        self._saldo = saldo
        self._cliente = cliente
        self._nome = F'{cliente.getnome} {cliente.getsobrenome}'
        self._db = []

    def transferirPara(self,  para: any, quantidade: float):
        from metodoTransferir import MT as Mt

        if self._saldo < quantidade:
            print("Saldo Insuficiente!")
        else:
            Mt(self._numero, self._saldo, self._cliente).transferir(quantidade=quantidade, conta=para)
            self._saldo -= quantidade
            self._db.append(["Transferência", float(quantidade), para.getNome])

    def depositar(self, quantidade: float):
        self._saldo += quantidade
        self._db.append(['Deposito', float(quantidade)])

    def sacar(self, quantidade: float):
        if self._saldo < quantidade:
            print("Saldo Insuficiente!")

        else:
            self._saldo -= quantidade
            self._db.append(["Saque", float(quantidade)])

    def exibirExtrato(self) -> None:
        print(f"Nome Completo: {self._nome}\n")
        print(f'CPF: {self._cliente.getcpf}\n')
        print(f'Nº conta: {self._numero}\n')
        print(f'Saldo Atual: R${self._saldo}\n\n')

        for v in self._db:
            print("_"*30)

            for index, valor in enumerate(v):
                n = ""
                if type(valor) is str and index == 0:
                    n = "Tipo: "
                    
                if type(valor) is float:
                    n = f"Quantia: "

                if type(valor) is str and index == 2:
                    n = f"Para: "

                print(f"{n} {valor}")

    @property
    def getSaldo(self) -> float:
        return self._saldo

    @getSaldo.setter
    def getSaldo(self, saldo: float) -> None:
        self._saldo += saldo

    @property
    def getNome(self) -> str:
        return self._nome

    @getNome.setter
    def getNome(self, nome: str):
        self._nome = nome

    @property
    def getDB(self) -> list:
        return self._db

    @getDB.setter
    def getDB(self, lista: list) -> None:
        self._db = lista

