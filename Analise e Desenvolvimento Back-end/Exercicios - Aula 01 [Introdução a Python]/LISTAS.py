"""

Utilizando listas faça um programa que faça 5 perguntas para uma pessoa sobre um crime. As perguntas são:
"Telefonou para a vítima?"
"Esteve no local do crime?"
"Mora perto da vítima?"
"Devia para a vítima?"
"Já trabalhou com a vítima?" O programa deve no final emitir uma classificação sobre a participação da pessoa no crime. 
Se a pessoa responder positivamente a 2 questões ela deve ser classificada como "Suspeita", entre 3 e 4 como "Cúmplice" 
e 5 como "Assassino". Caso contrário, ele será classificado como "Inocente".

"""

res = []
res.append(input("Telefonou para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Esteve no local do crime? 1/Sim ou 0/Não: "))
res.append(input("Mora perto da vítima? 1/Sim ou 0/Não: "))
res.append(input("Devia para a vítima? 1/Sim ou 0/Não: "))
res.append(input("Já trabalhou com a vítima? 1/Sim ou 0/Não: "))
soma_respostas = 0
for i in res: # soma o número de respostas
soma_respostas += int(i)
if (soma_respostas < 2):
 print("\nInocente")
elif (soma_respostas == 2):
 print("\nSuspeita")
elif (3 <= soma_respostas <= 4):
 print("\nCúmplice")
elif (soma_respostas == 5):
 print("\nAssassino")


########################################################


'''
Utilize uma lista para resolver o problema a seguir. Uma empresa paga seus vendedores com base em comissões. 
O vendedor recebe $200 por semana mais 9 por cento de suas vendas brutas daquela semana. Por exemplo,
 um vendedor que teve vendas brutas de $3000 em uma semana recebe $200 mais 9 por cento de $3000, ou seja, 
 um total de $470. Escreva um programa (usando um array de contadores) que determine quantos vendedores 
 receberam salários nos seguintes intervalos de valores:

'''

l=[0,0,0,0,0,0,0,0,0]
x=0
while True:
    n=float(input('Inf seu salario %d° R$: '%(x+1)))

    if 200 < n <299:
        l[0]+=1
    elif 300 < n > 399:
        l[1]+=1
    elif 400 < n > 499:
        l[2]+=1
    elif 500 < n > 599:
        l[3]+=1
    elif 600 < n > 699:
        l[4]+=1
    elif 700 < n > 799:
        l[5]+=1
    elif 800 < n > 899:
        l[6]+=1
    elif 900 < n > 999:
        l[7]+=1
    elif n >= 1000:
        l[8]=[8]+1
    x+=1
    d = input('deseja continuar?(s ou n)')
    if d == 'n':
        break
print(l[0])

