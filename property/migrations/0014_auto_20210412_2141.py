# Generated by Django 2.2.4 on 2021-04-12 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0013_auto_20210411_1405'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flat',
            name='new_building',
            field=models.NullBooleanField(db_index=True, verbose_name='Новостройка'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='owned_flats',
            field=models.ManyToManyField(db_index=True, related_name='owned_by', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
