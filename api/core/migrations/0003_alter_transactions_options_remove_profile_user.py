# Generated by Django 4.1.7 on 2023-04-01 19:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_categorytransaction_paymentmethodtransaction_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='transactions',
            options={'verbose_name': 'Транзакция', 'verbose_name_plural': 'Транзакции'},
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
    ]