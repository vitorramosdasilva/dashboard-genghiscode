from random import randint
from django.views.generic import TemplateView
from chartjs.views.lines import BaseLineChartView
from chartjs.views.columns import BaseColumnsHighChartsView
from chartjs.views.pie import HighChartPieView, HighChartDonutView
from django.shortcuts import render
from .models import Discagem, Campanha, TipoCampanha
from django.db.models import Sum
from django.http import JsonResponse
from django.db.models import F
# from django.views.generic.base import View
# from django.core import serializers
from django.db.models import Q
from django.db.models.expressions import RawSQL


class IndexView(TemplateView):
    template_name = "index-grid.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tipo_campanha'] = TipoCampanha.objects.values('tipoCampanha', 'id').order_by('id')
        context['campanha'] = Campanha.objects.values('nome_campanha', 'id').order_by('id')
        return context


class SobreView(TemplateView):
    template_name = "sobre.html"


# estou aqui ...
def funcao_total_alo(request):

    filtro_visao = request.GET.get('visao')
    filtro_campanha = request.GET.get('ck_campanha')
    filtro_id_tipo_campanha = request.GET.get('tipo_campanha')
    # print(str(filtro_id_tipo_campanha))
    q = Q()

    if not filtro_visao:
        filtro_visao = 'tentativas'
    if filtro_campanha:
        listCampanha = [str(ck_campanha) for ck_campanha in filtro_campanha.split(',')]
        q &= Q(campanha__nome_campanha__in=listCampanha)
    if filtro_id_tipo_campanha and str(filtro_id_tipo_campanha) != 'Selecione':
        q &= Q(campanha__tipoCampanha=filtro_id_tipo_campanha)
    if not q:
        q &= Q(campanha__nome_campanha__contains='Banpara')

    data = {
        'data': Discagem.objects.filter(classificacao__in=['ALO', 'CPC', 'IMPRODUTIVO', 'ACORDO']).filter(q).aggregate(alo=Sum(filtro_visao))
    }
    return JsonResponse(data, safe=False)


def funcao_total_cpc(request):

    filtro_visao = request.GET.get('visao')
    filtro_campanha = request.GET.get('ck_campanha')
    filtro_id_tipo_campanha = request.GET.get('tipo_campanha')
    # print(str(filtro_id_tipo_campanha))
    q = Q()

    if not filtro_visao:
        filtro_visao = 'tentativas'
    if filtro_campanha:
        listCampanha = [str(ck_campanha) for ck_campanha in filtro_campanha.split(',')]
        q &= Q(campanha__nome_campanha__in=listCampanha)
    if filtro_id_tipo_campanha and str(filtro_id_tipo_campanha) != 'Selecione':
        q &= Q(campanha__tipoCampanha=filtro_id_tipo_campanha)
    if not q:
        q &= Q(campanha__nome_campanha__contains='Banpara')

    data = {
        'data': Discagem.objects.filter(classificacao__in=['CPC', 'ACORDO']).filter(q).aggregate(cpc=Sum(filtro_visao))
    }
    return JsonResponse(data, safe=False)


def funcao_total_acordo(request):

    filtro_visao = request.GET.get('visao')
    filtro_campanha = request.GET.get('ck_campanha')
    filtro_id_tipo_campanha = request.GET.get('tipo_campanha')
    # print(str(filtro_id_tipo_campanha))
    q = Q()

    if not filtro_visao:
        filtro_visao = 'tentativas'
    if filtro_campanha:
        listCampanha = [str(ck_campanha) for ck_campanha in filtro_campanha.split(',')]
        q &= Q(campanha__nome_campanha__in=listCampanha)
    if filtro_id_tipo_campanha and str(filtro_id_tipo_campanha) != 'Selecione':
        q &= Q(campanha__tipoCampanha=filtro_id_tipo_campanha)
    if not q:
        q &= Q(campanha__nome_campanha__contains='Banpara')

    data = {
        'data': Discagem.objects.filter(classificacao='ACORDO').filter(q).aggregate(acordo=Sum(filtro_visao))
    }
    return JsonResponse(data, safe=False)


def funcao_acordo_cpc(request):

    filtro_visao = request.GET.get('visao')
    filtro_campanha = request.GET.get('ck_campanha')
    filtro_id_tipo_campanha = request.GET.get('tipo_campanha')
    # print(str(filtro_id_tipo_campanha))
    q = Q()

    if not filtro_visao:
        filtro_visao = 'tentativas'
    if filtro_campanha:
        listCampanha = [str(ck_campanha) for ck_campanha in filtro_campanha.split(',')]
        q &= Q(campanha__nome_campanha__in=listCampanha)
    if filtro_id_tipo_campanha and str(filtro_id_tipo_campanha) != 'Selecione':
        q &= Q(campanha__tipoCampanha=filtro_id_tipo_campanha)
    if not q:
        q &= Q(campanha__nome_campanha__contains='Banpara')

    acordo = Discagem.objects.filter(classificacao='ACORDO').filter(q).aggregate(acordo=Sum(filtro_visao))
    cpc = Discagem.objects.filter(classificacao__in=['CPC', 'ACORDO']).filter(q).aggregate(cpc=Sum(filtro_visao))

    if not cpc['cpc']:
        data_acordo_cpc = 0.0
    else:
        data_acordo_cpc = round((float(acordo['acordo'])/float(cpc['cpc'])) * 100, 2)

    data = {'data_acordo_cpc': data_acordo_cpc}
    return JsonResponse(data, safe=False)


def funcao_acordo_alo(request):

    filtro_visao = request.GET.get('visao')
    filtro_campanha = request.GET.get('ck_campanha')
    filtro_id_tipo_campanha = request.GET.get('tipo_campanha')
    # print(str(filtro_id_tipo_campanha))
    q = Q()

    if not filtro_visao:
        filtro_visao = 'tentativas'
    if filtro_campanha:
        listCampanha = [str(ck_campanha) for ck_campanha in filtro_campanha.split(',')]
        q &= Q(campanha__nome_campanha__in=listCampanha)
    if filtro_id_tipo_campanha and str(filtro_id_tipo_campanha) != 'Selecione':
        q &= Q(campanha__tipoCampanha=filtro_id_tipo_campanha)
    if not q:
        q &= Q(campanha__nome_campanha__contains='Banpara')

    cpc = Discagem.objects.filter(classificacao__in=['CPC', 'ACORDO']).filter(q).aggregate(cpc=Sum(filtro_visao))
    atendidas = Discagem.objects.filter(classificacao__in=['ALO', 'CPC', 'IMPRODUTIVO', 'ACORDO']).filter(q).aggregate(atendidas=Sum(filtro_visao))

    if not atendidas['atendidas']:
        data_acordo_alo = 0.0
    else:
        data_acordo_alo = round((float(cpc['cpc']) / float(atendidas['atendidas'])) * 100, 2)
    data = {
        'data_acordo_alo': data_acordo_alo
    }
    return JsonResponse(data, safe=False)

# _______________________ Graficos:


def discagem_tentativas(request):
    labels = []
    data = []

    filtro_visao = request.GET.get('visao')
    filtro_campanha = request.GET.get('ck_campanha')
    filtro_id_tipo_campanha = request.GET.get('tipo_campanha')
    # print(str(filtro_id_tipo_campanha))
    q = Q()
    print('eu aqui :' + str(filtro_visao))

    if not filtro_visao:
        filtro_visao = 'tentativas'
    if filtro_campanha:
        listCampanha = [str(ck_campanha) for ck_campanha in filtro_campanha.split(',')]
        q &= Q(campanha__nome_campanha__in=listCampanha)
    if filtro_id_tipo_campanha and str(filtro_id_tipo_campanha) != 'Selecione':
        q &= Q(campanha__tipoCampanha=filtro_id_tipo_campanha)
    if not q:
        q &= Q(campanha__nome_campanha__contains='Banpara')

    queryset = Discagem.objects.values('data').annotate(discagem_total=Sum(filtro_visao)). \
        order_by('data').filter(q)

    for entry in queryset:
        labels.append(entry['data'])
        data.append(entry['discagem_total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def discagem_unicas(request):
    labels = []
    data = []

    filtro_visao = request.GET.get('visao')
    filtro_campanha = request.GET.get('ck_campanha')
    filtro_id_tipo_campanha = request.GET.get('tipo_campanha')
    # print(str(filtro_id_tipo_campanha))
    q = Q()

    if not filtro_visao:
        filtro_visao = 'tentativas'
    if filtro_campanha:
        listCampanha = [str(ck_campanha) for ck_campanha in filtro_campanha.split(',')]
        q &= Q(campanha__nome_campanha__in=listCampanha)
    if filtro_id_tipo_campanha and str(filtro_id_tipo_campanha) != 'Selecione':
        q &= Q(campanha__tipoCampanha=filtro_id_tipo_campanha)
    if not q:
        q &= Q(campanha__nome_campanha__contains='Banpara')

    queryset = Discagem.objects.values('campanha__nome_campanha').\
        annotate(discagem_total=Sum(filtro_visao)).\
        order_by('campanha__nome_campanha').prefetch_related('campanha').filter(q)

    # print(queryset.query)
    for entry in queryset:
        labels.append(entry['campanha__nome_campanha'])
        data.append(entry['discagem_total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def discagem_acordos(request):
    labels = []
    data = []

    filtro_visao = request.GET.get('visao')
    filtro_campanha = request.GET.get('ck_campanha')
    filtro_id_tipo_campanha = request.GET.get('tipo_campanha')
    # print(str(filtro_id_tipo_campanha))
    q = Q()

    if not filtro_visao:
        filtro_visao = 'tentativas'
    if filtro_campanha:
        listCampanha = [str(ck_campanha) for ck_campanha in filtro_campanha.split(',')]
        q &= Q(campanha__nome_campanha__in=listCampanha)
    if filtro_id_tipo_campanha and str(filtro_id_tipo_campanha) != 'Selecione':
        q &= Q(campanha__tipoCampanha=filtro_id_tipo_campanha)
    if not q:
        q &= Q(campanha__nome_campanha__contains='Banpara')

    queryset = Discagem.objects.values('data').filter(classificacao='ACORDO').\
        annotate(discagem_total=Sum(filtro_visao)).order_by('data').filter(q)

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
    queryset = {}

    filtro_visao = request.GET.get('visao')
    filtro_campanha = request.GET.get('ck_campanha')
    filtro_id_tipo_campanha = request.GET.get('tipo_campanha')

    print(str(filtro_id_tipo_campanha))
    q = Q()

    if not filtro_visao:
        filtro_visao = 'tentativas'
    if filtro_campanha:
        listCampanha = [str(ck_campanha) for ck_campanha in filtro_campanha.split(',')]
        q &= Q(campanha__nome_campanha__in=listCampanha)
    if filtro_id_tipo_campanha and str(filtro_id_tipo_campanha) != 'Selecione':
        q &= Q(campanha__tipoCampanha=filtro_id_tipo_campanha)
    if not q:
        q &= Q(campanha__nome_campanha__contains='Banpara')

    cpc = Discagem.objects.values('classificacao').filter(classificacao__in=['CPC', 'ACORDO']).filter(q).aggregate(
        discagem_total=Sum(filtro_visao))

    atendidas = Discagem.objects.values('classificacao').filter(classificacao__in=['ALO', 'CPC', 'IMPRODUTIVO', 'ACORDO']).filter(q).aggregate(
            discagem_total=Sum(filtro_visao))

    improdutivo = Discagem.objects.values('classificacao').filter(classificacao__in=['IMPRODUTIVO']).filter(q).aggregate(discagem_total=Sum(filtro_visao))

    acordo = Discagem.objects.values('classificacao').filter(classificacao__in=['ACORDO']).filter(q).aggregate(discagem_total=Sum(filtro_visao))
    maquina = Discagem.objects.values('classificacao').filter(classificacao__in=['MAQUINA']).filter(q).aggregate(discagem_total=Sum(filtro_visao))

    queryset['Cpc'] = cpc
    queryset['Atendidas'] = atendidas
    queryset['Improdutivo'] = improdutivo
    queryset['Acordo'] = acordo
    queryset['Maquina'] = maquina

    # print(queryset)

    for entry in queryset:
        labels.append(entry)

    data.append(queryset['Cpc']['discagem_total'])
    data.append(queryset['Atendidas']['discagem_total'])
    data.append(queryset['Improdutivo']['discagem_total'])
    data.append(queryset['Acordo']['discagem_total'])
    data.append(queryset['Maquina']['discagem_total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


def discagem_maquinas_unic(request):
    labels = []
    data = []

    filtro_visao = request.GET.get('visao')
    filtro_campanha = request.GET.get('ck_campanha')
    filtro_id_tipo_campanha = request.GET.get('tipo_campanha')
    # print(str(filtro_id_tipo_campanha))
    q = Q()

    if not filtro_visao:
        filtro_visao = 'tentativas'
    if filtro_campanha:
        listCampanha = [str(ck_campanha) for ck_campanha in filtro_campanha.split(',')]
        q &= Q(campanha__nome_campanha__in=listCampanha)
    if filtro_id_tipo_campanha and str(filtro_id_tipo_campanha) != 'Selecione':
        q &= Q(campanha__tipoCampanha=filtro_id_tipo_campanha)
    if not q:
        q &= Q(campanha__nome_campanha__contains='Banpara')

    queryset = Discagem.objects.values('data').filter(classificacao='MAQUINA').\
        annotate(discagem_total=Sum(filtro_visao)).order_by('data').filter(q)

    for entry in queryset:
        labels.append(entry['data'])
        data.append(entry['discagem_total'])

    return JsonResponse(data={
        'labels': labels,
        'data': data,
    })


# Page Error ...
def error_400(request, exception):
    return render(request, '400.html', status=400)


def error_403(request, exception):
    return render(request, '403.html', status=403)


def error_404(request, exception):
    return render(request, '404.html', status=404)


def error_50x(request, exception):
    return render(request, '500.html', status=500)