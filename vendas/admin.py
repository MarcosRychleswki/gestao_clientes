from django.contrib import admin
from .actions import nfe_emitida
from .models import ItemDoPedido
from .models import Vendas



class ItemPedidoInLine(admin.TabularInline):
    model = ItemDoPedido
    extra = 1

class VendasAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    autocomplete_fields = ('pessoa',)
    list_filter = ('pessoa', 'desconto')
    list_display = ('id', 'pessoa', 'nfe_emitida')
    search_fields = ('id', 'pessoa__first_name',)
    actions = [nfe_emitida]
    inlines = [ItemPedidoInLine]


    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'



admin.site.register(ItemDoPedido)
admin.site.register(Vendas, VendasAdmin)