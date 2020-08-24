from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from chartjs.views.columns import BaseColumnsHighChartsView
from chartjs.views.pie import HighChartPieView, HighChartDonutView
from django.shortcuts import render
from .models import Discagem
from django.db.models import Sum
from django.http import JsonResponse


class IndexView(TemplateView):
    template_name = 'index-grid.html'


def discagem_unicas(request):
    labels = []
    data = []

    queryset = Discagem.objects.values('data').annotate(discagem_total=Sum('unic')).order_by('data')

    for entry in queryset:
        labels.append(entry['data'])
        data.append(entry['discagem_total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def discagem_tentativas(request):
    labels = []
    data = []

    queryset = Discagem.objects.values('data').annotate(discagem_total=Sum('tentativas')).order_by('data')

    for entry in queryset:
        labels.append(entry['data'])
        data.append(entry['discagem_total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def discagem_acordos(request):
    labels = []
    data = []

    queryset = Discagem.objects.values('data').filter(classificacao='ACORDO').annotate(discagem_total=Sum('unic')).order_by('data')

    for entry in queryset:
        labels.append(entry['data'])
        data.append(entry['discagem_total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
 

def discagem_classificacao_unicas(request):
    labels = []
    data = []

    queryset = Discagem.objects.values('classificacao').annotate(discagem_total=Sum('unic')).order_by('classificacao')

    for entry in queryset:
        labels.append(entry['classificacao'])
        data.append(entry['discagem_total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })

def discagem_maquinas(request):
    labels = []
    data = []

    queryset = Discagem.objects.values('data').filter(classificacao='MAQUINA').annotate(discagem_total=Sum('unic')).order_by('data')

    for entry in queryset:
        labels.append(entry['data'])
        data.append(entry['discagem_total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })
    
# class DadosJSONView(BaseLineChartView):

#     def get_labels(self):
#         queryset = Discagem.objects.values('data').distinct().order_by('data')
#         """Retorna 12 labels para a representação do x"""        
#         labels(queryset)

#         return labels

#     def get_providers(self):
#         queryset = Discagem.objects.values('campanha').distinct().order_by('data')
#         """Retorna os nomes dos datasets."""
#         datasets(queryset)
#         return datasets

#     def get_data(self):
#         """
#         Retorna 6 datasets para plotar o gráfico.

#         Cada linha representa um dataset.
#         Cada coluna representa um label.

#         A quantidade de dados precisa ser igual aos datasets/labels

#         12 labels, então 12 colunas.
#         6 datasets, então 6 linhas.
#         """
#         queryset = Discagem.objects.values('data', 'campanha').annotate(discagem_total=Sum('unic')).order_by('data', 'campanha')
#         dados.append(queryset)
#         for l in range(6):
#             for c in range(12):
#                 dado = [
#                     randint(1, 100),  # jan
#                     randint(1, 100),  # fev
#                     randint(1, 100),  # mar
#                     randint(1, 100),  # abr
#                     randint(1, 100),  # mai
#                     randint(1, 100),  # jun
#                     randint(1, 100),  # jul
#                     randint(1, 100),  # ago
#                     randint(1, 100),  # set
#                     randint(1, 100),  # out
#                     randint(1, 100),  # nov
#                     randint(1, 100)   # dez
#                 ]
#             dados.append(dado)
#         return dados
