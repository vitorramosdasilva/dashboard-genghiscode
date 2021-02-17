# Generated by Django 3.0.8 on 2021-01-18 23:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campanha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_campanha', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=250)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'campanha',
            },
        ),
        migrations.CreateModel(
            name='Carteira',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_carteira', models.IntegerField()),
                ('dt_referencia', models.DateField()),
                ('nr_conta', models.IntegerField()),
                ('carteira', models.CharField(max_length=200)),
                ('faixa', models.CharField(max_length=200)),
                ('qtd_carteira', models.IntegerField()),
                ('vl_carteira', models.DecimalField(decimal_places=2, max_digits=18)),
                ('qtd_pagamentos', models.IntegerField()),
                ('vl_pago', models.DecimalField(decimal_places=2, max_digits=18)),
                ('qtd_pag_acordo', models.IntegerField()),
                ('pagamento_acordo', models.DecimalField(decimal_places=2, max_digits=18)),
                ('qtd_colchao', models.IntegerField()),
                ('PagamentoColchao', models.DecimalField(decimal_places=2, max_digits=18)),
                ('qtd_espontaneo', models.IntegerField()),
                ('pagamento_espontaneo', models.DecimalField(decimal_places=2, max_digits=18)),
            ],
            options={
                'db_table': 'carteira',
            },
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_campanha', models.IntegerField()),
                ('mailing', models.CharField(max_length=200)),
                ('data', models.DateField()),
                ('recebido', models.IntegerField()),
                ('importado', models.IntegerField()),
                ('trabalhado', models.IntegerField()),
                ('campanha', models.CharField(max_length=150)),
            ],
            options={
                'db_table': 'mailing',
            },
        ),
        migrations.CreateModel(
            name='Operacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_operacao', models.CharField(max_length=150)),
                ('descricao', models.CharField(max_length=250)),
                ('data_criacao', models.DateField(auto_now_add=True)),
                ('data_alteracao', models.DateField(auto_now=True)),
            ],
            options={
                'db_table': 'operacao',
            },
        ),
        migrations.CreateModel(
            name='Tempo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id_campanha', models.IntegerField()),
                ('campanha', models.CharField(max_length=150)),
                ('data', models.DateField()),
                ('login', models.IntegerField()),
                ('status', models.CharField(max_length=100)),
                ('tempo', models.IntegerField()),
            ],
            options={
                'db_table': 'tempo',
            },
        ),
        migrations.CreateModel(
            name='TipoCampanha',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipoCampanha', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'tipocampanha',
            },
        ),
        migrations.CreateModel(
            name='Discagem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField()),
                ('classificacao', models.CharField(max_length=150)),
                ('tabulacao', models.CharField(max_length=200)),
                ('faixa', models.CharField(max_length=200)),
                ('unic', models.IntegerField()),
                ('tentativas', models.IntegerField()),
                ('campanha', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Campanha')),
            ],
            options={
                'db_table': 'discagem',
            },
        ),
        migrations.AddField(
            model_name='campanha',
            name='operacao',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Operacao'),
        ),
        migrations.AddField(
            model_name='campanha',
            name='tipoCampanha',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.TipoCampanha'),
        ),
    ]
