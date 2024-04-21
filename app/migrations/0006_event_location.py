# Generated by Django 5.0.4 on 2024-04-20 15:21

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_remove_ticket_is_actived'),
    ]

    operations = [
        migrations.AddField(
            model_name='event',
            name='location',
            field=models.CharField(default=django.utils.timezone.now, max_length=50, verbose_name="Lieu de l'evenement"),
            preserve_default=False,
        ),
    ]