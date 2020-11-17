# Generated by Django 3.1.1 on 2020-11-17 03:27

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_remove_exercise_exercise'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exercise',
            name='body_part',
            field=multiselectfield.db.fields.MultiSelectField(choices=[(1, 'CHEST'), (2, 'LEGS'), (3, 'ARMS'), (4, 'CALFS'), (5, 'HASTRINGS'), (6, 'QUADRICEPS'), (7, 'SHOULDERS'), (8, 'GLUTEUS'), (9, 'BACK'), (10, 'ABS')], max_length=20),
        ),
    ]