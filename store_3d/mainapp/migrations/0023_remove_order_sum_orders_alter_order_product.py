# Generated by Django 5.0.3 on 2024-03-25 06:30

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0022_alter_order_sum_orders'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='sum_orders',
        ),
        migrations.AlterField(
            model_name='order',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.product'),
        ),
    ]