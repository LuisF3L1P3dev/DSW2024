'''1 - Classe simples
Crie uma classe Pessoa com atributos: nome, idade e email.
Crie um método que exiba as informações da pessoa em formato
de string. Instancie pelo menos 3 objetos e teste.'''

'''2 - Encapsulamento e validação
Na classe Pessoa, garanta que a idade não pode ser negativa.
Adicione um método aniversario() que aumenta a idade em 1.'''

class Pessoa:
  def __init__(self, nome, idade, email):
    self.nome = nome
    if idade < 0:
      raise ValueError('Idade não pode ser negativa')
    self.idade = idade
    self.email = email
  
  def __str__(self):
    return 'Nome:{}\nIdade:{}\nEmail:{}'.format(self.nome, str(self.idade), self.email)
  
  def aniversario(self):
    self.idade += 1

p1 = Pessoa('Luis', 22, 'dantas@gmail.com')
p2 = Pessoa('Davi', 18, 'davi@gmail.com')
p3 = Pessoa('Lucas', 20, 'Lucas@gmail.com')

p1.aniversario()
print(p1,'\n')
print(p3,'\n')
print(p2,'\n')

