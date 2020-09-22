from django.shortcuts import render
from django.contrib.auth.models import User
from django.views.generic.base import TemplateView
from django.http import HttpResponse
from django.views import View



def home(request):

    return render(request, 'home/home.html')

class HomePageView(TemplateView):
    template_name = 'home/home2.html'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['minha_variavel'] = 'Seja bem vindo ao curso'
        return context


class MyView(View):

    def get(self, request, *args, **kwargs):
        return render(request,'home/home3.html')


    def post(self, request, *args, **kwargs):
        return HttpResponse('Post')


