# condições pare 1

# simples e composta

# ESTRUTURA SEQUENCIA - segue uma seguência, conjunto de passos

#Estrutura de seleção = expressão lógica = retorna booleano

# operador lógico = and|e , or|ou , not|negação

# quando há mais possibilidades, blocos diferentes que sequem seu caminho

# identação, espaço de 4 enters

num = int(input("Quantos anos tem seu caro? "))
print("Carro novo" if num <= 3 else "carro velho")

#ou

if num<= 3:
    print("carro novo")
else:
    print("carro velho")
    
#ou

if num <= 3 : print("novo")
else: print("velho")

#%%
#___________________ ESTRUTURA DE SELEÇÃO/CONDICIONADA SIMPLES   IF

# Apenas um bloco de comando, se for verdade

nome = input("Digite seu nome")

if nome == "Alê": print(f"{nome.capitalize} sua princesa!")
print("Bem vinda/o !")


#%%
#___________________ ESTRUTURA DE SELEÇÃO/CONDICIONADA IF, ELSE UM CONDIÇÃO

# Doisbloco de comando, se for verdade if, se for falso else

nome = input("Digite seu nome")

if nome == "Alê" or nome == "alê": print(f"{nome.capitalize()} sua princesa!")
else: print(f"{nome.capitalize()}  seu/sua plebeu/ia")
print("Bem vinda/o !")

# %%

#____________média

nota = float(input("nota 1 "))
nota2 = float(input("nota 2 "))

media = (nota + nota2)/2

print("Você passou" if media >= 6 else "Recuperação")


# %%

#_____________ ex 28 

# Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.
import random

num = int(input("digite valor inteiro entre 0 e 5: "))

lista = [0, 1, 2, 3, 4, 5]
sorteio = random.choice(lista)

if num >5 or num <0: print(f"O número {num} está fora da lista de sorteios")
elif num == sorteio: print(f"Você escolheu mesmo número que foi sorteado {num}")
else: print(f"O número sorteado foi {sorteio} e seu número {num}")

# %%

#______ correção prof 28

from random import randint
from time import sleep

computador = randint(0, 5)

print("_-=-_" * 15)
print(" ")
print(f"{"vou escolher um n° de 0 a 5":^75}")
print(" ")
print("_-=-_" * 15)
print(" ")

jogador = int(input(f"{"Advinhe o n° que escolhi: ":^75}"))

print(" ")
print("_-=-_" * 15)
print(" ")
print(f"{"Será que acertou?":^75}")
sleep(3)
print(" ")
print("_-=-_" * 15)
print(" ")

if jogador == computador:
    print(" ")
    print("_-=-_" * 15)
    print(" ")
    print(f"{"Acertou!":^75}")
    print("_-=-_" * 15)
    print(" ")
else:
    print(" ")
    print("_-=-_" * 15)
    print(" ")
    print(f"{"Errou!":^75}")
    print("_-=-_" * 15)
    print(" ")
    
# resolvi por o texto centralizado na linha que crie. são 5 caracteres * 15 = 75 
   
#%%

# _______________ ex 29

#Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.

veloc = float(input("velocidade km: "))

if veloc> 80: 
    print("Você foi multado")
    print(f"Valor da multa será R$ {(veloc - 80)*7.0:.2f}")

# correção igual ao que fiz

# %%

# _______________ ex 30

# Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.

nume = int(input("Digite um n° inteiro: "))

if nume % 2 == 0: print (f"O n° {nume} é par")
else: print(f"O n° {nume} é ímpar")

# correção mesma lógica que a minha

# %%

# _______________ ex 31

#  Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.

km = float(input("Quantos Km percorreu: "))

if km <= 200:
    print(f"Você percorreu {km} Km, valor final é de R$ {km*0.5:.2f}")
else: print(f"Você percorreu {km} Km, valor final é de R$ {km*0.45:.2f}")

# %%
 # Correção prof
 
km = float(input("Quantos Km percorreu: "))

valor = km*0.5 if km <= 200 else km*0.45
print(f"Você percorreu {km} Km, valor final é de R$ {valor:.2f}")

#%%
# _______________ ex 32

# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.

ano = int(input("Qual ano quer saber se é Bissexto"))
#print(type(ano))
converter = str(ano)
#print(type(converter))
indiciando = converter.rsplit()
#é uma função, tem ()
print(indiciando)

if indiciando == "0" and ano % 400 == 0 or indiciando != "0" and ano % 4 == 0: print(f"O ano {ano} é Bissexto")
else: print(f"O ano {ano} não é Bissexto")

# tentei fazer diferente
# se termina com 0 e é divisivel por 400 = bi
# se termina diferente de zero e é diviível por 4 = bi
# resto não bi

# dei input de int para conta| transformei em  string para fatiamento split(), como quero o último valor (índice 3) que fica à direita usei right split (peda da direta para esquerda) e compara se é ou não zero

# %%
# _______________ correção prof 32

ano = int(input("Ano: "))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0: print(f"O ano {ano} é Bissexto")
else: print(f"O ano {ano} não é Bissexto")

#%%
# _______________ ex 33

#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.

num1 = float(input("digeto um valor: "))
num2 = float(input("digeto outro valor: "))
num3 = float(input("digeto mais um valor: "))

# num1 = 16
# num2 = 17
# num3 = 18

# aqui esqueci de ver menor, m é só por o número da ponta da direta
# ex print(f"O numero {num3} é maior que os outro e {num2}")
if num1>num2 and num1>num3: 
    print(f"O numero {num1} é maior que os outro")
elif num2>num1 and num2>num3: 
    print(f"O numero {num2} é maior que os outro")
else: 
    print(f"O numero {num3} é maior que os outro")

#pensando outra forma
#estilo encadeado
#java seria &&

if num1>num2>num3: print(f"Ordem doss números {num1} > {num2} > {num3}")
elif num1>num3>num2: print(f"Ordem doss números {num1} > {num3} > {num2}")
elif num2>num1>num3: print(f"Ordem doss números {num2} > {num1} > {num3}")
elif num2>num3>num1: print(f"Ordem doss números {num2} > {num3} > {num1}")
elif num3>num1>num2: print(f"Ordem doss números {num3} > {num1} > {num2}")
# elif num3>num1 and num2>num1: print(f"Ordem doss números {num3} > {num2} > {num1}")
else: print(f"Ordem doss números {num3} > {num2} > {num1}")


# %%
# _______________ correção 33

num1 = float(input("digeto um valor: "))
num2 = float(input("digeto outro valor: "))
num3 = float(input("digeto mais um valor: "))

#considerar que a é o menor sempre

menor = num1

if num2<num1 and num2<num3: 
    menor=num2
if num3<num1 and num3<num2: 
    menor=num3

maior = num1

if num2>num1 and num2>num3: 
    maior=num2
if num3>num1 and num3>num2: 
    maior=num3

print(f"O menor valor é entre {num1}, {num2} e {num3} é o {menor} e o maior {maior}")


# %%
# _______________ ex 34

# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.

salario = float(input("Seu salário R$ "))

if salario > 1250.00:
    porcen = "10%"
    aumento = salario*1.10
else:
    porcen = "15%"
    aumento = salario*1.15

print(f"Você tece um  aumento de {porcen} no salário de R$ {salario:.2f}\nRecberá a partir de hoje R$ {aumento:.2f}")

# %%
# _______________ correção 34

salario = float(input("Seu salário R$ "))

if salario <= 1250:
    aumento = salario + (salario*15/100)
    
else:
    aumento = salario + (salario*10/100)

print(f"O salário de R$ {salario:.2f} será de R$ {aumento:.2f}")


# %%
# _______________ ex 35

# Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.

reta1 = float(input("Comprimento um: "))
reta2 = float(input("Comprimento dois: "))
reta3 = float(input("Comprimento três: "))

# soma do comprimento de quaisquer dos dois lados devem ser maior que o outro lado

if reta1+reta2 > reta3:
    #tem de deixar espaço entre os símbiolos
    print(f'{"O":^20}')
    print(f'{"O "*2:^20}')
    print(f'{"O "*3:^20}')
    print(f'{"O "*4:^20}')
else:
    print("Não é retângulo")
    
# %%

# _______________ correção 35

# só analise um parte, fatou comparar o resto

reta1 = float(input("Comprimento um: "))
reta2 = float(input("Comprimento dois: "))
reta3 = float(input("Comprimento três: "))

# soma do comprimento de quaisquer dos dois lados devem ser maior que o outro lado

if reta1+reta2 > reta3 and reta1 + reta3 > reta2 and reta2 + reta3 > reta1:
    print(f'{"O":^20}')
    print(f'{"O "*2:^20}')
    print(f'{"O "*3:^20}')
    print(f'{"O "*4:^20}')
else:
    print("Não é retângulo")
# %%
