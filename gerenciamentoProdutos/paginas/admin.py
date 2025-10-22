from django.contrib import admin
from .models import *

# Register your models here.
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ['nome','codigo','preco','quantidade', 'data_criacao']
    list_filter = ['nome', 'codigo']
    search_fields = ['data_criacao']
    ordering = ['-data_criacao']

admin.site.register(Produto,ProdutoAdmin)