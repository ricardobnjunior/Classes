"""
 Faça um Programa que peça as 4 notas bimestrais e mostre a média.

"""

num1 = float(input('Notas do 1º bimestre:'))
num2 = float(input('Notas do 2º bimestre:'))
num3 = float(input('Notas do 3º bimestre:'))
num4 = float(input('Notas do 4º bimestre:'))
print('A sua média foi:', (num1+num2+num3+num4)/4)

'''
 Faça um Programa que converta metros para centímetros.
'''

metros = float(input('Metros? '))
centimetros = metros * 100
print (centimetros, ' cm')

"""
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:

salário bruto.
quanto pagou ao INSS.
quanto pagou ao sindicato.
o salário líquido.
calcule os descontos e o salário líquido, conforme a tabela:

Obs.: Salário Bruto - Descontos = Salário Líquido.
"""


qH = input("Quanto você guanha por hora: ")
hT = input("Quantas horas você trabalhou: ")

salarioB = qH * hT

ir = (11/100.0 * salarioB)
inss = (8/100.0 * salarioB)
sindicato = (5/100.0 * salarioB)

vT = ir + inss + sindicato
salarioL = salarioB - vT

print ('Seu salário bruto é',salarioB)

print ('Valor dos impostos:')
print ('IR: ',ir)
print ('INSS: ',inss)
print ('Sindicato: ',sindicato)

print ('Seu salário liquido é: ',salarioL)