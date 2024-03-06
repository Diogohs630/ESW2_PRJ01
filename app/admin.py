from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(UF)
admin.site.register(Cidade)
admin.site.register(Bairro)
admin.site.register(tipoLogradouro)
admin.site.register(Logradouro)
admin.site.register(tipoPessoas)
admin.site.register(Pessoas)
admin.site.register(tipoImovel)
admin.site.register(Imovel)
admin.site.register(ContratoAluguel)
admin.site.register(ContratoVenda)
admin.site.register(Pagamento)
admin.site.register(Locador)
admin.site.register(Locatario)
admin.site.register(Usuario)
admin.site.register(Avalista)