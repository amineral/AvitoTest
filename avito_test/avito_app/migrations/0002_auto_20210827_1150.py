# Generated by Django 3.2.6 on 2021-08-27 11:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avito_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='operation',
            name='wallet',
        ),
        migrations.AddField(
            model_name='client',
            name='balance',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='client',
            name='currency',
            field=models.CharField(default='RUB', max_length=20),
        ),
        migrations.DeleteModel(
            name='Wallet',
        ),
    ]
