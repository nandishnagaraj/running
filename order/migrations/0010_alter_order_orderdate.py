# Generated by Django 4.2.4 on 2023-09-09 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0009_alter_order_orderdate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
