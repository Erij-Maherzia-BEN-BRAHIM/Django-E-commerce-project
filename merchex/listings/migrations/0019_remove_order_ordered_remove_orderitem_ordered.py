# Generated by Django 4.0.5 on 2022-06-23 17:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0018_remove_order_date_order_ordered_order_ordered_date_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='ordered',
        ),
        migrations.RemoveField(
            model_name='orderitem',
            name='ordered',
        ),
    ]