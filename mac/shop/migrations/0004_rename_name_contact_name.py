# Generated by Django 4.2.1 on 2023-06-02 11:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='name',
            new_name='Name',
        ),
    ]