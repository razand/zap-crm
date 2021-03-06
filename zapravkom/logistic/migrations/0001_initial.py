# Generated by Django 2.2 on 2019-04-09 14:04

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DayTasks',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('process', models.CharField(choices=[('Выполнено', 'Выполнено'), ('Не выполнено', 'Не выполнено'), ('Первый контакт', 'Первый контакт')], default='Первый контакт', max_length=15)),
                ('date', models.DateField(default=django.utils.timezone.now)),
                ('description', models.CharField(max_length=300)),
                ('working_time', models.CharField(default='-', max_length=50)),
                ('phone', models.CharField(default='-', max_length=60)),
                ('contact_name', models.CharField(default='-', max_length=20)),
                ('cashsumm', models.IntegerField(default=0)),
                ('get_set', models.CharField(choices=[('Забрать', 'Забрать'), ('Отдать', 'Отдать')], default='Забрать', max_length=7)),
                ('employee', models.CharField(choices=[('Дмитрий', 'Дмитрий'), ('Владислав', 'Владислав'), ('Сервис', 'Сервис')], default='Сервис', max_length=10)),
                ('replace', models.CharField(default='без подменки', max_length=50)),
                ('payment_method', models.CharField(choices=[('Нал', 'Нал'), ('Безнал', 'Безнал'), ('Без оплаты', 'Без оплаты')], default='Без оплаты', max_length=11)),
            ],
        ),
    ]
