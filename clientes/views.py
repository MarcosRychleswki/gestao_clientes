from django.http import HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Person
from produtos.models import Produto
from vendas.models import Vendas
from .forms import PersonForm
from django.views.generic.list import ListView
from django.views.generic.list import View
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy


# TODO lembrete de coisas a melhorar ou fazer
# Create your views here.
@login_required
def persons_list(request):
    persons = Person.objects.all()
    return render(request, 'person.html', {'persons': persons})


@login_required

def persons_new(request):
    if not request.user.has_perm('clientes.add_person'):
        return HttpResponse('Nao autorizado')
    elif not request.user.is_superuser:               #sistema de permissao
        return HttpResponse('Nao e superuser')

    form = PersonForm(request.POST or None, request.FILES or None)

    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_update(request, id):
    person = get_object_or_404(Person, pk=id)
    form = PersonForm(request.POST or None, request.FILES or None, instance=person)
    if form.is_valid():
        form.save()
        return redirect('persons_list')
    return render(request, 'person_form.html', {'form': form})


@login_required
def persons_delete(request, id):
    person = get_object_or_404(Person, pk=id)

    if request.method == 'POST':
        person.delete()
        return redirect('persons_list')

    return render(request, 'person_delete_confirm.html', {'person': person})


class PersonList(LoginRequiredMixin, ListView):#sempre a esquerda o LoginRequiredMixin pois ele tem que ser o primeiro
    model = Person
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        primeiro_acesso = self.request.session.get('primeiro_acesso',False)

        if not primeiro_acesso:
            context['message']= 'Seja bem vindo ao seu primeiro acesso'
            self.request.session['primeiro_acesso']= True
        else:
            context['message']= 'Voce ja acessou hoje'
        return context


class PersonDetail(LoginRequiredMixin, DetailView):
    model = Person

#diminui a query
    #def get_object(self, queryset=None):
        #pk = self.kwargs.get(self.pk_url_kwarg)
        #return Person.objects.select_related('doc').get(id=pk)




    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['vendas'] = Vendas.objects.filter(
            pessoa_id=self.object.id)
        return context





class PersonCreate(CreateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = "/clientes/person_list"


class PersonUpdate(UpdateView):
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')


class PersonDelete(PermissionRequiredMixin, DeleteView):
    permission_required = ('clientes.deletar_clientes',)
    model = Person
    fields = ['first_name', 'last_name', 'age', 'salary', 'bio', 'photo']
    success_url = reverse_lazy('person_list_cbv')


class ProdutoBulk(View):
    def get(self, request):
        produtos=['banana', 'maca', 'melancia', 'pera', 'limao', 'laranja']
        list_produtos = []

        for produto in produtos:
            p = Produto(descricao=produto, preco=10)
            list_produtos.append(p)

        Produto.objects.bulk_create(list_produtos)

        return HttpResponse('Funcionou')

