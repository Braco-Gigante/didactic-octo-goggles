# Generated by Django 2.0 on 2018-11-11 10:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0013_benefactor_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cost',
            old_name='benefactor',
            new_name='trip',
        ),
    ]
