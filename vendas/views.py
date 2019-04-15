from django.shortcuts import render
from django.views import View
from django.db.models import Sum, F, Max, Avg, Min, FloatField, Count
from .models import Venda
from django.http import HttpResponse


class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso negado, voce precisa de permissao!')
        return super(DashboardView, self).dispatch(request, *args, **kwargs)

    def get(self, request):

        data = {}
        data['media'] = Venda.objects.media()
        data['media_desc'] = Venda.objects.media_desconto()
        data['min'] = Venda.objects.min()
        data['max'] = Venda.objects.max()
        data['count'] = Venda.objects.all().aggregate(Count('id'))['id__count']
        data['n_ped_nfe'] = Venda.objects.n_ped_nfe()
        return render(request, 'vendas/dashboard.html', data)

class NovoPedido(View):
    def get(self, request):
        return render(request, 'vendas/novo-pedido.html')

    def post(self, request):
        data = {}
        data['numero'] = request.POST['numero']
        data['desconto'] = float(request.POST)['desconto']
        data['venda'] = (request.POST)['venda_id']

        if data['venda']:
            venda = Venda.objects.get(id=data['venda'])
        else:
            venda = Venda.objects.create(
                numero=data['numero'], desconto=data['desconto'])

        itens = venda.itemdopedido_set.all()
        data['venda_obj'] = venda
        data['itens'] = itens
        return render(
            request, 'vendas/novo-pedido.html')