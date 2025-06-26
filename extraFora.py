def dia (mm, dd):
    if mm == 8 or mm//2 != 0:
        d = dd + 1
        if d > 31:
            d = 1
    else:
        if d > 30:
            d = 1
    
    return d

def mes (mm, dd):
    dias = dia(mm, dd)    # fiz assim dias = dia() e está errada, deve por os parâmetros dentro 
    if dias == 1:
        m = mm + 1
    if m > 12 :
        m = 1
    
    return m

def ano (aa, mm):
    meses = mes(mm)
    if meses == 1:
        a = aa + 1
    return a

#main

niver = input("\ndigite dd/mm/aaaa: ")

separa = niver.split("/")

aa = ano(int(separa[2]))

mm = mes(int(separa[1]))

dd = dia(int(separa[1]), int(separa[0]))


print(f"{dd}/{mm}/{aa}")