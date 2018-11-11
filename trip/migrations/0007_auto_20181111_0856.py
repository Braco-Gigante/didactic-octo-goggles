# Generated by Django 2.0 on 2018-11-11 08:56

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('trip', '0006_cost_receipt'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='name',
            field=models.CharField(default=django.utils.timezone.now, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='trip',
            name='benefactor',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='trip.Benefactor'),
        ),
    ]
