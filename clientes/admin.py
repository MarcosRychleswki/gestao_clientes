from django.contrib import admin

# Register your models here.
from .models import Person



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
    search_fields = ('id', 'first_name')


    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Nao'
    short_description = 'Possui foto'













admin.site.register(Person, PersonAdmin)
