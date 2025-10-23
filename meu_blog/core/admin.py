from django.contrib import admin
from .models import Autor, Post
# Register your models here.


class AutorAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email']
    search_fields = ['nome']

admin.site.register(Autor, AutorAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['titulo','status','data_pub']
    list_filter = ['status','data_pub']
    search_fields = ['titulo']
    ordering = ['-data_pub']
admin.site.register(Post, PostAdmin)
