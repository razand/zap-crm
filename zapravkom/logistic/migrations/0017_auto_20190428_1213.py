# Generated by Django 2.2 on 2019-04-28 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0016_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='cartridge',
            name='price',
            field=models.IntegerField(default=0, verbose_name='Цена'),
        ),
        migrations.AlterField(
            model_name='cartridge',
            name='resourse',
            field=models.IntegerField(default=0),
        ),
    ]