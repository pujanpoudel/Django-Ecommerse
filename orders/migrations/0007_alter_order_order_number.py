# Generated by Django 4.1.7 on 2023-04-26 10:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0006_remove_orderproduct_variations_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_number',
            field=models.IntegerField(max_length=20),
        ),
    ]
