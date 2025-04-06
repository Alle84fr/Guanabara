
# tipos primitivo e saídas de dados
# os 4 fundamentais - há mais
# int = inteiro sem ponto           ex: 1
# float = fracionado, com ponto     ex: 1.0
# string = caracteres               ex: "um"
# booleano = True ou False

# ! soma dois números !

n1 = int(input("\nnumero1: "))
n2 = int(input("numero2: "))

soma = n1 + n2
subtraia = n1 - n2
divida = n1 / n2
resto = n1 % n2
inteiro = n1 // n2
elevado = n1 ** n2

print(f""" n1 = {n1} || n2 = {n2}
soma '+' = {soma}   #fez só soma
subtraia '-' = {subtraia}
divida '/' = {divida}
resto '%' = {resto}
inteiro // = {inteiro}
elevado '**' = {elevado}""")


# forma antiga de concatenar, só para ter o que foi dito no vídeo

print("para ficar com print igual ao do professo, vou usar o mais novo, com f")
print(" A soma de", n1, "e", n2, "é igual a", soma)
print("A soma enre {} e {} é {}".format(n1, n2, soma))

# saber se o valor é  numérico, resultado será bool 
# deve ser entrada como str

x = input("\ndigite só numeros: ")
y = input("digite só texto: ")
r = input("digite caracteres: ")

print(f"\no tipo do {x} é {type(x)}")
print(f"isalnum é {x.isalnum()}, todos caracteres devem ser alfa numéricos = letras ou n°s")
print(f"isalnum é {x.isalpha()}, todos caracteres devems ser letras")
print(f"isalnum é {x.isdecimal()}, todos devem ser decimais (0-9)")
print(f"isalnum é {x.isupper()}, todas letras devem ser maiúsculas")
print(f"isalnum é {x.islower()}, todas letras devems ser minúsculas")
print(f"isalnum é {x.isnumeric()}, todos caracteres devems ser numéricos ( contandi dígitos especiais como VII)")

print(f"\no tipo do {y} é {type(y)}")
print(f"isalnum é {x.isalnum()}, todos caracteres devem ser alfa numéricos = letras ou n°s")
print(f"isalnum é {x.isalpha()}, todos caracteres devems ser letras")
print(f"isalnum é {x.isdecimal()}, todos devem ser decimais (0-9)")
print(f"isalnum é {x.isupper()}, todas letras devem ser maiúsculas")
print(f"isalnum é {x.islower()}, todas letras devems ser minúsculas")
print(f"isalnum é {x.isnumeric()}, todos caracteres devems ser numéricos ( contandi dígitos especiais como VII)")

print(f"\no tipo do {r} é {type(r)}")
print(f"isalnum é {x.isalnum()}, todos caracteres devem ser alfa numéricos = letras ou n°s")
print(f"isalnum é {x.isalpha()}, todos caracteres devems ser letras")
print(f"isalnum é {x.isdecimal()}, todos devem ser decimais (0-9)")
print(f"isalnum é {x.isupper()}, todas letras devem ser maiúsculas")
print(f"isalnum é {x.islower()}, todas letras devems ser minúsculas")
print(f"isalnum é {x.isnumeric()}, todos caracteres devems ser numéricos ( contandi dígitos especiais como VII)\n")

#"\n no início é para pular linha antes do print"
#"\n no final é para pular linha depois do print"
# cls clear screen - limpar tela
# se por print(f"isalnum é {x.islower}, todas letras devems ser minúsculas") sem () retorna endereço, acho eu, não o valor
