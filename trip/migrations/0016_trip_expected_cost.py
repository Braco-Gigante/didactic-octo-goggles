# Generated by Django 2.0 on 2018-11-11 12:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0015_remove_benefactor_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='expected_cost',
            field=models.FloatField(default=2000),
            preserve_default=False,
        ),
    ]
