# Generated by Django 4.0.5 on 2022-06-22 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0014_alter_produit_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produit',
            name='image',
            field=models.ImageField(blank=True, upload_to='static/'),
        ),
    ]
