# Generated by Django 4.0.5 on 2022-06-21 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0008_fournisseur_produit_remove_listing_band_delete_band_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(upload_to='listings/static/listings/produits'),
        ),
    ]
