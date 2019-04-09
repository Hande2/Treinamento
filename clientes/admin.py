from django.contrib import admin
from .actions import nfe_emitida, nfe_nao_emitida
from .models import Person, Documento, Produto, Venda

class PersonAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Dados pessoais', {'fields': ('first_name', 'last_name', 'doc')}),
        ('Dados complementares', {'fields':  ('age', 'salary', 'photo')})
    )
    #fields = (('doc', 'first_name'), 'last_name', ('age', 'salary'), 'bio', 'photo')
    # exclude = ('bio', )
    list_filter = ('age', 'salary')
    list_display = ('first_name','doc', 'last_name', 'age', 'salary', 'bio', 'tem_foto')
    search_fields = ('id', 'first_name')
    actions =  [nfe_emitida]
    autocomplete_fields = ['doc']

    def tem_foto(self, obj):
        if obj.photo:
            return 'Sim'
        else:
            return 'Não'

    tem_foto.short_description = 'Possui foto'

class VendaAdmin(admin.ModelAdmin):
    readonly_fields = ('valor',)
    autocomplete_fields = ('pessoa',)
    list_filter = ('pessoa__doc', 'desconto')
    list_display = ('id', 'pessoa', 'get_total', 'nfe_emitida')
    search_fields = ('is', 'pessoa__first_name')
    actions = [nfe_emitida, nfe_nao_emitida]
    filter_horizontal = ['produtos',]


class DocumentoAdmin(admin.ModelAdmin):
    search_fields = ['num_doc']



admin.site.register(Person, PersonAdmin)
admin.site.register(Documento, DocumentoAdmin)
admin.site.register(Produto)
admin.site.register(Venda, VendaAdmin)
