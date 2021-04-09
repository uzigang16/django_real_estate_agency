# Generated by Django 2.2.4 on 2021-04-09 16:22

from django.db import migrations
import phonenumbers


def add_pure_phone(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        try:
            phone = phonenumbers.parse(flat.owners_phonenumber, "RU")
            pure_phone = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
            valid_phone = phonenumbers.is_valid_number(pure_phone)
            flat.owner_pure_phone = valid_phone
            flat.save()
        except AttributeError:
            flat.owner_pure_phone = None


def move_back(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        flat.owner_pure_phone = None


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0008_auto_20210409_1904'),
    ]

    operations = [
        migrations.RunPython(add_pure_phone, move_back)

    ]
