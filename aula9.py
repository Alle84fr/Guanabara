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

print(f"A primeira vez que aparece um e na na {cadeia.find('e')} posição")
# observação - dentro do parentes, dentro das aspas do f, não pode ter outra igual, então, se inicia com aspa duplas ""
# e dentro precisa de aspas use a simples, se incia com a simples, dentro use as " "
print(f"A primeira vez que aparece um ideo na na {cadeia.find('ideo')} posição")
print(f"A primeira vez que aparece um ideo na na {cadeia.find('tuba')} posição")
# aqui o retorno será -1, e -1 = a não encontrado/ não existe

# ------------------------------------------------------------------------------------#
#                                     in- tem no                                      #
# ------------------------------------------------------------------------------------#

print(f"Tem em dentro da frase Curso em video? {'em'in cadeia}")
# resposta True
print(f"Tem lha dentro da frase Curso em video? {'lha'in cadeia}")
# resposta False


#                                       TRANSFORMAÇÃO

# ====================================================================================#
#                            replace - trocar/ reposicionar                           #
# ====================================================================================#

repl = cadeia.replace("em","dentro")
print(f"Ficou '{repl}'")

# ====================================================================================#
#                            upper - fontes MAIÚSCULAS                                #
# ====================================================================================#

f = "tudo em maiúsculo"
print(f"tudo em maiúsculo -> '{f.upper()}'")
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
#                      title - 1° letras da palvras em maiúscula                      #
# ====================================================================================#

e = "as primeiras LETRAS SERÃO em maiúsculo"
print(f"as primeiras LETRAS SERÃO em maiúsculo -> '{e.title()}'")

# ====================================================================================#
#                       strip - remoce epaços no início e fim                      #
# ====================================================================================#

s = "     arrumando espeços sobrando        "
print(f"     arrumando espeços sobrando         -> '{s.strip()}'")
# tem 5 espaços no início e 8 no final

# r = right    - coloca rstring - só pega os final - direita
# l = lefth    - coloca lstring - só pega os iniciais - esquerda

#                                       DIVISÃO