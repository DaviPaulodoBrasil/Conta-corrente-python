class Cliente:

    def __init__(self, nome: str, cpf: str, sobrenome: str):
        self._nome = nome
        self._cpf = cpf
        self._sobrenome = sobrenome

    @property
    def getnome(self):
        return self._nome

    @getnome.setter
    def getnome(self, nome: str) -> None:
        self._nome = nome

    @property
    def getcpf(self) -> str:
        return self._cpf

    @getcpf.setter
    def getcpf(self, cpf: str) -> None:
        self._cpf = cpf

    @property
    def getsobrenome(self) -> str:
        return self._sobrenome

    @getsobrenome.setter
    def getsobrenome(self, sobrenome: str) -> None:
        self._sobrenome = sobrenome
