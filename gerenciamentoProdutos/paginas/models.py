from django.db import models

# Create your models here.
class Produto(models.Model):
  nome = models.CharField(max_length=50)
  codigo = models.CharField(max_length=50)
  descricao = models.TextField()
  preco = models.DecimalField(decimal_places=2, max_digits=5)
  quantidade = models.IntegerField()
  data_criacao = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    return self.nome