from django.http import HttpResponseNotFound



def nfe_emitida(modeladmin, request, queryset):
    if request.user.has_perm('vendas.setar_nfe'):
        queryset.update(nfe_emitida=True)
    else:
        return HttpResponseNotFound('<h1>Sem permissao </h1>')
nfe_emitida.short_description = "Nfe emitida"