class Pessoa:
  def __init__(self, nome, idade, email):
    self.nome = nome
    self.idade = idade
    self.email = email
  
  def __str__(self):
    return 'Nome:{}\nIdade:{}\nEmail:{}'.format(self.nome, str(self.idade), self.email)
  

p1 = Pessoa('Luis', 22, 'dantas@gmail.com')
p2 = Pessoa('Davi', 18, 'davi@gmail.com')
p3 = Pessoa('Lucas', 20, 'Lucas@gmail.com')

print(p1,'\n')
print(p3,'\n')
print(p2,'\n')

