# Generated by Django 2.2 on 2019-07-14 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('logistic', '0018_auto_20190703_2002'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserMessage',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False, verbose_name='id')),
                ('message', models.CharField(blank=True, max_length=400, verbose_name='Message')),
                ('onread', models.BooleanField(default=False, verbose_name='OnRead')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='from_user', to='logistic.User')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='to_user', to='logistic.User')),
            ],
        ),
    ]
