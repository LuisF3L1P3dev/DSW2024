# Manipulação de strings
# Escreva uma função que receba um texto e:
# Conte quantas vogais existem.
# Retorne o texto invertido.
# Verifique se o texto é um palíndromo.

vogais ='aeiou'
quant = []
def ver_palavra(palavra):
    #quantas vogais?
    for i in palavra:
        if i in vogais:        
            quant.append(i)
    return print(f'A palavra {palavra} tem :', len(quant),'vogais')

def inverter(palavra):
    palavra_invertida = palavra[::-1]
    return print(palavra_invertida)

def palindromo(texto):
    if texto.replace(" ", "") == texto.replace(" ", "")[::-1]:
        return print(True)
    else:
        return print(False)

ver_palavra('Rangelu')
inverter('Luis')
palindromo('subi no onibus')


