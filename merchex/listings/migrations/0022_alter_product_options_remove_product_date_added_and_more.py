# Generated by Django 4.0.5 on 2022-06-24 10:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listings', '0021_rename_nomproduit_product_name_remove_product_prix_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={},
        ),
        migrations.RemoveField(
            model_name='product',
            name='date_added',
        ),
        migrations.AddField(
            model_name='product',
            name='slug',
            field=models.SlugField(default='', max_length=128),
            preserve_default=False,
        ),
    ]