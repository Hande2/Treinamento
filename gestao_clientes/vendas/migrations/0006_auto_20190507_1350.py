# Generated by Django 2.2 on 2019-05-07 13:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('produtos', '0001_initial'),
        ('vendas', '0005_auto_20190411_1742'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='itemdopedido',
            unique_together={('venda', 'produto')},
        ),
    ]
