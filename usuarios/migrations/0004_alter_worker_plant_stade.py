# Generated by Django 5.1.2 on 2024-11-28 23:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_worker_plant_stade'),
    ]

    operations = [
        migrations.AlterField(
            model_name='worker_plant',
            name='stade',
            field=models.CharField(max_length=100),
        ),
    ]
