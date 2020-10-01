from django.shortcuts import render
from django.views import View
from .models import Vendas
from django.http import HttpResponse




class DashboardView(View):
    def dispatch(self, request, *args, **kwargs):           #permissao para ver o dashboard
        if not request.user.has_perm('vendas.ver_dashboard'):
            return HttpResponse('Acesso negado')

        return super(DashboardView, self).dispatch( request, *args, **kwargs)

    def get(self, request):
        data = {}
        data['media'] = Vendas.objects.media()
        data['media_desc'] = Vendas.objects.media_desconto()
        data['min'] = Vendas.objects.min()
        data['max'] = Vendas.objects.max()
        data['n_ped'] = Vendas.objects.num_pedidos()
        data['n_ped_nfe'] = Vendas.objects.num_ped_nefe()


        return render(request, 'vendas/dashboard.html', data)
