from Cliente import Cliente
from ContaCorrente import ContaCorrente

#cliente-conta 1
d = Cliente(nome="Davi", cpf="133.999.034-67", sobrenome="Silva")
cd1 = ContaCorrente(numero="1023", saldo=0.0, cliente=d)

#cliente-conta 2
v = Cliente("Vinicius", '111.234.678-90', "Pinto")
cv1 = ContaCorrente(numero="1256", saldo=0.0, cliente=v)

#executando os metodos em cd1
cd1.depositar(1200.00)
cd1.sacar(200.00)


#executando os metodos em cv1
cv1.depositar(1500.00)
cv1.sacar(100.00)
cv1.transferirPara(cd1, 200.00)

cv1.exibirExtrato()

