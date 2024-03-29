# Generated by Django 4.0.5 on 2022-06-24 09:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0020_commande_product_remove_orderitem_item_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='nomProduit',
            new_name='name',
        ),
        migrations.RemoveField(
            model_name='product',
            name='prix',
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='product',
            name='stock',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='static/'),
        ),
    ]
