# Generated by Django 3.1.1 on 2020-09-26 04:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_auto_20200925_2330'),
    ]

    operations = [
        migrations.RenameField(
            model_name='serie',
            old_name='set_bellown',
            new_name='father_set',
        ),
    ]