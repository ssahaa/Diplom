# Generated by Django 5.0.4 on 2024-05-16 19:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0018_alter_agreement_unique_together_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='agreement',
            name='idTP',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='api.tp', verbose_name='id ТП'),
        ),
    ]
