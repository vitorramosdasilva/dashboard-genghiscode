from django.urls import path
from . import views
from .views import IndexView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    # path('dados/', DadosJSONView.as_view(), name='dados'),
    path('discagem-unicas/', views.discagem_unicas, name='discagem-unicas'),
    path('discagem-tentativas/', views.discagem_tentativas, name='discagem-tentativas'),
    path('discagem-acordos/', views.discagem_acordos, name='discagem-acordos'),
    path('classificacao-unicas/', views.discagem_classificacao_unicas, name='classificacao-unicas'),
    path('discagem-maquinas/', views.discagem_maquinas, name='discagem-maquinas'),
    
    # path('population-chart/', views.population_chart, name='population-chart'),
    # path('dadospie/', DadosPieJSONView.as_view(), name='pie'),
    # path('dados/', DadosDonutJSONView.as_view(), name='donut'),
]