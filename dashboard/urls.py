from django.urls import path

from .views import IndexView, DadosJSONView


urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('dados/', DadosJSONView.as_view(), name='dados'),
    # path('dadospie/', DadosPieJSONView.as_view(), name='pie'),
    # path('dados/', DadosDonutJSONView.as_view(), name='donut'),
]