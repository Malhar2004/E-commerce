# Generated by Django 4.2.1 on 2023-06-02 11:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_rename_name_contact_name'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='contact',
            new_name='contact_us',
        ),
    ]
