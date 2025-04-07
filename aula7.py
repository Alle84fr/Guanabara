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
#Crie algoritmo que mostre seu dobro, triplo e quadrupo, (add raiz quadrada)
# raiz quadrada é n**(1/2) ou n ** 0.5 -->  este tinha errado, não sabia como fazer a raiz

# valor:.n°f - mosta n° de casas após o ponto ex: {real:.2f} sai float(f) = 45.25 e não 45.25896

print(f" o dobro de 7 é {7*2} \n o triplo de 7 é {7*3}\n o quadruplo de 7 é {7*4}\n a raiz quadrada de 7 é {7**0.5:.3f}")

# execício 07
# calcular média de 3 notas

print(f"\nnota1: 5.1 , nota2: 7.7, nota3: 6.8 \n a média é {(5.1+7.7+6.8)/3:.2f}")

# exercício 08
# pegar valor em metro e converter para cm e mm

metro = float(input("\nDigite um valor de metro para ser convertido, usar . : "))
print(f"{metro} m equivale a:\n {metro*100:.0f} cm\n {metro*1000:.0f} mm\n")

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
print(f"com dolar valendo 5.84, seu R$ {dinh} vale: $ {dinh/5.84:.4f}")
print(f"com euro valendo 6.14, seu R$ {dinh} vale: € {dinh/6.41:.4f}")
print(f"com libra estrellina valendo 7.39, seu R$ {dinh} vale: £ {dinh/7.39:.4f}")
print(f"com iene estrellina valendo 0.04, seu R$ {dinh} vale: JP¥ {dinh*0.04:.4f}")
print(f"com peso estrellina valendo 0.0045, seu R$ {dinh} vale: JP¥ {dinh*0.0045:.4f}\n")

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
porc = 15.25 * (1-0.05)
# porce recebe valor que será multiplocado por ( 1 seria o inteiro/100% - 0.15 que quanto vou decontar = 85%)
# ou pode fazer direto  %%%%%%%%%%%%%%%%%%%%% 15.25 * 0.85 %%%%%%%%%%%%%%%

# professor = 15.25*5/100   errei, coloquei 15% e não 5

print(f"5 % de desconto de R$ {real} é R$ {porc:.2f}")
print(f"formula 15.25 * (1-0.15)")

# Exercício 13
# 15 % de aumento

porce = 15.25 * 1.05
# aqui tem o valor * (100%(1) mais os 15%(0.15)

# professor = 15.25 + (15.25*15/100)   

print(f"15 % de aumento de R$ {real} é R$ {porce:.2f}")
print(f"formula 15.25 * 1.15\n")

#exercicios 14
#converta os graus
# de C (celsos) para F (Fahrenheit) -> F = C*(9/5)+32   ou   F = C*1.8+32
# 100°C é o intervalo de H2O fervente a congelada = 180°F
# 32°F é de congelamento (0°C)

# de F para C = C = ((F -32)*5)/9

print(f"De Fahrenheit (85°) para Celsos = C = ((F -32)*5)/9 = {((85-32)*5)/9}°C")
print(f"De Celsos (85°) para Fahrenheit = F = C*(9/5)+32 = {85*(9/5)+32}°F\n")

#exercício 15
# aluguem de carro - km percorrido(0.15/km) _ dias(60/d)

km = float(input("Quantos km foi percorrido: "))
dia = int(input("Quantos dias: "))
print(f"Sendo o carro alugado por {dia} dias, com valor de R$60.00\n Tendo o carro rodado {km} km, com valor de R$0.15")
print(f"O valor a ser pago será {(km*0.15)+(dia*60):.2f}\n")