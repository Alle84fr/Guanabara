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

