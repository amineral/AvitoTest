# Generated by Django 3.2.6 on 2021-08-30 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('avito_app', '0010_remove_operation_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='operation',
            old_name='balance_changing',
            new_name='value',
        ),
    ]
