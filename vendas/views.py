from django.shortcuts import render
from django.views import View
from .models import Vendas




class DashboardView(View):
    def get(self, request):
        data = {}
        data['media'] = Vendas.objects.media()
        data['media_desc'] = Vendas.objects.media_desconto()
        data['min'] = Vendas.objects.min()
        data['max'] = Vendas.objects.max()
        data['n_ped'] = Vendas.objects.num_pedidos()
        data['n_ped_nfe'] = Vendas.objects.num_ped_nefe()


        return render(request, 'vendas/dashboard.html', data)
