# Generated by Django 5.0.3 on 2024-03-12 07:35

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fifapp', '0002_rename_foto_jugador_jugador_foto_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tecnico',
            name='nacionalidad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fifapp.equipo'),
        ),
    ]
