# Generated by Django 2.2 on 2019-07-16 18:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0034_auto_20190716_2140'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='cashsumm',
            field=models.IntegerField(blank=True, default=0, help_text='Сумма денег которую надо получить от клиента, если оплата не по безналу', verbose_name='Сумма денег'),
        ),
    ]