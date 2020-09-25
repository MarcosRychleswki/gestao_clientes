from django.contrib import admin

# Register your models here.
from .models import Person
from .models import Produto
from .models import Vendas



class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields':('first_name', 'last_name')}),
        ('Dados complementares',{
            'classes': ('collapse',),
            'fields':('age', 'salary', 'photo')})

    )
    #fields = (('first_name', 'last_name'), ('age', 'salary'), 'bio', 'photo')
    #exlude = ('bio') para excluir um campo
    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'tem_foto')
    list_filter =  ('age', 'salary')


    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Nao'
    short_description = 'Possui foto'



class VendasAdmin(admin.ModelAdmin):
    readonly_fields = ['valor']
    raw_id_fields = ('pessoa', 'produtos')
    list_filter = ('pessoa', 'desconto')
    list_display = ('id', 'pessoa', 'get_total')
    search_fields = ('id', 'pessoa__first_name',)

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'




class ProdutosAdmin(admin.ModelAdmin):
    list_display = ('id', 'descricao', 'preco')
    search_fields = ('id', 'descricao',)

admin.site.register(Person, PersonAdmin)
admin.site.register(Produto, ProdutosAdmin)
admin.site.register(Vendas, VendasAdmin)