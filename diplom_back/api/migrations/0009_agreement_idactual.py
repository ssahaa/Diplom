# Generated by Django 5.0.4 on 2024-04-24 10:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_alter_gost_dock_iddock_alter_gost_dock_idgost'),
    ]

    operations = [
        migrations.AddField(
            model_name='agreement',
            name='idActual',
            field=models.BooleanField(default=False, verbose_name='Актуальность'),
        ),
    ]
