# Generated by Django 3.1.3 on 2020-12-01 11:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('exercises', '0009_auto_20201201_1220'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exercise',
            name='variation',
        ),
        migrations.DeleteModel(
            name='ExerciseVariation',
        ),
    ]
