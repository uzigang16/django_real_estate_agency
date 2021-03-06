# Generated by Django 2.2.4 on 2021-04-11 11:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20210409_2100'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='flat',
            name='owner',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owner_pure_phone',
        ),
        migrations.RemoveField(
            model_name='flat',
            name='owners_phonenumber',
        ),
        migrations.AlterField(
            model_name='owner',
            name='owned_flats',
            field=models.ManyToManyField(related_name='flats_owned', to='property.Flat', verbose_name='Квартиры в собственности'),
        ),
    ]
