
# **************************************************************************************************#
#                    AGORA COMEÇA PARTES QUE CONFUNDO OU NÃO LEMBRO OU ERRO                         #
# **************************************************************************************************#

# Modulos | Quebrando n° | cateto e Hipotenusa | Seno,cosseno e tangente | sorteando intem na lista 
# tocando mp3 | manipulando texto | exercícios

# importações - para adicionar funções ao py
# import oQueDeseja       ex import blueprint
# blueprint é uma biblioteca
# from math import ceil, floor, trunc, pow, sqrt, factorial
# ceil(x) = maior n° inteiro maior ou menor a x
# trunc(x) = pega a parte inteira, sem arredondar
# floor(x) = menor n° inteiro maior ou menor a x
# pow(x,y) == x**n° (potência)
# sqrt(x) = raiz quadrada de x
# factorial(n) = fatorial
# porém tem outros que não serão pegos, usados
# isqrt(n) = raiz quadrada inteira de um inteiro não negativo n
# isfinite(x) = vê se x não é n° infinito ou um NAN(não n°)
# isinf(x) = x é um infinito positivo ou negativo
# pi = 3.141592 ... 
# da biblioteca blueprint traga a classe Blueprint
# de toda tudo que tem na biblioteca blueprint, quero apenas a classe Blueprint

# ----------------------- apenas com import--------------------

#import math
# raizQdrada = math.sqrt(num)
# raizQdradaC = math.ceil(raizQdrada)
# raizQdradaF = math.floor(num)

# ------------------------- apenas com from--------------------

#     #%% - marcador usado para dividir o cód em células executáveis(code cell)
# assim posso rodar cada cód sem precisar comentar, deletar ou criar novas files
# em projetos não se dá tantos imports, é um único cód, mas aqui, para não ter de ficar subindo e descendo fiz esta gambiarra


#%%
from math import floor, ceil, sqrt, trunc, isinf

#%%
num = int(input("n°: "))

raizQdrada = sqrt(num)
raizQdradaC = ceil(raizQdrada)
raizQdradaF = floor(num)

print(f"A raiz quadrada de {num} é: {raizQdrada}")
print(f"A raiz quadrada, arredondada para cima, de {num} é: {raizQdradaC}")
print(f"A raiz quadrada, arredondada para baixo, de {num} é: {raizQdradaF}")

# caso a biblioteca não venha com python, é sór dar pip install nomeMódulo (estou usando vs code)(ver se é com pip mesmo)


# ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨ EXERCÍCIOS ¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨¨

#%%
#_________________________________________________________exer 16
# Ler um n° real e mostre sua porção inteira

from math import trunc, isinf

x = float(input(" digite valor real, ele é com ponto: "))

intei = trunc(x)
inf_neg = isinf(x)

print(f"o valor real/float {x} é este valor inteiro {intei}, é {inf_neg} para n° infinito ou negativo ")

#%%
#************************* CORREÇÃO COM VÁRIAS FORMAS DO EXER 16

# sem usar a biblioteca math
#int(x) = vê se o n° é inteiro
#"inf" = infinito

x = float(input(" digite valor real, ele é com ponto: "))

intei = int(x)
if x < 0:
    res = True
else:
    res = False
    
if x == float("inf") or float("-inf"):
    resu = True
else:
    resu = False

if res == True or resu == True:
    rest = True
else:
    rest = False



print(f"o valor real/float {x} é este valor inteiro {intei}, é {rest} para n° infinito ou negativo ")

# %%
#________________________________________________________ exer 17

# ler comprimento do cateto oposto e do cateto adjacente de um triângulo e mostre comprimento da hipotenusa

#matematicamnete falando:
#teorema de Pitágoras 
# elevar cateto ao quadrado
# somar resultados
# raiz quadrada
# ex (x**2+y**3)sqrt2 (algo assim)



cateno1 = float(input("cateno 1: "))
cateno2 = float(input("cateno 2: "))

#passo a passo:

poten_coc_1 = cateno1**2
poten_coc_2 = cateno2**2
soma = poten_coc_1+poten_coc_2
raiz1 = sqrt(soma)
print(raiz1)

#%%

# ------------------------- Correção professor 

hi = (cateno1**2 + cateno2**2) **(1/2) 
print(hi)

#%%
# ------------------------ importando math professor

from math import hypot
co = 3.0
ca = 4.0

hi = hypot(co, ca)
print(hi)



#%%
#________________________________________________________ exer 18

# ler um ângulo e mostre o valor do seno cosseno e tangente

#                          FIZ ERRADO 


#usarei para
# cosseno = cos(x)
# seno = sin(x)
# tangente = tan(x)

from math import cos, tan, sin, radians

angulo = int(input("digite valor de um ângulo: "))

cosseno = cos(angulo)
seno = sin(angulo) 
tangente = tan(angulo)                 

print(f""" do ângulo {angulo} temos:
      cosseno = {cosseno:.2f}
      seno = {seno:2f}
      tangente = {tangente:.2f}""")

#  ----------------------------- Correção professor 

# RADIANS = TEM DE CONVERTER O ÂNGULO X DE GRAU PARA RADIANOS

senos = sin(radians(angulo))
coss = cos(radians(angulo))
tang = tan(radians(angulo))
print(f"\n{senos}")

# esplicando o motivo de ter de converter em radiano(n°)
# a função trigonométrica em .py trabalha com radianos
# 90° (ângulo) é 1/4 de um circulo completo - engenharia, navegação, geometria básica usa

# 90 (n°) é apenas um número natural
# 90 radianos equilave a 14.32 voltas completas no circulo

# senos = sin(radians(angulo))
# aqui está transformando ângulo para radiano - ao converter 90 passa a ser 1/4 a volta completa

# %%

#_________________________________________________________exer 19

# sortear 4 alunos para apagar quadro. mostrar o nome do escolhido

# sortei = comb(n, k) -> n é o n° de maneiras de escolher k intens de n itens sem repetição e sem ordem

#                          não consegui

from math import comb

sortei = comb(4, 4)

if sortei == 0:
    k1 = "Rosa"
elif sortei == 1:
    k2 = "Rodolfo"
elif sortei == 2:
    k3 = "Rogério"
else:
    k4 = "Roberta"


print(f"O aluno sorteado foi {k1}")

#%%
#  ----------------------------- Correção professor 

# usar lista e ramdom
import random

alunos = ["Rosa", "Rodolfo", "Rogério", "Roberta"] 
# passei um dcit (dicionário) e não uma lista - dá erro pois espera algo ordenado/com índice
# estava assim {"Rosa", "Rodolfo", "Rogério", "Roberta"}
# para para converter em lista random.choice(list(alunos))

sorteio = random.choice(alunos)

print(f"Aluno sorteado foi {sorteio}")
# 

# %%

#________________________________________________________ exer 20

# professor quer agora sortear mostrando a ordem dos sorteados para responder exercícos

#perm(n, k) = Número de maneiras de escolher k itens de n itens 
# sem repetição e com ordem

from math import perm

sorte = perm(4, 4)

if sorte == 0:
    k11 = "Rosa"
elif sorte == 1:
    k21 = "Rodolfo"
elif sorte == 2:
    k31 = "Rogério"
else:
    k41 = "Roberta"

print(sorte)

#não sei como usar estas funções

#%%
#  ----------------------------- Correção professor 

# usar lista e ramdom

from random import shuffle

alun = ["Rosa", "Rodolfo", "Rogério", "Roberta"] 
random.shuffle(alun)

print(f"chamada")
print(alun)


#%%
#________________________________________________________ exer 21

#tocar mp3

#fui ver e deveria dar pip install soundfile, porém não estou podendo instalar nada devido muitas bibliotecas já usdas para curso

#  ----------------------------- Correção professor

# pegar música no computador e por aqui, arrastar
# renomeei para elis, simples

import paygame
#(terminal pip install paygame)

paygame.init()
#inicia o paygame

paygame.mixer.music.load("elis.pm3")
#carrega a música

paygame.mixer.music.play()
#para tocar

paygame.event.wait()
#para esperar a múcica

