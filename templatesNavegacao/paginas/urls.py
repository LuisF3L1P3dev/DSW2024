from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('base/', views.base, name='base'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('destaques/', views.destaques, name='destaques'),
    path('sobre/', views.sobre, name='sobre'),

]