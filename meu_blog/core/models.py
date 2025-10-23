from django.db import models

# Create your models here.
class Autor(models.Model):
    nome = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    biografia = models.TextField()

class Post(models.Model):
    titulo = models.CharField(max_length=50)
    conteudo = models.TextField()
    data_pub = models.DateTimeField(auto_now_add=True)
    status = models.BooleanField()