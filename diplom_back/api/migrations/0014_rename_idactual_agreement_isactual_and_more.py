# Generated by Django 5.0.4 on 2024-05-16 17:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0013_user_login'),
    ]

    operations = [
        migrations.RenameField(
            model_name='agreement',
            old_name='idActual',
            new_name='isActual',
        ),
        migrations.AddField(
            model_name='agreement',
            name='idTpStringNew',
            field=models.CharField(db_column='TPAllGostId', default='-', max_length=256, verbose_name='Все Id Гостов'),
        ),
        migrations.AddField(
            model_name='tp',
            name='idTpString',
            field=models.CharField(db_column='TPAllGostId', default='-', max_length=256, verbose_name='Все Id Гостов'),
        ),
        migrations.AlterField(
            model_name='agreement',
            name='idTP',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.tp', verbose_name='id ТП'),
        ),
    ]
