# Generated by Django 2.0 on 2018-11-11 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0003_auto_20181111_0003'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cost',
            name='when',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trip',
            name='end',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='trip',
            name='start',
            field=models.CharField(max_length=100),
        ),
    ]
