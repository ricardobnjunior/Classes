"""
O Sr. Manoel Joaquim acaba de adquirir uma panificadora e pretende implantar a metodologia 
da tabelinha, que já é um sucesso na sua loja de 1,99. Você foi contratado para desenvolver 
o programa que monta a tabela de preços de pães, de 1 até 50 pães, a partir do preço do pão
 informado pelo usuário, conforme o exemplo abaixo:

"""


paes = int(input("Digite a quantidade de pães: "))
while paes > 50:
    produtos = int(input("Digite a quantidade de produtos[menos que 50]: "))

count = 1
preco_pao = float(input("Qual é o preço do pão? : "))

for j in range(paes):
    print(count, "= R$", round(preco_pao * count, 2))
    count += 1


"""

O Sr. Manoel Joaquim expandiu seus negócios para além dos negócios de 1,99 e agora 
possui uma loja de conveniências. Faça um programa que implemente uma caixa registradora 
rudimentar. O programa deverá receber um número desconhecido de valores referentes aos 
preços das mercadorias. Um valor zero deve ser informado pelo operador para indicar o final 
da compra. O programa deve então mostrar o total da compra e perguntar o valor em dinheiro 
que o cliente forneceu, para então calcular e mostrar o valor do troco. Após esta operação,
 o programa deverá voltar ao ponto inicial, para registrar a próxima compra. A saída deve
  ser conforme o exemplo abaixo:

"""

import time

while True:
    precos_produtos = []
    preco_produto = True
    n_produto = 1

    while preco_produto != 0:
        print("Produto n° ", n_produto)
        preco_produto = float(input("Digite o preço do produto: "))
        precos_produtos.append(preco_produto)
        n_produto += 1

    print("Total: ", sum(precos_produtos))
    dinheiro = float(input("Digite a quantida que irá pagar: "))

    while dinheiro < sum(precos_produtos):
        dinheiro = float(input("Digite a quantida que irá pagar[maior que o total da compra] : "))

    print("Dinheiro: R$", dinheiro)
    print("Troco: R$", dinheiro - sum(precos_produtos))
    print("\nPróxima compra em 3 segundos...")
    time.sleep(3)
    print("\n" * 5)