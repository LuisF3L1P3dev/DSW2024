# Tipos e estruturas de dados
# Crie uma lista com 10 números inteiros.
# Escreva uma função que receba essa lista e retorne:
# O maior valor.
# O menor valor.
# A média dos valores.


l1 = list(range(10))

def v_lista(lista):
  maior_n = max(lista)
  return 'O maior número da lista é:', maior_n

saida = v_lista(l1)
print(saida)