# Generated by Django 2.2.4 on 2021-04-09 17:30

from django.db import migrations


def fill_out_owner(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')
    for flat in Flat.objects.all():
        Owner.objects.get_or_create(
            name=flat.owner,
            phone_number=flat.owners_phonenumber,
            pure_phone_number=flat.owner_pure_phone)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0010_auto_20210409_2023'),
    ]

    operations = [
        migrations.RunPython(fill_out_owner)

    ]
