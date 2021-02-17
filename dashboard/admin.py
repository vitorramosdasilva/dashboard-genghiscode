from django.contrib import admin

from django.contrib import admin
from .models import Discagem, Operacao, Campanha, TipoCampanha

admin.site.register(Discagem)
admin.site.register(Operacao)
admin.site.register(Campanha)
admin.site.register(TipoCampanha)
