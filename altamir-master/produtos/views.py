from django.shortcuts import render
from produtos.models import Produto

def index(request):
    produtos = Produto.objects.filter(categoria__nome="Livro")
    return render(request, 'produtos/listar.html', {'produtos': produtos})
    