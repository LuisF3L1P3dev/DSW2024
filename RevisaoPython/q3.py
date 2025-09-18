'''Dicionários e compreensão de listas
Dada a lista de nomes ["Ana", "Bruno", "Carlos", "Ana", "Bruno", "Ana"], 
crie um dicionário que mostre quantas vezes cada nome aparece.
Extra: transforme em uma list comprehension que retorna apenas 
os nomes que aparecem mais de uma vez.'''


nomes = ["Ana", "Bruno", "Carlos", "Ana", "Bruno"]
dicionario = {}

for i in nomes:
    if i in dicionario:
        dicionario[i]=+ 1
