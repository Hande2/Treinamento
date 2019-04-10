from django.contrib import admin
from .models import Venda
from .models import ItemDoPedido
from .actions import nfe_emitida, nfe_nao_emitida


class ItemPedidoInline(admin.TabularInline):
    model = ItemDoPedido
    extra = 1


class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    autocomplete_fields = ('pessoa',)
    list_filter = ('pessoa__doc',)
    list_display = ('id', 'pessoa', 'nfe_emitida')
    search_fields = ('is', 'pessoa__first_name')
    actions = [nfe_emitida, nfe_nao_emitida]
    #filter_horizontal = ['produtos',]
    inlines = [ItemPedidoInline]

    def total(self, obj):
        return obj.get_total()

    total.short_description = 'Total'


admin.site.register(ItemDoPedido)
admin.site.register(Venda, VendaAdmin)
