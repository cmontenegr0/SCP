# Generated by Django 4.1 on 2022-09-02 02:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('planeadores', '0003_unidad_numero_unidad'),
    ]

    operations = [
        migrations.AlterField(
            model_name='unidad',
            name='numero_unidad',
            field=models.CharField(max_length=255),
        ),
    ]
