# Cores no Terminal

# omo utilizar os códigos de escape sequence ANSI (no terminal) para configurar cores para os seus programas em Python. Veja como utilizar o código \033[m com todas as suas principais possibilidades.

# começa com contrabarra \033[ m
# o m fecha o cód
# pode por cód de estilo textcolor background
# pode poder na ordem que quiser

# \033[0; 33; 44m

# cód para estilo 0 = sem estilo/normal - reset (pode deixar estar vazio neste caso)
# Text Sytel      1 = negrito - bold
#                 2 = mais claro - faint/low intendity
#                 3 = itálico - italic
#                 4 = sublinhado - underline  #não consegui enchergar o sublinhado, não se se estava muito na margem
#                 5 = piscar lento - slow blink  #não piscou, atualmente este cód é ignorado pelos terminais - usar time.sleep() 
#                 7 = inverte cor do texto e fundo - reverse/Swap FG/BG
#                 8 = invisível - hidden/Conceal
#                 9 = riscado - strikethrough

# cód para cores    30 = preto - black
# Foreground Colors 31 = vermelho - red
#                   32 = verde - green
#                   33 = amarelo - yellow
#                   34 = azul - blue
#                   35 = roxo - purple
#                   36 = ciano - cyan
#                   37 = cinza - padrão - gray // alguns casos branco
# cód para cores brilhantes    90 = preto - black
# Bright                       91 = vermelho - red
#                              92 = verde - green
#                              93 = amarelo - yellow
#                              94 = azul - blue
#                              95 = roxo - purple
#                              96 = ciano - cyan
#                              97 = branco verdadeiro - bright white


# cód para fundo 40 = preto - black  #ficou amarelo
#                41 = vermelho - red
#                42 = verde - green
#                43 = amarelo - yellow
#                44 = azul - blue
#                45 = roxo - purple
#                46 = ciano - cyan
#                47 = cinza - padrão - gray  # ficou braco sujo
# cód para fundo Brilhante 100 = cinza claro - bright light gray
# Bright                   101 = vermelho - red
#                          102 = verde - green
#                          103 = amarelo - yellow
#                          104 = azul - blue
#                          105 = rosa - purple   # no meu termonal ficou amarelo
#                          106 = ciano - cyan
#                          107 = branco - white

# todos estão entre ponto e virgula ;

#DEVE POR O CÓD DENTRO DAS ASPAS DO PRINT

#                      PARA NÃO SEGUIR COM A CONFIGURAÇÃO, NO FINAL DO COMANDO POR \033[m, SERIA MARCAÇÃO FINAL
print("\n\033[1;97;45m o cód é negrito; texto branco; fundo roxo\033[m\n")
print("\033[2;33;41m o cód é mais claro; texto amarelo, fundo vermelho\033[m\n")
print("\033[3;36;47m o cód é itálico; texto ciano, fundo cinza\033[m\n")
print("\033[4;34;42m o cód é sublinhado; texto azul, fundo verde\033[m\n")
print("\033[5;31;47m o cód é picar lento; texto vermelho\033[m\n")
print("\033[7;33;40m o cód é inverter; texto cinza, fundo branco\033[m\n")
print("\033[8;33;46m o cód é invisível\033[m\n")
print("\033[9;33;45m o cód é riscado; texto amarelo, fundo roxo\033[m\n")

print("\n\033[1;97;100m cinza\033[m\n")
print("\033[2;33;101m vermelho\033[m\n")
print("\033[3;36;102m verde\033[m\n")
print("\033[4;34;103m amarelo\033[m\n")
print("\033[5;31;104m azul\033[m\n")
print("\033[7;33;105m rosa/purple\033[m\n")
print("\033[8;33;106m ciano\033[m\n")
print("\033[9;33;107m branco\033[m\n")

print("\n\033[7;97;40m inverter branco e preto\033[m\n")

print("\nCor \033[95m roxo vivo\033[m e a cor \033[96m ciano vivo \033[m\n")