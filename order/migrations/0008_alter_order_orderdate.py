# Generated by Django 4.2.4 on 2023-09-09 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0007_remove_order_total_amount_order_orderdate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='OrderDate',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
