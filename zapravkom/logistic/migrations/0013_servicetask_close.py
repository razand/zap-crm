# Generated by Django 2.2 on 2019-04-13 17:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0012_auto_20190413_2004'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicetask',
            name='close',
            field=models.BooleanField(default=False, verbose_name='финиш'),
        ),
    ]
