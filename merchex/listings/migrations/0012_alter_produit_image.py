# Generated by Django 4.0.5 on 2022-06-21 21:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0011_alter_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='listings/static/listings/produits/'),
        ),
    ]
