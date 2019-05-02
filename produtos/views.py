from django.shortcuts import render
from django.http import HttpResponse
from produtos.models import Produto
from django.views.generic import View
from django.shortcuts import render, redirect, get_object_or_404

# Create your views here.

class ProdutoBulk(View):
    def get(self, request):
        produtos = ['Banana', 'Maca', 'Limao', 'Laranja', 'Pera', 'Melancia']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')