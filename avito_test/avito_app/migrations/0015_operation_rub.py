# Generated by Django 3.2.6 on 2021-09-07 12:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('avito_app', '0014_auto_20210907_1245'),
    ]

    operations = [
        migrations.AddField(
            model_name='operation',
            name='RUB',
            field=models.IntegerField(default=0),
        ),
    ]