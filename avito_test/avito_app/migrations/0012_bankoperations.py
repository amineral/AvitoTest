# Generated by Django 3.2.6 on 2021-09-04 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('avito_app', '0011_rename_balance_changing_operation_value'),
    ]

    operations = [
        migrations.CreateModel(
            name='BankOperations',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('operation_type', models.CharField(max_length=4)),
                ('value', models.IntegerField(default=0)),
                ('client_to', models.ForeignKey(default=None, on_delete=django.db.models.deletion.CASCADE, to='avito_app.client')),
            ],
        ),
    ]
