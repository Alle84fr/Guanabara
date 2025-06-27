# manipulação de texto

# CADEIA DE CARACTERES - IMPORTANTE ESTUDAR

# frase = cadeia de caracteres = string = cadeia de texto
# Sempre entre aspas simples ' ' ou duplas " "
# ex: cadeia = " curso em vídeos"
# o .py irá separar letras, contando com espaço e cada um estará relacionado a sua posição (índice)
# ex: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 índice inicia em zerp
#     c u r s o   e m   v  i  d  e  o  s são 13 letras e 2 espaços vazios = 15 caracteres


# -------------------------- FATIAMENTO --------------------------------#


#1° FORMA

# [] = lista

cadeia = "curso em videos"   
# estava dando erro na numeração dos índices, ex: 8 estava pegando m - motivo, tinha espeço no início da frase, criando um "caractere" a mais " curso em vídeo". foi arrumado

print(" ")
print(cadeia)
#printa toda frase da variável cadeia

print(f"no íncide 6 tem {cadeia[6]} caractere")
print(f"no índide 8 tem {cadeia[8]} espaço entre palavras")
print(cadeia[13])
# pega a variável cadeia, que, neste caso será tratada como array ou lista e para saber o que se tem na posição 13, por
# exemplo chama o nome da lista/variável []/colchete e a posição que deseja

# 2° forma

print(cadeia[1:5])
# ex: 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 índice inicia em zerp
#     c u r s o   e m   v  i  d  e  o  s são 13 letras e 2 espaços vazios = 15 caracteres

# 1 2 3 4   índice inicia em zerp
# u r s o   são 13 letras e 2 espaços vazios = 15 caracteres
# EXCLUI O ÚLTIMO ÍNDICE - COMEÇA CERTO, MAS TERMINA COM UM A MENOS NO FINAL - !!!!! RANGE !!!!!
# pegará do índice 1 ao 4 (urso), IGNORA O 5 (ESPAÇO)
print(cadeia[5:11])

print(cadeia[3:13:3])
# inicia no zero (c), pula 2 e pega o 3°s, vai assim até o 13
# print(cadeia[ INÍCIO: FIM : PULOS])
# 3  6 9 12  índice inicia em zerp
# s  e v  e  são 13 letras e 2 espaços vazios = 15 caracteres

print(cadeia[:10])
# começa literalmente do 0 e vai até o 9 - equiva 0:10
# 0 1 2 3 4 5 6 7 8 9  índice inicia em zerp
# c u r s o   e m   v   são 13 letras e 2 espaços vazios = 15 caracteres

print(cadeia[7:])
# começa no 7 e vai até acabar, pegando o último
# 7 8 9 10 11 12 13 14 índice inicia em zerp
# m   v  i  d  e  o  s são 13 letras e 2 espaços vazios = 15 caracteres

print(cadeia[9::2])
# inicia no 9, vai até o final (tipo 9:final:pulo2)
# 9 11 13  índice inicia em zerp
# v  d  o  são 13 letras e 2 espaços vazios = 15 caracteres


# ------------------------------------------------------------------------------------#
#                                len - comprimento                                    #
#                             quantidade de caracteres                                #
# ------------------------------------------------------------------------------------#

print(len(cadeia))

# ------------------------------------------------------------------------------------#
#                             count- contar repetição                                 #
#                          vezes que um caracter se repete                            #
# ------------------------------------------------------------------------------------#

print(cadeia.count("o"))
# quantas vezes o "o" minúsculo aparece

print(cadeia.count("o",0,16))
# estou contando e fatiando ao mesmo tempo - aqui coloquei um n° a mais do comprimento para poder pegar
# toda frase

# ------------------------------------------------------------------------------------#
#                       find- momento que iniciou a repetição                         #
# ------------------------------------------------------------------------------------#

print(f"\nA primeira vez que aparece um 'e' na na {cadeia.find('e')} posição")
# observação - dentro do parentes, dentro das aspas do f, não pode ter outra igual, então, se inicia com aspa duplas ""
# e dentro precisa de aspas use a simples, se incia com a simples, dentro use as " "
print(f"A primeira vez que aparece um 'ideo' é na {cadeia.lower().find('ideo')} posição")
# aqui transformei a frase em munusculo e procurei ideo em minusculo  
print(f"A primeira vez que aparece um 'IDEO' é na {cadeia.upper().find('IDEO')} posição")
print(f"A primeira vez que aparece um 'Ideo' é na {cadeia.capitalize().find('Ideo')} posição")
# aqui irá dar -1 (não existe) porque Ideo vem da palavra video, e capitalize deixa apenas a 1° maiúscula, não as outras
# ficando "Curso Em Videos"
print(f"A primeira vez que aparece um 'tuba' é na {cadeia.find('tuba')} posição")
# aqui o retorno será -1, e -1 = a não encontrado/ não existe

# ------------------------------------------------------------------------------------#
#                                     in- tem no                                      #
# ------------------------------------------------------------------------------------#

print(f"\nTem em dentro da frase Curso em video? {'em'in cadeia}")
# resposta True
print(f"Tem lha dentro da frase Curso em video? {'lha'in cadeia}")
# resposta False


#                                       TRANSFORMAÇÃO

# ====================================================================================#
#                            replace - trocar/ reposicionar                           #
# ====================================================================================#

muda = cadeia.replace("em","dentro")
print(f"\nFicou '{muda}'")

# ====================================================================================#
#                            upper - fontes MAIÚSCULAS                                #
# ====================================================================================#

f = "tudo em maiúsculo"
print(f.upper())
# uper é um método, tem de ter () no final

# ====================================================================================#
#                            lower - fontes minúsclua                                 #
# ====================================================================================#

c = "FRASE TODA MAIÚSCULA"
print(f"FRASE TODA MINÚSCULA -> '{c.lower()}'")

# ====================================================================================#
#                      capitaliza - só 1° letra fica maiúscula                        #
# ====================================================================================#

d = "Deixa Só A Primeira MAIÚSCULA"
print(f"Deixa Só A Primeira MAIÚSCULA -> '{d.capitalize()}'")

# ====================================================================================#
#                      title - todas 1°s letras das palvras em maiúscula                      #
# ====================================================================================#

e = "as primeiras LETRAS SERÃO em maiúsculo"
print(f"as primeiras LETRAS SERÃO em maiúsculo -> '{e.title()}'")

# ====================================================================================#
#                       strip - remoce epaços no início e fim                         #
# ====================================================================================#

s = "     arrumando espeços sobrando        "
print(f"     arrumando espeços sobrando         -> '{s.strip()}'")
# tem 5 espaços no início e 8 no final

# r = right    - coloca rstring - só pega os final - direita
# l = lefth    - coloca lstring - só pega os iniciais - esquerda


#                                       DIVISÃO

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                   split - divide a string considerando os espaços                    #
#                    cada pavra recebe um índice novo, é recolocada                    #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

frase = "Cavalo bebeu a água do bebê valdo"
frase = frase.split()
print(f"\nSeparando e crianod lista de palavras {frase}")
#retorno = Separando e crianod lista de palavras ['Cavalo', 'bebeu', 'a', 'água', 'do', 'bebê', 'valdo']

# era
# C a v a l o   b e b e  u     a     a  g  u  a     d  o     b  e  b  e     V  a  l  d  o
# 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32
# ficaria
# C a v a l o  b e b e u  a  a g u a  d o  b e b e  V a l d o
# 0 1 2 3 4 5  0 1 2 3 4  0  0 1 2 3  0 1  0 1 2 3  0 1 2 3 4
#     0           1       2     3      4      5        6            são 7 palavras
# como se separasse em blocos, criando uma lista com todas as palavras
 
print(f"pega o dado no índice 1 '{frase[1]}' e diga o que tem na posição 4 '{frase[1][4]}\n")

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#
#                             join - junta a string seprada                            #
#                    pode por separador ou espaço entre as palvras                     #
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~#

junte = "".join(frase)
print(junte)
# retorno: Cavalo ~ bebeu ~ a ~ água ~ do ~ bebê ~ valdo
# observar que como coloquei espaço dentro do aspas, sai com espaço se fizer sem fica sem espaço

junto = ">".join(frase)
print(junto)
# retorno: Cavalo>bebeu>a>água>do>bebê>valdo
# aqui não tem espaço dentro das " "



###########################################################################################
#                                                                                         #
#                                    Exercícios em aula                                   #
#                                                                                         #
###########################################################################################

#%%
# exe 22
# escreva um nome completo e mostre tudo me maiúsculo, minúsculo, letras sem epaço, quantas letras no 1° nome

nome = input("nome completo: ")

print(nome.upper())    # sem ver
print(nome.lower())    # sem ver
print(f"tem {len(nome)} letras")       # estava pondo len.nome, está errado. Correta é chamar len e dentro do parentes a lista

# para tirar os espaços irei usar 1° posição o que não quero e na 2° como tem que se comportar
# len para percorrer e contar
# replace é para t rocar
# " ", "" trocar espaço em branco por nada, juntar 

print(len(nome.replace(" ", "")))            #tive de ver

fat = nome.split()   # é split e não strip
#print(fat)
print(len(fat[0]))
# outra forma que o prof fez, também está certo

#%%

#correção professor 22

# strip tira espaços antes e depois, mas mantém espaço entre palavras
nome = input("nome completo: ").strip()

# forma antiga de fazer print
print("Tudo minúsculo {}".format(nome.lower()))
print("Tudo maiúsculo {}".format(nome.upper()))
#quero tirar espaços entre cacacteres - (-nome.count(' '))- contador de espaços
print("tamanho/ caracteres {}".format(len(nome) - nome.count(" ")))
# vai procurar o 1° espaço e contar caracteres até ele
print(f"O primeiro nome tem {nome.find(" ")}")


# %%

# exer 23
# ler um número entre 0 9999 e retornar separados

numString = input("numero de 0 a 9999: ")
numInt = int(numString)

if numInt < 10:
    print(f"unidade {numString[0]}")
elif numInt < 100:
    print(f"""unidade {numString[0]}
          dezena {num[1]}""")
elif numInt < 1000:
    print(f"""unidade {numString[0]}
          dezena {numString[1]}
          centena {numString[2]}""")
else:
        print(f"""unidade {numString[0]}
          dezena {numString[1]}
          centena {numString[2]}
          milhar {numString[3]}""")
        
#%%

# correção do prof 23

# usou forma matemética, pois não entrou em laço

# pega unidade e divide por inteiro 1 e tira módulo por 10 (resto %)
numero = int(input("Digite n° até 9999:  "))

uni = numero // 1 % 10
dez = numero // 10 % 10
cen = numero // 100 % 10
mil = numero // 1000 % 10

print(f"unidade: {uni} \ndezena: {dez} \ncentena: {cen} \nmilhar: {mil} ")

# %%

# ex 24 crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "santo"

p = input("digite nome de uma cidades")
print(f"A cidade {p} tem 'Santo' em seus caractere {p.find('santos')} posição")

# %%

# correção prof 24

cidade = input("Nome da cidade: ").strip()
#lembrado que strip é para tirar espaços no ínicio e fim

print(cidade[:5].upper() == "SANTO")
# pega valor de entrada, os 5 1°s caracteres e vê see é igual a palavra SANTOS em maiúsculo
# a frase foi converetida a maiúsculo com o a função .upper()

#%%

# exerecico 25

# ver se tem silva no nome

nome = input("Digite um nome: ").strip()

print(f"Existe a palavra 'SILVA' NESTE NOME?\nNo índice: {nome.upper().find("SILVA")}\nSe índico for '-1', é porque não existe.")

# %%
 # correção professor 25
 # ele deixou tudo em minusculo, e fez com in
 
nome = input("Digite um nome: ").strip()

print(f"Seu nome tem 'Silva'?\n{"silva" in nome.lower()}")

#%%

# exercício 26
# Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.

palavras =  input("digete uma frase: ")
print(f"Na frase {palavras} há {palavras.lower().count("a")} 'a'")
print(f"O primeiro 'a' está no índice {palavras.lower().find("a")}")

# tentei fazer com -1, para vir de tras para frente mas não deu certo


# %%

# correção professor

# PARA QUE O RETORNO DO ÍNDICE SEJA DE POSIÇÃO 1°, 2° ... COLOCA-SE NA FRETE +1 (INDICE 0 +1)
# PROFESSRO USOU O R E L ANTES DO NOME DA FUNÇÃO - R - DIREITA L -ESQUEDAR
# R - IRÁ LER DO LADO DIREITO (-1) PARA ESQUERDO 

# fez tratamento de espeço e deixou direto no input/entrada a conversão para maiúsculo

palavras =  input("digete uma frase: ").upper().strip()
print(f"Na frase {palavras} há {palavras.lower().count("a")} 'a'")
print(f"O primeiro 'a' está no índice {palavras().find("a")+1}")
print(f"O primeiro 'a' está no índice {palavras().rfind("a")+1}")


# %%

# exerc 27 
#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = input("Digite nome completo: ").strip()
#deixei sem espaço na frente e trás

divide = nome.split()
print(f"O primeiro nome da pessoa é {divide[0].capitalize()} e o último sobrenome é {divide[-1].capitalize()}")
# -1 faz ler do último ao primeiro
# deixei com 1° letra sempre maiúscula

# %%

# correção prof 27

nomes = input("Digite nome: ").strip()
corta = nomes.split()
print(f"O primeiro nome da pessoa é {corta[0].capitalize()} e o último sobrenome é {corta[len(corta)-1].capitalize()}")


