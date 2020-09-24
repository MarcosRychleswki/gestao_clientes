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
    list_display = ('first_name', 'last_name', 'age', 'salary', 'bio', 'photo')


admin.site.register(Person, PersonAdmin)
admin.site.register(Produto)
admin.site.register(Vendas)