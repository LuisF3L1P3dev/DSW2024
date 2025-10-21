from django.shortcuts import render

# Create your views here.

def index(request):
   return render(request, 'paginas/index.html')

def base(request):
   return render(request, 'base.html')

def portfolio(request):
   return render(request, 'paginas/portfolio.html')

def destaques(request):
   return render(request, 'paginas/destaques.html')

def sobre(request):
   return render(request, 'paginas/sobre.html')

def contato(request):
   return render(request, 'paginas/contato.html')