# Generated by Django 2.0 on 2018-11-11 03:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0005_auto_20181111_0313'),
    ]

    operations = [
        migrations.AddField(
            model_name='cost',
            name='receipt',
            field=models.ImageField(default='receipts/default.png', upload_to='receipts/'),
        ),
    ]
