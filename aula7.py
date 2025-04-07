# operações aritméticas
# operando  operador  operando  igualdade  resultado   

n = int(input("\nnumero um ")) #cuidado por tipo antes do input, salvo ser for str
x = int(input("numero dois "))
print (f"\na soma de {n} + {x} == {n+x}")
print (f"a subtração de {n} - {x} == {n-x}")
print (f"a multiplicação de {n} * {x} == {n*x}")
print (f"a divisão de {n} / {x} == {n/x}  ----> pode retonar int ou float, usa as casas após a vírgula")
print (f"a div inteira de {n} // {x} == {n//x} ----> ela pega apenas o valor antes da vírgula")
print (f"o resto de {n} % {x} == {n%x}  ----> valor que sobra fora do ressultado ex f5/2 -> resultado 2 resto 1")
print (f"a potência de {n} ** {x} == {n**x}  ----> ex 5**3 - base é 5 , potência 3 - 5 elevado a 3 = 5x5x5 \n")

#se quiser rodar sem dar play é só digitar no terminal python nomeFile.extensão ex python aula7.py


nu1 = 20
nu2 = 14
nu3 = 15
nu4 = 5
nu5 = 2
nu6 = 2
nu7 = 3
nu8 = 3

v1 = nu4 + nu5
v2 = nu3 - v1
v3 = nu6 ** nu7
v4 = nu2 / v2
v5 = v3 * nu8
v6 = nu1 + v4
v7 = v6 - v5


print (f"\n{nu1} + {nu2} / ({nu3} - ({nu4} + {nu5})) - {nu6} ** {nu7} * {nu8}")
print (f""" ordem de procedência - o que são vistos e feitos
       1° fará o que está dentro do () - > {nu4} + {nu5} = {v1}
       2° fará o que está dentro do () - > {nu3} - ({nu4} + {nu5})) = {v2}
       3° fará a elevação - > {nu6} ** {nu7} = {v3}
       4° fará - > {nu2} / {v2} = {v4}
       5° fará  - > {v3} * {nu8} = {v5}
       6° fará - > {nu1} + {v4} = {v6}
       7° fará - > {v6} - {v5} = {v7}""")
print(f"resultado : {nu1+ nu2 / (nu3 - (nu4 + nu5)) - nu6 ** nu7 * nu8}\n")

# Concatenização

print("Conta" + "tena")

# repetição de caracteres

print("_" * 15)

# formatando print alinhamento em espaços
a = "gustaco"
print(f"\nalinhas a 21 caracteres {a:21} espaço branco a esqueda")
print(f"alinhar a 21 caracteres {a:>21} espeços branco a direita")
print(f"alinhar a 21 caracteres {a:^21} espeço branco centralizado")
print(f"substitui espaço em branco por algo {a:¨^15} ¨ no espali em branco centralizado")
print(f"substitui espaço em branco por algo {a:👻^15} ¨ no espali em branco centralizado\n")

print("Agora estou vendo a quebra de linhas\n sem usar ''' \n mas usando \ n onde quero quebrar\n funciona")


# exercício 05
# faça um número e mostre na tela o seu sucesso e antecessor

valor = int(input("\ndigite valor: "))

print(f"o antecessor de {valor} é\n {valor - 1}\n o sucessor é\n {valor + 1} ")

# exercíco 06 
#Crie algoritmo que mostre seu dobro, triplo e quadrupo

print(f" o dobro de 7 é {7*2} \n o triplo de 7 é {7*3}\n o quadruplo de 7 é {7*4}")

# execício 07
# calcular média de 3 notas

print(f"\nnota1: 5.1 , nota2: 7.7, nota3: 6.8 \n a média é {(5.1+7.7+6.8)/3}")

# exercício 08
# pegar valor em metro e converter para cm e mm

metro = float(input("\nDigite um valor de metro para ser convertido, usar . : "))
print(f"{metro} m equivale a:\n {metro*100} cm\n {metro*1000} mm\n")

#exercíco 09
# exercío tabuada - não vou usar método não dado

tab = int(input("digite valor de 2 a 9: "))
print(f" a tabuado do {tab} é:")
print(f"1*{tab} = {tab*1}")
print(f"2*{tab} = {tab*2}")
print(f"3*{tab} = {tab*3}")
print(f"4*{tab} = {tab*4}")
print(f"5*{tab} = {tab*5}")
print(f"6*{tab} = {tab*6}")
print(f"7*{tab} = {tab*7}")
print(f"8*{tab} = {tab*8}")
print(f"9*{tab} = {tab*9}")
print(f"10*{tab} = {tab*10}\n")

#exercío 10
# conversão para dolar

dinh = float(input("Quando vc quer converter? "))
print(f"com dolar valendo 5.84, seu R$ {dinh} vale: $ {dinh/5.84}")
print(f"com euro valendo 6.14, seu R$ {dinh} vale: € {dinh/6.41}")
print(f"com libra estrellina valendo 7.39, seu R$ {dinh} vale: £ {dinh/7.39}")
print(f"com iene estrellina valendo 0.04, seu R$ {dinh} vale: JP¥ {dinh*0.04}")
print(f"com peso estrellina valendo 0.0045, seu R$ {dinh} vale: JP¥ {dinh*0.0045}\n")

# Exercício 11
# ler largura(l) e altura (h) calcular área e mais quatidade de tinta (1l = 2m**2)

l = 2
h = 1.5
area = l * h
litros = area/2
print(f"para pinta {area} de parede com l {l} e altura {h} usa-se {litros} litros de tinta\n")

# Exercício 12
# 5 % de desconto

real = 15.25
porc = 15.25 * (1-0.15)
# porce recebe valor que será multiplocado por ( 1 seria o inteiro/100% - 0.15 que quanto vou decontar = 85%)
# ou pode fazer direto  %%%%%%%%%%%%%%%%%%%%% 15.25 * 0.85 %%%%%%%%%%%%%%%

print(f"15 % de desconto de R$ {real} é R$ {porc}")
print(f"formula 15.25 * (1-0.15)")

# Exercício 13
# 5 % de aumento

porce = 15.25 * 1.15
# aqui tem o valor * (100%(1) mais os 15%(0.15)

print(f"15 % de aumento de R$ {real} é R$ {porce}")
print(f"formula 15.25 * 1.15\n")