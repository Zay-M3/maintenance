# Generated by Django 5.1.2 on 2025-01-10 00:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activos', '0004_rename_area_activo_activos_areaactivo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activos',
            name='codigoActivo',
            field=models.BigIntegerField(unique=True),
        ),
    ]
