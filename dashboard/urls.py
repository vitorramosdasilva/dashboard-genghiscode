from django.urls import path
from . import views
from .views import IndexView, SobreView

app_name = 'dashboard'

urlpatterns = [

    path('', views.IndexView.as_view(), name='index'),
    path('sobre/', views.SobreView.as_view(), name='sobre'),

    # url campanha right dashboard set in context ...
    path('campanha/', views.Campanha, name='campanha'),

    path('total-alo/', views.funcao_total_alo, name='total-alo'),
    path('total-cpc/', views.funcao_total_cpc, name='total-cpc'),
    path('total-acordo/', views.funcao_total_acordo, name='total-acordo'),

    path('acordo-cpc/', views.funcao_acordo_cpc, name='acordo_cpc'),
    path('acordo-alo/', views.funcao_acordo_alo, name='acordo_alo'),

    # url charts .....
    path('discagem-unicas/', views.discagem_unicas, name='discagem-unicas'),
    path('discagem-tentativas/', views.discagem_tentativas, name='discagem-tentativas'),
    path('discagem-acordos/', views.discagem_acordos, name='discagem-acordos'),
    path('classificacao-unicas/', views.discagem_classificacao_unicas, name='classificacao-unicas'),
    path('discagem-maquinas-unic/', views.discagem_maquinas_unic, name='discagem-maquinas-unic'),
]